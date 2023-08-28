python_sources()

python_tests(
    name="tests",
    skip_mypy=True
)

pex_binary(
  name="binary",
  entry_point="src.python.api.main",
)

pex_binary(
  name="binary-linux",
  entry_point="src.python.api.main",
  layout = "packed",
  execution_mode = "venv",
  complete_platforms = ["src/python:platforms"]
)
