# Problem 1689
### Partitioning Into Minimum Number Of Deci-Binary Numbers

## Problem

A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.



#### Example 1:
```python
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32
```
#### Example 2:
```python
Input: n = "82734"
Output: 8
```
#### Example 3:
```python
Input: n = "27346209830709182346"
Output: 9
 ```

---

# Solution
### The solution is find the max number

The number of deci-binary numbers will always be equal to larges number. The largest number will give the most number of ones\
9 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1\
8 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1\
7 = 1 + 1 + 1 + 1 + 1 + 1 + 1

#### Example 1:
```python
32
11
11
10
```
#### Example 2:
```python
82734
11111
11111
10111
10101
10100
10100
10100
10000
```



