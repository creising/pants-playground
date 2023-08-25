import logging

import uvicorn
import zmq
from fastapi import FastAPI

from src.python.utils.logit import log_it

log = logging.getLogger("my-api")

context = zmq.Context()
log_it("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://server-container:5555")
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

@app.get("/test")
def read_root():
    log_it("Calling type check")
    message = "It worked!"
    return {"message": message}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
