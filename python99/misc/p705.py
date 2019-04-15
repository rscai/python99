def full_word(n):
    nToWords = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero'
    }
    words = [nToWords[num] for num in str(n)]
    return '-'.join(words)
