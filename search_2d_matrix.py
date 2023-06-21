class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # select an arbitrary m
        # check if number is less than or greater than list[m[0]] and list[m[-1]]
        # perform search inside m
        # if greater than [m[-1]] go right
        # if less than [m[0]] go left

        # binary search to find subarray
        # binary search to find element in subarray
        
        class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # select an arbitrary m
        # check if number is less than or greater than list[m[0]] and list[m[-1]]
        # perform search inside m
        # if greater than [m[-1]] go right
        # if less than [m[0]] go left

        # binary search to find subarray
        # binary search to find element in subarray
        
        l , r = 0, len(matrix)-1
        while (l<=r):
            # m = l + ((r-1) //2)
            m = (l+r)//2
            if (matrix[m][-1]< target):
                l = m + 1
            elif (matrix[m][0]> target):
                r = m - 1
            # spotted the problem
            else :
                break
        
        if not l<=r:
            return False
            # choose wisely betwen l and r
        anotherL, rir = 0, len(matrix[r])-1
        while (anotherL<=rir):
            # mid = anotherL + ((rir-1)//2)
            mid = (anotherL+rir)//2
            if (matrix[m][mid]>target):
                rir = mid -1
            elif (matrix[m][mid]<target):
                anotherL = mid + 1
            else :
                return True
        return False
    
    #why did this not work?

        # l , r = 0, len(matrix)-1
        # while (l<=r):
        #     m = l + ((r-1) //2)
        #     if (matrix[m][-1]> target):
        #         r = m -1
        #     elif (matrix[m][0]< target):
        #         l = m + 1
        #     # spotted the problem
        #     else :
        #         break
        #     # choose wisely betwen l and r
        # anotherL, rir = 0, len(matrix[r])-1
        # while (anotherL<=rir):
        #     mid = anotherL + ((rir-1)//2)
        #     if (matrix[r][mid]>target):
        #         rir = mid -1
        #     elif (matrix[r][mid]<target):
        #         anotherL = mid + 1
        #     else :
        #         return True
        # return False
    


