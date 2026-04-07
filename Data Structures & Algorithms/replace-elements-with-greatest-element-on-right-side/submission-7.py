class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        if length == 1:
            return [-1]
        answer = arr.copy()
        i = length - 1
        answer[i] = -1
        while (i > 0):
            i -= 1
            answer[i] = max(answer[i+1], arr[i+1])
        return answer



