rules = {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
    'VI': 6,
    'VII': 7,
    'VIII': 8,
    'IX': 9,
    'X': 10,
    'XX': 20,
    'XXX': 30,
    'XL': 40,
    'L': 50,
    'LX': 60,
    'LXX': 70,
    'LXXX': 80,
    'XC': 90,
    'C': 100,
    'CC': 200,
    'CCC': 300,
    'CD': 400,
    'D': 500,
    'DC': 600,
    'DCC': 700,
    'DCCC': 800,
    'CM': 900,
    'M': 1000,
    'MM': 2000,
    'MMM': 3000
}

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman = []
    s = s[::-1]
    result = 0
    num = 0
    for ss in s:
        roman.append(ss)
        check = ''.join(roman[::-1])
        
        if check in rules:
            num = rules[check]
        else:
            # New number
            result = result + num
            roman = [roman[-1]]
    result = result + num
    return num


if __name__ == '__main__':
    s = 'DCXXI'
    roman = []
    s = s[::-1]
    result = 0
    num = 0
    for ss in s:
        roman.append(ss)
        check = ''.join(roman[::-1])
        
        if check in rules:
            num = rules[check]
        else:
            # New number
            result = result + num
            roman = [roman[-1]]
    result = result + num