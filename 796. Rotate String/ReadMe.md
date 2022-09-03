# Problem 796. 
### Rotate String


[Link On LeetCode]()

## Problem
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

#### Example 1:
```python
Input: s = "abcde", goal = "cdeab"
Output: true
```
#### Example 2:
```python
Input: s = "abcde", goal = "abced"
Output: false
```

#### Constraints:
```
- 1 <= s.length, goal.length <= 100
- s and goal consist of lowercase English letters.
```

---
## Solution

### First Solution
Loop over the string 
```python
for i in range(0,len(s)):
    if s == goal:
        return True
    else:
        s = s[1:] + s[0]
return False
```

### Second Solution
The ans will exist iin the concatenated string
__NOTE__ the size of the inputs are not the same so we should check for len
```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in s + s and len(s) == len(goal)

# s = "abcde" , goal = "cdeab"
# s+s = abcdeabcde
# goal in s+s = ab[cdeab]cde
```


