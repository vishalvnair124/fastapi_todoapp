import conn as con
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    mycursor = con.mydb.cursor(dictionary=True)  # Fetch results as dictionaries

    mycursor.execute("SELECT * FROM tasks")
    myresult = mycursor.fetchall()
    mycursor.close()  # Close the cursor

    return templates.TemplateResponse("index.html", context={"request": request, "tasks": myresult})


@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}


@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "name": name, "price": price}


@app.patch("/items/{item_id}")
def patch_item(item_id: int, name: str = None, price: float = None):
    updated_data = {"item_id": item_id}
    if name is not None:
        updated_data["name"] = name
    if price is not None:
        updated_data["price"] = price
    return updated_data


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted successfully"}
