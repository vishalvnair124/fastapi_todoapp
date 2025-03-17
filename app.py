from typing import Optional
from pydantic import BaseModel
import conn as con  # Import your MySQL connection
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Folder for HTML files


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    desc: Optional[str] = None  



#  Home Route - Display Tasks
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    mycursor = con.mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM tasks")
    tasks = mycursor.fetchall()
    mycursor.close()

    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})


#  Add Task
@app.post("/add/")
async def create_item(title: str = Form(...), desc: str = Form(...)):
    mycursor = con.mydb.cursor()
    sql = "INSERT INTO tasks (task_title, task_desc) VALUES (%s, %s)"
    values = (title, desc)
    mycursor.execute(sql, values)
    con.mydb.commit()
    mycursor.close()

    return RedirectResponse(url="/", status_code=303)  # Redirect back to homepage


# Edit Task Page
@app.get("/edit/{task_id}", response_class=HTMLResponse)
async def edit_task(request: Request, task_id: int):
    mycursor = con.mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
    task = mycursor.fetchone()
    mycursor.close()

    if not task:
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse("edit.html", {"request": request, "task": task})


# Update Task (PUT - Update Title and Description)
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: TaskUpdate):
    mycursor = con.mydb.cursor()

    # Debug: Check if the task exists before updating
    mycursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
    existing_task = mycursor.fetchone()

    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found (Before Update)")

    print(f"Existing Task Found: {existing_task}")  # Debugging

    # Proceed with the update
    sql = "UPDATE tasks SET task_title = %s, task_desc = %s WHERE task_id = %s"
    values = (task.title, task.desc, task_id)
    mycursor.execute(sql, values)

    print(f"Rows affected: {mycursor.rowcount}")  # Debugging

    if mycursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task found but not updated")

    mycursor.close()
    return {"message": "Task updated successfully"}



# Partial Update Task (PATCH - Update Only Title)
@app.patch("/tasks/{task_id}")
async def update_task_partial(task_id: int, task: TaskUpdate):
    mycursor = con.mydb.cursor()
    print(task_id)

    # Check if task exists before updating
    mycursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
    existing_task = mycursor.fetchone()
    print(existing_task)

    if not existing_task:
        mycursor.close()
        raise HTTPException(status_code=404, detail="Task not found (Before Update)")

    print(f"Existing Task Found: {existing_task}")  # Debugging

    # Update only the title
    sql = "UPDATE tasks SET task_title = %s WHERE task_id = %s"
    values = (task.title, task_id)
    mycursor.execute(sql, values)

    print(f"Rows affected: {mycursor.rowcount}")  # Debugging

    if mycursor.rowcount == 0:
        mycursor.close()
        raise HTTPException(status_code=404, detail="Task found but not updated")

    mycursor.close()
    return {"message": "Task title updated successfully"}




#  Delete Task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    mycursor = con.mydb.cursor()
    sql = "DELETE FROM tasks WHERE task_id=%s"
    mycursor.execute(sql, (task_id,))
    con.mydb.commit()
    mycursor.close()

    return {"message": "Task deleted successfully"}
