from main import num2words


def test_num2words_zero():
    assert num2words(0) == 'zero'


def test_num2words_ten():
    assert num2words(10) == 'ten'


def test_num2words_hundred():
    assert num2words(100) == 'one hundred'
    assert num2words(101) == 'one hundred one'
    assert num2words(299) == 'two hundred ninety nine'


def test_num2words_thousand():
    assert num2words(1000) == 'one thousand'
    assert num2words(1001) == 'one thousand one'
    assert num2words(2999) == 'two thousand nine hundred ninety nine'


def test_num2words_million():
    assert num2words(1000000) == 'one million'
    assert num2words(1000001) == 'one million one'
    assert num2words(9999999) == 'nine million nine hundred ninety nine thousand nine hundred ninety nine'


def test_num2words_billion():
    assert num2words(1000000000) == 'one billion'
    assert num2words(1000000001) == 'one billion one'
    assert num2words(9999999999) == 'nine billion nine hundred ninety nine million nine hundred ninety nine thousand' \
                                    ' nine hundred ninety nine'
