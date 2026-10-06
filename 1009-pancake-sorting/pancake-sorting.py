class Solution:
    def pancakeSort(self, arr):
        ans = []

        for size in range(len(arr), 1, -1):

            # Find the index of the largest element
            max_index = arr.index(size)

            # Bring the largest element to the front
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
                ans.append(max_index + 1)

            # Move the largest element to its correct position
            arr[:size] = arr[:size][::-1]
            ans.append(size)

        return ans