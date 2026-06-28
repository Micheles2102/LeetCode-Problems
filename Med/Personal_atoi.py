"""
Approach
Current:
Simulation / String
Suggested:
Simulation / String
Key Idea:
String parsing with state management to handle whitespace, signs, 
digits, and integer overflow constraints.
Current complexity:
O(N)
Suggested complexity:
O(N)

"""


class Solution:
    def myAtoi(self, s: str) -> int:
        # Ignore any leading whitespace [for less space complexity we can iterate via index instead creating a new string]
        t = s.lstrip()
        if t == "" or t[0].isalpha():
            return 0
        value = 0
        savenegative = False
        start = 0
        if t[0] == '-':
            savenegative = True
            start = 1
        if t[0] == '+':
            start = 1
        for x in t[start:]:
            if ord('0') <= ord(x) <= ord('9'):
                # ord() restituisci l'ascci del valore  e sottraendo il valore ascii di 0 riesco ad ottenere il valore numerico
                x = ord(x) - ord('0')
                value = value * 10 + (x)
            else:
                break
        if savenegative:
            value *= -1
        if value < -2**31:
            return -2**31
        if value > (2**31)-1:
            return (2**31)-1
        return value
