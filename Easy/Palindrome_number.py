# ==========================================
# APPROACH 1: Using String Conversion
# ==========================================
# Time Complexity: O(N) - where N is the number of digits in the integer.
# Space Complexity: O(N) - str(x) allocates a new string of length N in memory.
class SolutionString:
    def isPalindrome(self, x: int) -> bool:
        is_pal = False
        s = str(x)
        if s[0] == '-':
            return is_pal
        index = 0
        while index < len(s):
            if s[index] == s[len(s) - index - 1]:
                is_pal = True
            else:
                is_pal = False
                break
            index += 1
        return is_pal


# ==========================================
# APPROACH 2: Mathematical Approach (No Strings)
# ==========================================
# Time Complexity: O(log10(x)) equivalent to O(N) - the loop runs once for each digit.
# Space Complexity: O(1) - Constant space. No memory copies or type conversions are made.
# Note: Need to add a check for integer overflow in strictly typed languages (e.g., Java/C++).[U can use half of the number to avoid overflow: 1221 reverse the first half and compare with the second half]
class SolutionMath:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes (due to the '-' sign)
        if x < 0:
            return False

        reverse = 0
        temp = x
        while temp > 0:
            reverse = reverse * 10 + (temp % 10)
            temp //= 10

        return x == reverse
