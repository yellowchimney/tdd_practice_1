from lib.check_codeword import check_codeword

def test_correct_codeword():
    assert check_codeword("horse") == "Correct! Come in."

def test_words_starting_with_h():
    assert check_codeword("hose") == "Close, but nope."

def test_wrong_codeword():
    assert check_codeword("physics") == "WRONG!"