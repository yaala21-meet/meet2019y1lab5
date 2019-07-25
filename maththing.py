# getting the nums
nums = input("?")

# finding the second degree
degs = nums.find("n^2")
Bdegs = nums[:degs]
print("before: " + Bdegs + " place:" + str(degs))

# finding the first degree
nums = nums[degs+3:]
print(nums)
