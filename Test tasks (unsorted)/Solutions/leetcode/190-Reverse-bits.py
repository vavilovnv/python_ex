"""
https://leetcode.com/problems/reverse-bits/

Category - Easy

Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type.
In this case, both input and output will be given as a signed integer type.
They should not affect your implementation, as the integer's internal binary
representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement
notation. Therefore, in Example 2 above, the input represents the signed
integer -3 and the output represents the signed integer -1073741825.

"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # Iterate over all 32 bits of the given number
        for _ in range(32):
            # Left shift the reversed number by 1 and 
            # add the last bit of the given number to it
            res = (res << 1) | (n & 1)
            # To add the last bit of the given number to the reversed number,
            # perform an AND operation with the given number and 1
            n >>= 1
        return res
