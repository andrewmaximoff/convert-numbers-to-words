# Humanize calculator

### QuickStart
Main function ```convert2sentence```.  Use:
```python
from main import convert2sentence

input_string = '3 + 7 = 10'
output_string = convert2sentence(input_string)  # 'three plus seven equals ten
```

### Testing
All test keep in test dictionary. Requirements [pytest](https://docs.pytest.org/en/latest/) Use:
```bash
$ pytest
================================================================== test session starts ===================================================================
platform linux -- Python 3.7.3, pytest-4.4.1, py-1.8.0, pluggy-0.11.0
rootdir: /home/am/Code/pet-projects/convert-numbers-to-words
collected 10 items                                                                                                                                       

test/test_convert2sentence.py ....                                                                                                                 [ 40%]
test/test_num2words.py ......                                                                                                                      [100%]

=============================================================== 10 passed in 0.04 seconds ================================================================
```

