left sorted and right sorted arrays
```
#example
[0,1,2,4,5,6,7] # sorted unrotated
[4,5,6,7,0,1,2] # sorted rotated with index 3
# left sorted array [4,5,6,7] right sorted array [0,1,2]

[1,2,4,5,6,7,0]
```

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

```