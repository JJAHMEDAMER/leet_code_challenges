# Problem 1108. 
### Defanging an IP Address

[Link On LeetCode](https://leetcode.com/problems/defanging-an-ip-address/)

## Problem
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

#### Example 1:
```python
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
```
#### Example 2:
```python
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 ```

#### Constraints:

The given address is a valid IPv4 address.

---
## Solution

### First Solution
initialize an empty sting and loop over the input string
```python
ans = ""
for i in address:
    if i == ".":
        ans += ("[.]")
    else:
        ans += (i)
return ans
```

### Second Solution
Use the replace method
```python
return address.replace(".","[.]")
```
Runtime: 34 ms, faster than 86.28% of Python3 online submissions
Memory Usage: 13.8 MB, less than 49.47% of Python3 online submissions

### Third Solution 
Use split and join methods
split takes a string and returns a list 
join takes a list and return a string
```python
# return "[.]".join(address.split("."))  # One line solution

LIST = address.split(address)  # address = 1.1.1.1
ans = "[.]".join(LIST)  # LIST = ["1", "1", "1", "1"]
return ans  # ans = "1[.]1[.]1[.]1"
```
Runtime: 59 ms, faster than 15.19% of Python3 online submission
Memory Usage: 13.8 MB, less than 94.67% of Python3 online submissions





