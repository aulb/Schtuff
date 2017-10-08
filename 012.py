class Solution(object):
    def __init__(self):
        self.rules = {
        	1: 'I',
        	2: 'II',
        	3: 'III',
        	4: 'IV',
        	5: 'V',
        	6: 'VI',
        	7: 'VII',
        	8: 'VIII',
        	9: 'IX',
        	10: 'X',
        	20: 'XX',
        	30: 'XXX',
        	40: 'XL',
        	50: 'L',
        	60: 'LX',
        	70: 'LXX',
        	80: 'LXXX',
        	90: 'XC',
        	100: 'C',
        	200: 'CC',
        	300: 'CCC',
        	400: 'CD',
        	500: 'D',
        	600: 'DC',
        	700: 'DCC',
        	800: 'DCCC',
        	900: 'CM',
        	1000: 'M',
        	2000: 'MM',
        	3000: 'MMM'
        }
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num > 3999:
        	return None
    
        roman = []
        counter = 1
        while num is not 0:
        	x = (num % 10) * counter
        	num = num / 10
        	if x is not 0:
        		roman.append(self.rules[x])
        		last = x
    
        	counter = counter * 10
    
        return ''.join(roman[::-1])
