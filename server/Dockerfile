FROM python:3.11.4-bullseye
RUN apt-get update
# RUN apt-get install -y libzmq3-dev
COPY server/binary.pex /app

ENTRYPOINT ["/app/binary.pex"]
