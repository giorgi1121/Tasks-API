import json
import sqlite3
from fastapi import HTTPException, status
class DataClient():
    def __init__(self):
        self.connection = sqlite3.connect("tasks.db")
        self.connection.row_factory = sqlite3.Row
        self.c = self.connection.cursor()

    def close(self):
        self.connection.close()
        
    def initDb(self):
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
                  id INTEGER PRIMARY KEY,
                  title VARCHAR(255) NOT NULL,
                  completed BOOLEAN NOT NULL DEFAULT FALSE
        )
""")
        self.connection.commit()

    def getTasks(self):
        self.c.execute("""
        SELECT * FROM tasks;
""")
        rows = self.c.fetchall()
        self.connection.commit()
        return rows

    def getTask(self, id):
        self.c.execute("""
        SELECT * FROM tasks WHERE id = (?);
""", (id, ))
        row = self.c.fetchone()
        self.connection.commit()
        return row 
    
    def createTask(self, tasks):
        self.c.execute("""
        INSERT INTO tasks (id, title, completed)
                    VALUES((?), (?), (?))
""", (tasks["id"], tasks["title"], tasks["completed"]))
        self.connection.commit()
        return tasks

    def updateTasks(self, id, new_task):
        self.c.execute("""
        UPDATE tasks SET title = ?, completed = ? WHERE id = ?
""", (new_task["title"], new_task["completed"], id))
        self.connection.commit()
        return new_task
    
    def deleteTask(self, id):
        self.c.execute("""
        DELETE FROM tasks WHERE id = ?
""", (id, ))
        self.connection.commit()
