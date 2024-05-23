## Finding permutations of a list using backtracking algorithm
def permute(nums):
    def backtrack(start):
        if start == len(nums):
            res.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    res = []
    backtrack(0)
    return res
    
def subsets(start, nums, path, validset):
    validset.append(path)
    for i in range(start, len(nums)):
        subsets(i + 1, nums, path + [nums[i]], validset)
    return validset

def main():
    nums = [1, 2, 3]
    # print(permute(nums))
    validset = []
    validset = subsets(0, nums, [], validset)
    print(validset)

if __name__ == '__main__':
    main()