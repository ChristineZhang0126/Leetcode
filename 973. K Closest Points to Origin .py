# 973. K Closest Points to Origin
# Medium
# 8.1K
# 289
# Companies
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

# Constraints:

# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104

# import heapq
# from math import sqrt

# class Solution(object):
#     def kClosest(self, points, k):
#         """
#         :type points: List[List[int]]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         # use min heap
#         return_list = []
#         the_list = {}

#         for i in range(len(points)):
#             # Correct the usage of sqrt
#             the_list[i] = sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1])

#         the_value = list(the_list.values())
#         heapq.heapify(the_value)

#         while k != 0:
#             # Pop the smallest element directly from the min heap
#             a_val = heapq.heappop(the_value)
#             for item, values in the_list.items():
#                 if values == a_val:
#                     return_list.append(points[item])
#                     k -= 1

#         return return_list
import heapq
from math import sqrt

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Use min heap directly
        min_heap = []

        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(min_heap, (distance, point))

        return_list = [heapq.heappop(min_heap)[1] for _ in range(k)]

        return return_list