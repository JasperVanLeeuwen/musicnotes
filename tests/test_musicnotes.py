from musicnotes.musicnotes import Guitar, String, Strings


def test_guitar_string():
    guitar = Guitar()
    strings = guitar.strings
    string = strings[1]
    assert isinstance(string, String)

def test_strings_string():
    strings = Strings()
    string = strings[1]
    assert isinstance(string, String)