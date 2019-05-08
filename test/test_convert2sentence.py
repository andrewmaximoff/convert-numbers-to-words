from main import convert2sentence


def test_convert2sentence_invalid_input():
    assert convert2sentence('+3+7=10') == 'invalid input'


def test_convert2sentence_space():
    assert convert2sentence(' 3  + 7   = 10') == 'three plus seven equals ten'


def test_convert2sentence_billion():
    assert convert2sentence('1923273809 + 7 = 1923273816') == 'one billion nine hundred twenty three million two ' \
                                                              'hundred seventy three thousand eight hundred nine ' \
                                                              'plus seven equals one billion nine hundred twenty ' \
                                                              'three million two hundred seventy three thousand ' \
                                                              'eight hundred sixteen'


def test_convert2sentence_million():
    assert convert2sentence('9706412 + 7 = 9706419') == 'nine million seven hundred six thousand four hundred' \
                                                              ' twelve plus seven equals nine million seven hundred ' \
                                                              'six thousand four hundred nineteen'

