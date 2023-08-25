
docker_image(
  name="client-container",
  restartable=True
)


#docker run -v $PWD:/share --rm -t python:3.11.4-bullseye bash -c 'python -mvenv pex.venv && ./pex.venv/bin/pip install -U pex && ./pex.venv/bin/pex3 interpreter inspect --python /usr/local/bin/python3.11 --markers --tags --indent 2' > out.json