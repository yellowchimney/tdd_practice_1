import pytest
from lib.present import Present

def test_wrap_exception():
    present = Present()
    present.wrap(12)
    with pytest.raises(Exception) as e:
        present.wrap(12)
    assert str(e.value) == "A contents has already been wrapped."

def test_unwrap_exception():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."