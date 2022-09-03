# Problem 0000. 
### problem title

[Link On LeetCode]()

## Problem


#### Example 1:
```python
Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
```
#### Example 2:
```python
Input: operations = ["++X","++X","X++"]
Output: 3
Explanation: The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.
```
#### Example 3:
```python
Input: operations = ["X++","++X","--X","X--"]
Output: 0
Explanation: The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.
```

#### Constraints:
```
- 1 <= operations.length <= 100
- operations[i] will be either "++X", "X++", "--X", or "X--".
```

---
## Solution

### First Solution
Loop over each element\
__NOTE__ There are 3 comparisons that run every loop
1. "++X" == operation
2. "X++" == operation
3. or
```python
ans = 0
for operation in operations:
    if "++X" == operation or "X++" == operation:
        ans += 1
    else:
        ans -= 1
return ans
```
Runtime: 94 ms, faster than 32.03%\
Memory Usage: 13.8 MB, less than 96.03%

### Second Solution
Loop over each element\
__NOTE__ There will be ether one or two comparison in each loop
1. X++ -> two comp
2. ++X -> One comp 
```python
ans = 0
for operation in operations:
    if "+" in operation:
        ans += 1
    else:
        ans -= 1
return ans
```
Runtime: 74 ms, faster than 64.00%\
Memory Usage: 13.8 MB, less than 56.11%

### Third Solution 
Get length of the list and for each (-) subtract 2 not 1
1. subtract once for counting because we added 1 for each element
2. subtract once for "X--" = -1
```python
ans = len(operations)
for operation in operations:
    if "-" in operation:
        ans -= 2
return ans
```

### Fourth Solution 
count method
```python
return (operations.count("X++")+operations.count("++X") - 
            operations.count("X--") - operations.count("--X"))
```

### Fifth Solution 
Sum Function
```python
return sum(1 if '+' in operation else -1 for operation in operations)
```





