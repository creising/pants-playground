# Define a self-contained, relocatable binary that contains a complete Python environment
# (i.e., code and dependencies but not the interpreter itself). See https://pex.readthedocs.io
python_sources()

# python_requirement(
#     name="zmq",
#     requirements=["pyzmq"],
#     modules=["zmq"],
# )


# python_requirements(
#     name="reqs",
#     module_mapping={"pyzmq": ["zmq"]}
# )

# Define a docker image that can be used to ship our Python env truly everywhere
docker_image(name="server-container")
# in a newer version this will be build_platform=["linux/amd64"]

file(name="platforms", source="./platforms.json")

pex_binary(
  name="binary",
  entry_point="server.main:main",
  layout = "packed",
  execution_mode = "venv",
  complete_platforms = [":platforms"]
  # platforms=[
  #   'current',
  #   'linux-x86_64-cp-3.7.5-m',
  # ]
  # shebang="#!/usr/bin/env python3",
  # Enable hot re-load
  # restartable=True
  # platforms=[
  #       "linux-x86_64-cp-3.7.5-cp37m",
  #       # "macosx_10.12_x86_64-cp-310-cp310",
  #   ]
)