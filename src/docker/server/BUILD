
# Define a docker image that can be used to ship our Python env truly everywhere
docker_image(name="server-container")
# in a newer version this will be build_platform=["linux/amd64"]

# file(name="platforms", source="./platforms.json")

#docker run -v $PWD:/share --rm -t python:3.11.4-bullseye bash -c 'python -mvenv pex.venv && ./pex.venv/bin/pip install -U pex && ./pex.venv/bin/pex3 interpreter inspect --python /usr/local/bin/python3.11 --markers --tags --indent 2' > out.json