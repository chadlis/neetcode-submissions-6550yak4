class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        if length == 1:
            return [-1]
        i = length - 1
        previous = arr[i]
        arr[i] = -1
        while (i > 0):
            i -= 1
            current = arr[i]
            arr[i] = max(previous, arr[i+1])
            previous = current
        return arr



