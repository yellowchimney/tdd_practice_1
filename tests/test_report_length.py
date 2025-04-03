from lib.report_length import report_length

def test_returns_correct_length():
    assert report_length("hello") == "This string was 5 characters long."

def test_returns_string():
    result = report_length("hello")
    assert isinstance(result, str)