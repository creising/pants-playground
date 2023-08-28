FROM --platform=linux/x86_64 python:3.11.4-bullseye

EXPOSE 8080

COPY src.python.api/binary-linux.pex /app/

ENTRYPOINT ["/app/__main__.py"]