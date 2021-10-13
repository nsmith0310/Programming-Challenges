class NumArray:

    def __init__(self, nums: List[int]):
        self.n = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.n[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
