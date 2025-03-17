import conn as con  # Import your MySQL connection
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Folder for HTML files


# 📌 1️⃣ Home Route - Display Tasks
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    mycursor = con.mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM tasks")
    tasks = mycursor.fetchall()
    mycursor.close()

    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})


# 📌 2️⃣ Add Task
@app.post("/add/")
async def create_item(title: str = Form(...), desc: str = Form(...)):
    mycursor = con.mydb.cursor()
    sql = "INSERT INTO tasks (task_title, task_desc) VALUES (%s, %s)"
    values = (title, desc)
    mycursor.execute(sql, values)
    con.mydb.commit()
    mycursor.close()

    return RedirectResponse(url="/", status_code=303)  # Redirect back to homepage


# 📌 3️⃣ Update Task (PUT - Full Update)
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, title: str, desc: str):
    mycursor = con.mydb.cursor()
    sql = "UPDATE tasks SET task_title=%s, task_desc=%s WHERE task_id=%s"
    values = (title, desc, task_id)
    mycursor.execute(sql, values)
    con.mydb.commit()
    mycursor.close()

    return {"message": "Task updated successfully"}


# 📌 4️⃣ Partial Update Task (PATCH)
@app.patch("/tasks/{task_id}")
async def patch_task(task_id: int, title: str = None, desc: str = None):
    mycursor = con.mydb.cursor()
    
    updates = []
    values = []
    
    if title:
        updates.append("task_title=%s")
        values.append(title)
    
    if desc:
        updates.append("task_desc=%s")
        values.append(desc)

    if updates:
        sql = f"UPDATE tasks SET {', '.join(updates)} WHERE task_id=%s"
        values.append(task_id)
        mycursor.execute(sql, values)
        con.mydb.commit()
    
    mycursor.close()
    return {"message": "Task updated successfully"}


# 📌 5️⃣ Delete Task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    mycursor = con.mydb.cursor()
    sql = "DELETE FROM tasks WHERE task_id=%s"
    mycursor.execute(sql, (task_id,))
    con.mydb.commit()
    mycursor.close()

    return {"message": "Task deleted successfully"}
