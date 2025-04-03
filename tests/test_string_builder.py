from lib.string_builder import StringBuilder

def test_string_builder_returns_str():
    builder = StringBuilder()
    builder.add("hello")
    result = builder.output()
    
    assert isinstance(result, str)

def test_string_builder_adds_one_str():
    builder = StringBuilder()
    builder.add("hello")
    result = builder.output()
    
    assert result == "hello"

def test_string_builder_adds_multiple_strings():
    builder = StringBuilder()
    builder.add("hello")
    builder.add(" beautiful")
    builder.add(" souls")
    result = builder.output()
    
    assert result == "hello beautiful souls"

def test_sb_returns_string_size():
    builder = StringBuilder()
    builder.add("hello")
    result = builder.size()
    
    assert result == 5