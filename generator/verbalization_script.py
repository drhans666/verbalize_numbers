import math
number = 1002320300500


def first_three(three):
    ones = ['', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem',
            'osiem', 'dziewięć']
    tens = ['dziesięć', 'jedenaście', 'dwanaście', 'trzynaście',
            'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście',
            'osiemnaście', 'dziewiętnaście']
    enties = ['', '', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt',
              'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt']
    hundreds = ['', 'sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset',
                'siedemset', 'osiemset', 'dziewięćset']

    on = int(three % 10)
    ent = int(three / 10 % 10)
    hun = int(three / 100 % 10)
    result = []
    result.append(hundreds[hun])
    if int(ent) == 1:
        result.append(tens[on])
    else:
        result.append(enties[ent])
        result.append(ones[on])
    if '' in result:
        result.remove('')
    return ' '.join(result)


def stack_threes(number):
    str_number = str(abs(number))
    threes_number = int(math.ceil(len(str_number) / 3))
    threes_list = []

    for i in range(threes_number):
        threes_list.append(str_number[-3:])
        str_number = str_number.replace(str_number[-3:], '')
    return threes_list


def big_validator(count, three_num):
    thousands = ['tysiąc', 'tysiące', 'tysięcy']
    millions = ['milion', 'miliony', 'milionów']
    milliards = ['miliard', 'miliardy', 'miliardów']
    billions = ['bilion', 'biliony', 'bilionów']
    big_numbers = [thousands, millions, milliards, billions]
    ones = int(three_num % 10)
    tens = int(three_num / 10 % 10)

    if three_num == 1:
        grammar_form = 0
    elif tens == 1 and ones > 1:
        grammar_form = 2
    elif 2 <= ones <= 4:
        grammar_form = 1
    else:
        grammar_form = 2

    return big_numbers[count][grammar_form]


def verbalize_number(three_list):
    count = 0
    verbalized = []
    for three_num in three_list:
        if count != 0:
            verbalized.append(big_validator(count, int(three_num)))
        verbalized.append(first_three(int(three_num)))
        count += 1
    verbalized = verbalized[::-1]
    return (' '.join(verbalized)).strip()


def check_minus(number, verbalized):
    if number < 0:
        verbalized = 'minus ' + verbalized
    return verbalized


three_list = stack_threes(number)
verbalized = verbalize_number(three_list)
print(check_minus(number, verbalized))

