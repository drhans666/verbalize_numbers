from django.test import TestCase

from .views import int_to_str


class MainTest(TestCase):

    def test_digits(self):
        verbalized = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem',
                      'osiem', 'dziewięć']
        data = enumerate(verbalized)
        for number, verbal in data:
            result = int_to_str(number)
            self.assertEqual(result, verbal)

    def test_dozen(self):
        verbalized = ['dziesięć', 'jedenaście', 'dwanaście', 'trzynaście',
                      'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście',
                      'osiemnaście', 'dziewiętnaście']
        numbers = range(10, 19)
        data = zip(numbers, verbalized)
        for number, verbal in data:
            result = int_to_str(number)
            self.assertEqual(result, verbal)

    def test_until_hundred(self):

        verbalized = ['dwadzieścia', 'trzydzieści jeden', 'czterdzieści dwa', 'pięćdziesiąt trzy',
                      'sześćdziesiąt cztery', 'pięćdziesiąt pięć', 'sześćdziesiąt sześć',
                      'siedemdziesiąt siedem', 'osiemdziesiąt osiem', 'dziewięćdziesiąt dziewięć']
        numbers = [20, 31, 42, 53, 64, 55, 66, 77, 88, 99]
        data = zip(numbers, verbalized)
        for number, verbal in data:
            result = int_to_str(number)
            self.assertEqual(result, verbal)

    def test_until_thousand(self):

        verbalized = ['sto', 'sto dwanaście', 'dwieście czterdzieści sześć',
                      'trzysta sześćdziesiąt cztery', 'czterysta pięćdziesiąt osiem',
                      'pięćset trzy', 'sześćset sześćdziesiąt sześć', 'siedemset dwadzieścia jeden',
                      'osiemset dziewięćdziesiąt', 'dziewięćset dziewięćdziesiąt dziewięć']
        numbers = [100, 112, 246, 364, 458, 503, 666, 721, 890, 999]
        data = zip(numbers, verbalized)
        for number, verbal in data:
            result = int_to_str(number)
            self.assertEqual(result, verbal)

    def test_thousands(self):
        verbalized = ['tysiąc sto dwadzieścia jeden', 'cztery tysiące trzysta trzydzieści',
                      'jedenaście tysięcy czterdzieści dziewięć',
                      'sto trzydzieści tysięcy osiemset dziewięćdziesiąt pięć']
        numbers = [1121, 4330, 11049, 130895]
        data = zip(numbers, verbalized)
        for number, verbal in data:
            result = int_to_str(number)
            self.assertEqual(result, verbal)

    def test_millions(self):
        verbalized = ['milion tysiąc dwieście dwadzieścia dziewięć',
                      'cztery miliony trzysta tysięcy sto trzydzieści',
                      'sto milionów osiemset tysięcy dwieście osiemdziesiąt trzy']

        numbers = [1001229, 4300130, 100800283]
        data = zip(numbers, verbalized)
        for number, verbal in data:
            result = int_to_str(number)
            self.assertEqual(result, verbal)

    # milliard is polish version of english billion
    def test_milliard(self):
        verbalized = ['miliard dwieście dwadzieścia milionów trzysta tysięcy',
                      'trzy miliardy osiemset trzydzieści milionów pięćdziesiąt',
                      'dziesięć miliardów trzysta tysięcy dwieście pięćdziesiąt sześć']

        numbers = [1220300000, 3830000050, 10000300256]
        data = zip(numbers, verbalized)
        for number, verbal in data:
            result = int_to_str(number)
            self.assertEqual(result, verbal)

    # billion is polish version of english trillion
    def test_billions(self):
        verbalized = ['bilion dwa miliardy trzysta dwadzieścia milionów trzysta tysięcy pięćset',
                      'cztery biliony trzy miliardy osiemset trzydzieści milionów pięćdziesiąt',
                      'dwanaście bilionów dziesięć miliardów trzysta tysięcy dwieście pięćdziesiąt sześć']

        numbers = [1002320300500, 4003830000050, 12010000300256]
        data = zip(numbers, verbalized)
        for number, verbal in data:
            result = int_to_str(number)
            self.assertEqual(result, verbal)

    def test_big_round(self):
        verbalized = ['milion', 'sto milionów', 'dziesięć miliardów', 'sto bilionów']
        numbers = [1000000, 100000000, 10000000000, 100000000000000]
        data = zip(numbers, verbalized)
        for number, verbal in data:
            result = int_to_str(number)
            self.assertEqual(result, verbal)

    def test_negative(self):
        verbalized = ['minus dziesięć', 'minus sto pięćdziesiąt sześć', 'minus siedem tysięcy']
        numbers = [-10, -156, -7000]
        data = zip(numbers, verbalized)
        for number, verbal in data:
            result = int_to_str(number)
            self.assertEqual(result, verbal)
