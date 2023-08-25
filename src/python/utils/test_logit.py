from src.python.utils.logit import format_message

def test_format_message():
    assert format_message("message") == "Logging message: message"