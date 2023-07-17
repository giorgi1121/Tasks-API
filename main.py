from typing import Union
from fastapi import FastAPI, status, HTTPException
from dataClient import DataClient

app = FastAPI()
DataClient().initDb()
    

@app.get("/")
def read_root():
    return {"info": "This is simple todo app for managing your daily tasks",
            "tasks_list": "/tasks"
        }

@app.get("/tasks/")
def read_tasks():
    dataClient = DataClient()
    tasks = dataClient.getTasks()
    dataClient.close()
    return tasks

@app.get("/tasks/{tasks_id}")
def read_tasks(tasks_id: int, q: Union[str, None] = None):
    dataClient = DataClient()
    result = dataClient.getTask(tasks_id)
    dataClient.close()
    if result == None:
        raise HTTPException(status_code=404, detail= status.HTTP_404_NOT_FOUND)
    else:
        return result
    
@app.post("/tasks/")
def create_task(task: dict):
    dataClient = DataClient()
    dataClient.createTask(task)
    dataClient.close()
    return "Reacived"

@app.put("/tasks/{tasks_id}")
def update_task(tasks_id: int, new_task: dict):
    dataClient = DataClient()    
    dataClient.updateTasks(tasks_id, new_task)
    dataClient.close()
    return "Updated"

@app.delete("/tasks/{tasks_id}")
def delete_task(tasks_id: int):
    dataClient = DataClient()
    dataClient.deleteTask(tasks_id)
    dataClient.close()
    return tasks_id