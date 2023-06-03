class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(int)
        return bits.count("1")