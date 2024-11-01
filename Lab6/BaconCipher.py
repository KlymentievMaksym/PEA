dict_of_alphabet = {  # a b c d e f g h i j k l m n o p q r s t u v w x y z
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z'
}

l = int(input())
string = input()
word = ''
for i in range(0, l-5+1, 5):
    num = [0] * 5
    five_chars = string[i:i+5]
    for char_index in range(5):
        if five_chars[char_index].isdigit():
            num[char_index] = 1
        else:
            num[char_index] = 0
    num = int(''.join(map(str, num)), 2)
    word += dict_of_alphabet[num]
print(word)
