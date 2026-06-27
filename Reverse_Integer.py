"""
Note: 
The returned integer must be within the 32-bit signed integer range: [−2^31,  2^31 − 1].
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Complessity Analysis:
Time complexity : O(d) / O(log(x)). There are roughly log10(x) digits in x. d = number of digits in x.
Space complexity : O(1). We only need constant space to store the final result.
"""


class Solution:
    def reverse(self, x: int) -> int:
        risultato = 0
        negativo = False
        if x < 0:
            x *= -1
            negativo = True

        while x > 0:
            valore = x % 10
            risultato = (risultato * 10) + valore
            x = x//10
        if negativo:
            risultato *= -1
        if not (-2**(31) <= abs(risultato) <= (2**(31)) - 1):
            return 0
        return risultato
