python_sources()

pex_binary(
  name="binary",
  entry_point="src.python.processor.main:main",
  layout = "packed",
  execution_mode = "venv",
)

pex_binary(
  name="binary-linux",
  entry_point="src.python.processor.main:main",  layout = "packed",
  execution_mode = "venv",
  complete_platforms = ["src/python:platforms"]
)
