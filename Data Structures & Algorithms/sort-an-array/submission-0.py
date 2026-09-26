class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr1, arr2):

            res = []
            i = j = 0

            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            
            while i < len(arr1):
                res.append(arr1[i])
                i += 1

            while j < len(arr2):
                res.append(arr2[j])
                j += 1

            return res
        

        def mergeSort(arr, start, stop):

            if start == stop:
                return [arr[start]]
            
            mid = (start + stop ) // 2

            left = mergeSort(arr, start, mid)
            right = mergeSort(arr, mid+1, stop)

            return merge(left, right)


        return mergeSort(nums, 0, len(nums)-1)

        


  



    
        