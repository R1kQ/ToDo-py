# ToDo-py

This is a simple Todo List application built with Flask a Python web framework.
The application provides a RESTful API  for managing tasks (create, read, and update) and a frontend interface for interacting with the API.


# Steps to start up app
<br>
1. Make sure you have Python installed on your system

    https://www.python.org/downloads/
   
<br>
2. Clone repository

    https://github.com/R1kQ/ToDo-py.git

<br>
3. Install dependencies located in requirements.txt

    python3 -m pip install -r requirements.txt
    
    or

    python -m pip install -r requirements.txt


<br>
4. Run the app from IDE terminal

    python3 app.py
    
    or

    python app.py`


# Curl Command Examples

`curl http://localhost:5000/tasks`

<img width="220" alt="image" src="https://github.com/user-attachments/assets/6f458bf8-b76f-40de-8756-9d7bf655979b" />



`curl http://localhost:5000/tasks/2`

<img width="202" alt="image" src="https://github.com/user-attachments/assets/ba0a4c6a-22fb-42bc-aa2a-775a6b650eca" />



`curl --noproxy -x POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Buy groceries"}'`

<img width="187" alt="image" src="https://github.com/user-attachments/assets/31781f3c-97ed-402d-b62e-037dd69f295e" />




`curl -X PUT http://localhost:5000/tasks/4 -H "Content-Type: application/json" -d '{"complete": true}'`
<img width="197" alt="image" src="https://github.com/user-attachments/assets/8ddd05de-76ae-44b4-a739-bd2351ea1a0d" />



# Error Curl Command Examples
`curl --noproxy -x POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": ""}'`
<br>
<img width="378" alt="image" src="https://github.com/user-attachments/assets/31036ea0-5e09-447f-900f-af1d08225bae" />

`curl -X PUT http://localhost:5000/tasks/4 -H "Content-Type: application/json" -d '{"complete": ""}'`
<img width="356" alt="image" src="https://github.com/user-attachments/assets/c98898a2-236c-402d-9a3c-40a0540efefc" />

