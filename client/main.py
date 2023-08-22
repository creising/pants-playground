from typing import Union
from fastapi import FastAPI
import zmq
import logging
from logger import log_it

log = logging.getLogger("my-api")

# def log_it(input):
#     print(input, flush=True)

context = zmq.Context()
log_it("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://python-fun-server-app-1:5555")
log_it("Connected to socket")

app = FastAPI()


@app.get("/")
def read_root():
    log_it("Sending hello")
    socket.send(b"Hello")
    log_it("Sent! Waiting for message")
    message = socket.recv()
    log_it("Got message")
    return {"message": message}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def add_bang(input):
    return f"{input}!"
