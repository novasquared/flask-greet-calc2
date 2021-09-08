from flask import Flask, request
import operations

app = Flask(__name__)

@app.get("/add")
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.add(a,b)
    return str(result)

@app.get("/sub")
def subtract():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.sub(a,b)
    return str(result)

@app.get("/mult")
def multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.mult(a,b)
    return str(result)

@app.get("/div")
def divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.div(a,b)
    return str(result)
