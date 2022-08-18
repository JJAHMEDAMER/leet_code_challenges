'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 
-------------------------------------------------

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
 -------------------------------------------------

Constraints:

-231 <= x <= 231 - 1
'''


def isPalindrome(x: int) -> bool:
    num = str(x)
    if len(num)/2 == 0:
        return False
    else:
        for i in range(len(num)//2):
            if num[i] != num[-i-1]:
                return False
        return True

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(0))
print(isPalindrome(1000021))