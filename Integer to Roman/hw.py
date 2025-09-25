class RomanConverter:
    def int_to_roman(self, num: int) -> str:
        """
        Converts an integer to its Roman numeral equivalent.
        """
        if not 0 < num < 4000:
            return "Number out of range (1-3999)"

        roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        roman_numeral = ""
        for value, symbol in roman_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

if __name__ == "__main__":
    converter = RomanConverter()
    try:
        user_input = int(input("Enter an integer to convert to Roman numeral: "))
        roman_result = converter.int_to_roman(user_input)
        print(f"The Roman numeral equivalent is: {roman_result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

