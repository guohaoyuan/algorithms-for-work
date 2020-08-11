class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)
        L, R = 0, n - 1

        while L <= R:
            mid = (L + R) >> 1
            if L == R:
                if nums[L] == target:
                    return L
                else:
                    return -1
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < nums[R]:
                    # 右有序
                    if  nums[R]>=target>nums[mid]:
                        # 此搜索区间为[mid + 1, R]
                        L = mid + 1
                    else:
                        R = mid - 1
                elif nums[mid] > nums[R]:
                    # 左有序
                    if nums[L] <=target<nums[mid]:
                        # 搜取区间[L, mid - 1]
                        R = mid - 1
                    else:
                        L = mid + 1
        return -1