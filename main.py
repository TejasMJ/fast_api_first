from fastapi import FastAPI

app = FastAPI()

items = []


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fastapi")
def read_root():
    return {"Hello": "From FastAPI"}

@app.get("/fast")
def read_root():
    test_varable = "Hello from FastAPI"
    return f"<h1>{test_varable}</h1>"

@app.post("/items/")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item not found"}
    return {"item": items[item_id]}