import math


def first_three(three):
    """
    Gets trio like 345 or 674, processes, cleans and returns verbalized form
    :param three: int
    :return: str
    """
    ones = ['', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem',
            'osiem', 'dziewięć']
    tens = ['dziesięć', 'jedenaście', 'dwanaście', 'trzynaście',
            'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście',
            'osiemnaście', 'dziewiętnaście']
    enties = ['', '', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt',
              'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt']
    hundreds = ['', 'sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset',
                'siedemset', 'osiemset', 'dziewięćset']

    # assigns index nr to verbalized form in list
    on = int(three % 10)
    ent = int(three / 10 % 10)
    hun = int(three / 100 % 10)

    # appends result list with verbal. forms.
    result = []
    result.append(hundreds[hun])
    if int(ent) == 1:
        result.append(tens[on])
    else:
        result.append(enties[ent])
        result.append(ones[on])
    # cleans result list from empty strings
    while '' in result:
        result.remove('')
    return ' '.join(result)


def stack_threes(number):
    """
    Function takes a number and return's it as a list of three-char strings
    :param number: integer 
    :return: list
    """
    # ensures number is natural and turns it into string
    str_number = str(abs(number))
    # check how many trio's in number
    threes_number = int(math.ceil(len(str_number) / 3))
    threes_list = []
    # loop divides integers into trio's and passes them to list
    for i in range(threes_number):
        threes_list.append(str_number[-3:])
        str_number = str_number[:-3]
    return threes_list


def big_validator(trio_num, trio_content):
    """
    Validates and assigns in right form values like million, thousand etc.
    :param trio_num: int
    :param trio_content: int 
    :return: string
    """
    
    thousands = ['tysiąc', 'tysiące', 'tysięcy', '']
    millions = ['milion', 'miliony', 'milionów', '']
    milliards = ['miliard', 'miliardy', 'miliardów', '']
    billions = ['bilion', 'biliony', 'bilionów', '']
    big_numbers = [thousands, millions, milliards, billions]
    ones = int(trio_content % 10)
    tens = int(trio_content / 10 % 10)

    # takes care of edge case. Prevents putting 'big_numbers' f.e. 'tysiąc' in 1000000
    if trio_content == 000:
        grammar_form = 3
    # assigns correct grammar form
    elif trio_content == 1:
        grammar_form = 0
    elif tens == 1 and ones > 1:
        grammar_form = 2
    elif 2 <= ones <= 4:
        grammar_form = 1
    else:
        grammar_form = 2

    return big_numbers[trio_num][grammar_form]


def verbalize_number(three_list):
    """
    Function takes list with 3-char strings representing base number
    It returns string with verbalized number without positive/negative 
    :param three_list: list 
    :return: str
    """
    # is used as a trio counter. f.e. 1 trio is 0-999, 2 thousands, 3 millions etc.
    trio_nr = -1
    verbalized = []

    for trio_content in three_list:
        if trio_nr >= 0:
            verbalized.append(big_validator(trio_nr, int(trio_content)))
        # takes care of edge case
        try:
            if verbalized[-1] not in ['tysiąc', 'milion', 'miliard', 'bilion']:
                verbalized.append(first_three(int(trio_content)))
        except IndexError:
            verbalized.append(first_three(int(trio_content)))
        trio_nr += 1
    # makes mirror reflection of list
    verbalized = verbalized[::-1]
    # cleans of empty strings
    while '' in verbalized:
        verbalized.remove('')
    return (' '.join(verbalized)).strip()


def check_minus(number, verbalized):
    """
    Checks if base number is negative. If yes adds 'minus' phrase.
    :param number: 
    :param verbalized: 
    :return: 
    """
    if number < 0:
        verbalized = 'minus ' + verbalized
    return verbalized
