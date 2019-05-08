import re

from typing import List, Union, Dict


marks: Dict[str, str] = {
    '-': 'minus',
    '+': 'plus',
    '*': 'multiplication',
    '/': 'division',
    '=': 'equals'
}

nums_20_90: List[str] = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
nums_0_19: List[str] = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                        'Seventeen', 'eighteen', 'nineteen']
nums_dict: Dict[int, str] = {100: 'hundred', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion'}


def result_counter(item: str, items: List[str]) -> Union[bool, None]:
    """ Add item to `result_items`."""
    if item.isdigit():
        if not items:
            items.append(num2words(int(item)))
        elif items[-1] in marks.values():
            items.append(num2words(int(item)))
        else:
            return True
    else:
        if not items:
            return True
        elif items[-1] not in marks.values() and item in marks.keys():
            items.append(marks[item])
        else:
            return True


def num2words(num: int) -> str:
    if num < 20:
        return nums_0_19[num]
    if num < 100:
        return nums_20_90[num//10-2] + ('' if num % 10 == 0 else ' ' + nums_0_19[num % 10])
    max_key = max([key for key in nums_dict.keys() if key <= num])
    return num2words(num//max_key) + ' ' + nums_dict[max_key] \
           + ('' if num % max_key == 0 else ' ' + num2words(num % max_key))


def convert2sentence(sentence: str) -> str:
    sentence = sentence.replace(' ', '')
    items = re.split(r'([+\-*/=])', sentence)
    items = list(filter(lambda x: x, items))  # removal of empty elements

    result_items = []

    for i in items:
        if result_counter(i, result_items):
            return 'invalid input'

    return ' '.join(result_items)


if __name__ == '__main__':
    print(convert2sentence('3+7=10'))  # simple review
