FROM --platform=linux/x86_64 python:3.11.4-bullseye

COPY src.python.client/binary-linux.pex /app/

ENTRYPOINT ["/app/__main__.py"]