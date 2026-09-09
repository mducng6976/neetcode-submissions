class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        arrange = sorted(count, key=count.get, reverse=True)
        result = []
        count = 0
        for n in arrange:
            if count == k:
                return result
            else:
                result.append(n)
                count += 1
        return result