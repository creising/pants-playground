import logging
import os
import random

import uvicorn
import zmq
from fastapi import FastAPI

from src.python.utils.logit import log_it

log = logging.getLogger("my-api")

context = zmq.Context()
log_it("Connecting to hello world server…")
socket = context.socket(zmq.REQ)

processorUrl = os.environ.get("PROC_URL") or "localhost"
connect_url = f"tcp://{processorUrl}:5555"
log_it(f"URL: {connect_url}")
socket.connect(connect_url)

log_it("Connected to socket")

app = FastAPI()


@app.get("/")
def read_root():
    num = random.randint(0, 100)
    log_it(f"Sending number {num}")
    socket.send_string(str(num))
    message = socket.recv_string()
    log_it("Got message")
    return {"message": message}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
