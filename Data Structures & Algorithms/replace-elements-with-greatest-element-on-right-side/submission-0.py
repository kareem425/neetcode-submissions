class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightM = -1

        for i in range(len(arr)-1,-1,-1):
            newM = max(rightM,arr[i])
            arr[i] = rightM
            rightM = newM
        return arr