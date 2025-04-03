from lib.gratitudes import Gratitudes

def test_returns_str():
    gratitudes = Gratitudes()
    gratitudes.add("sunny day")
    result = gratitudes.format()
    
    assert isinstance(result, str)

def test_adds_one_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("sunny day")
    result = gratitudes.format()

    assert result == "Be grateful for: sunny day"

def test_adds_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("sunny day")
    gratitudes.add("warm house")
    gratitudes.add("yummy coffee")
    result = gratitudes.format()

    assert result == "Be grateful for: sunny day, warm house, yummy coffee"

def test_adds_to_storage():
    gratitudes = Gratitudes()
    gratitudes.add("sunny day")
    gratitudes.add("warm house")
    gratitudes.add("yummy coffee")

    assert gratitudes.gratitudes == ["sunny day", "warm house", "yummy coffee"]