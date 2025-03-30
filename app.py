from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# SQLite config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False) 

with app.app_context():
    db.create_all()
#     new_todo = Todo(title="Test Item 1", complete=False)
#     db.session.add(new_todo)
#     db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-task')
def todo_form():
    return render_template('form.html')

@app.route('/tasks', methods=['GET'])
def get_todos():
    try:
        todos = Todo.query.order_by(Todo.complete.asc()).all()
        return jsonify([{
            'id': todo.id,
            'title': todo.title,
            'complete': todo.complete
        } for todo in todos])
    except Exception as e:
        return jsonify({
            'error': 'Internal Server Error',
            'message': f'Failed to fetch tasks: {str(e)}'
        }), 500

@app.route('/tasks/<int:id>', methods=['GET'])
def get_todo(id):
    try:
        todo = Todo.query.get_or_404(id)
        return jsonify([{
            'id': todo.id,
            'title': todo.title,
            'complete': todo.complete
        }])
    except Exception as e:
        return jsonify({
            'error': 'Not found',
            'message': f'Task with ID {id} not found'
        }), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.get_json()
    
    if not data or 'complete' not in data:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Complete status is required'
        }), 400
    
    if type(data['complete']) != bool:
        return jsonify({
           'error': 'Bad Request',
           'message': 'Complete status must be a boolean'
    }), 400
    
    todo.complete = data.get('complete', todo.complete)

    db.session.commit()
    return jsonify({
        'id': todo.id,
        'title': todo.title,
        'complete': todo.complete
    })

@app.route('/tasks', methods=['POST'])
def create_todo():
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Task title is required'
        }), 400
    
    if len(data['title'].strip()) == 0:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Task title cannot be an empty string'
        }), 400
    
    todo = Todo(
        title=data['title'].strip(),
        complete=False
    )
    
    db.session.add(todo)
    db.session.commit()

    return jsonify({
        'id': todo.id,
        'title': todo.title,
        'complete': todo.complete
    }), 201

if __name__ == "__main__":
    app.run(debug=True)