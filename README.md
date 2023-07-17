# Tasks-API

## main.py
- Created main.py file wich creates main server with using FastAPI;

## dataClient.py
- Created dataClient.py file which is used for communication with data base;

## crud.py
- Created crud.py file which is used for communication to server. It is command-line ToDo App client; 
  
## tasks.py
- Created tasks.py which creates TaskClient class. That class is used in crud.py file for sending requests to the main server;
  
## tasks.db
- tasks.db file will be created after running the application.

# How to use?
For running the progrram you should type following code in terminal: "uvicorn main:app --reload"

After running this command,the server will start. So you can use crud.py as a Client app to send requests. You can read all tasks or just one task by id. Also you can create new task, update older one or delete by id.
