class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort(left_half)
                merge_sort(right_half)

                i = j = k = 0

        # Merge the two sorted halves
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

        # Add any remaining elements from left_half
                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

        # Add any remaining elements from right_half
                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1
            
        answer = nums1 + nums2
        merge_sort(answer)
        if len(answer) % 2 == 0:
            print(answer[int(len(answer) / 2) - 1])
            print(answer[int((len(answer))/2)])
            return (answer[int(len(answer) / 2) - 1] + answer[int((len(answer))/2)])/2
        return answer[int(len(answer)/2)]


