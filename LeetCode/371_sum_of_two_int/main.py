class Solution:
    def getSum(self, a: int, b: int) -> int:
        pass

    def halfAdder(a: int, b: int):
        if a == 0 and b == 0:
            return (0,0)
        elif a == 1 and b == 1:
            return (0,1)
        else:
            return (1,0)

    def fullAdder(self, a: int, b: int, carry: int):
        firstSum, carry = self.halfAdder(a, b)
        sum, lastCarry = self.halfAdder(carry, firstSum)

        return (sum, carry or lastCarry)
        