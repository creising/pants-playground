import time

import zmq


def log_it(input):
    print(input, flush=True)


log_it("Starting server!")
context = zmq.Context()
log_it("Created context")
socket = context.socket(zmq.REP)
log_it("Created socket")
socket.bind("tcp://0.0.0.0:5555")
log_it("Bound to local host. Waiting for data")

while True:
    #  Wait for next request from client
    message = socket.recv()
    log_it(f"Received request!: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")
    log_it("message sent")
