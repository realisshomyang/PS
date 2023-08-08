def subset_sum(nums, target):
    def backtrack(i, curr_sum):
        if curr_sum == target:
            return True
        if i == len(nums) or curr_sum > target:
            return False

        include = backtrack(i + 1, curr_sum + nums[i])
        exclude = backtrack(i + 1, curr_sum)

        return include or exclude

    return backtrack(0, 0)


# Example usage
nums = [2, 3, 7, 8]
target = 11

is_possible = subset_sum(nums, target)
print("Is it possible to achieve the target sum?", is_possible)
