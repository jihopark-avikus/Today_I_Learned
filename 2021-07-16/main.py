
class Representer:
    def __init__(self, base: str) -> None:
        self.base = base

    def convert(self, num: str) -> int:

        if self.base == 'binary_to_decimal':
            decimal = 0
            
            for idx, val in enumerate(num[::-1]):
                decimal += (pow(2, idx) * int(val))
            
            return decimal

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num", type=str, help="binary number(str) to be converted into decimal", default=None)

    arg = parser.parse_args()

    tester = Representer(base='binary_to_decimal')

    case1 = '0101' 
    case2 = '1111'

    assert tester.convert(case1) == 5, 'not correct'
    assert tester.convert(case2) == 15, 'not correct'

    if arg.num is not None:
        print(f"{arg.num} is converted to {tester.convert(arg.num)}")
    