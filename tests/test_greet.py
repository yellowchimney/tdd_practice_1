from lib.greet import greet

def test_returns_greeting_with_name():
   
    assert greet("Sasha") == "Hello, Sasha!"
    assert greet("Amina") == "Hello, Amina!"
    