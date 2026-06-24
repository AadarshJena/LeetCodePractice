class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #hello!

        output = []
        #temp_list = []
        product = 1
        length = len(nums)
        index = 0
        second_index = 1

        while index < length:
            
            for i in range(length):
                if i != index:
                    product = product * nums[i]
            output.append(product)
            index += 1
            product = 1
        return output

gang = Solution()
print(gang.productExceptSelf())
