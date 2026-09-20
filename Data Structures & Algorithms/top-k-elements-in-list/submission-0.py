class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        count_list = [[] for n in range(len(nums) + 1)]

        for n in nums:
            if n not in frequency_map:
                frequency_map[n] = 1
            else:
                frequency_map[n] += 1

        for n, c in frequency_map.items():
            count_list[c].append(n)
        
        res = []

        for i in range(len(count_list) - 1, 0, -1):
            for n in count_list[i]:
                if len(res) == k:
                    return res

                res.append(n)
        return res

