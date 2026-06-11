class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        # first decide where the row is
        row = -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] > target: # go to prev row
                bottom = mid - 1
            elif matrix[mid][len(matrix[0]) - 1] < target: # go to next row
                top = mid + 1
            else:
                row = mid
                break # we are on the right row which is in mid
        
        print(f"{row=}")
        # now binary search on that row
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
