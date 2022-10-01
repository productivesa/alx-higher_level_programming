#!/usr/bin/python3
def roman_to_int(roman_string):
    if type_if_roman(roman_string) == str:
        roman_number = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
                        }
        sum = 0
        chk = 0

        for x in range(len(roman_string)):
            if chk:
                chk = 0
                continue
            for key in roman_number:
                if roman_string[x] == key and x != len(roman_string) - 1:
                    if roman_string[x] == 'I' and roman_string[x + 1] == 'V':
                        sum += 4
                        chk = 1
                    elif roman_string[x] == 'I' and roman_string[x + 1] == 'X':
                        sum += 9
                        chk = 1
                    elif roman_string[x] == 'X' and roman_string[x + 1] == 'L':
                        sum += 40
                        chk = 1
                    elif roman_string[x] == 'X' and roman_string[x + 1] == 'C':
                        sum += 90
                        chk = 1
                    elif roman_string[x] == 'C' and roman_string[x + 1] == 'D':
                        sum += 400
                        chk = 1
                    elif roman_string[x] == 'C' and roman_string[x + 1] == 'M':
                        sum += 900
                        chk = 1
                    else:
                        sum += roman_number[key]
                elif roman_string[x] == key:
                    sum += roman_number[key]
        return sum
    return 0
