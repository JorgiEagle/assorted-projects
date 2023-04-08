"""
Problem: A string consists of only ( and ) characters
A string is balanced iff
    It is empty
    It has the form (S) where S is also balanced
    it has the form S1 S2 where both are balanced
    
Given L ( characters and R 0 characters
"""

for test in range(int(input())):
    complete = min(map(int, input().split()))
    # The number of complete bracket pairs (), is the minimum of these two values
    # The maximal number is the triangle number of the number of pairs,
    # Or, (n(n+1))/2
    result = int((complete*(complete+1))/2)
    print(f"Case #{test+1}: {result}")