class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Data is sorted in each row and across each rows as well.
        # Data is sorted, so hint is binary search approach.
        # If we can think of this 2D array as 1D array (visualize), then binary search can be applied.

        # Formula for relation between 1D array index and 2D array index:
        # 1D[i]=2D[i//n][i%n]
        # for m*n matrix
        m=len(matrix)
        n=len(matrix[0])

        # l, r and mid are 1D array index
        l,r = 0, m*n-1
        while l<=r:
            mid=(l+r)//2
            # Check if target is smaller or larger compared to mid element using 1D to 2D arrray index correlation.
            if target<matrix[mid//n][mid%n]:
                r=mid-1
            elif target>matrix[mid//n][mid%n]:
                l=mid+1
            else:
                # Success: found target
                return True
        
        return False

# Time complexity: O(log(m*n))
# Space complexity: O(1)
# where m and n are numbers of rows and columns of matrix