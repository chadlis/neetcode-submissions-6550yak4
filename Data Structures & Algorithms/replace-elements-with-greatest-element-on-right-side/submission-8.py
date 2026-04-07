class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        if length == 1:
            return [-1]
        answer = arr.copy()
        right_max = -1
        for i in range(length-1, -1, -1):
            answer[i] = right_max
            right_max = max(right_max, arr[i])
        return answer