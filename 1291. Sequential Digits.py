# 1291. Sequential Digits
# Description
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 

# Constraints:

# 10 <= low <= high <= 10^9
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        # str_low = str(low)
        # str_high = str(high)
        # return_list = []
        # new_high = int(str_low + '0') - 1
        # if new_high >= high:
        # # while int(new_high) < int(str_high):
        # #     if len(str_low) == len(str_high):
        #     if str_low[0] == str_high[0]:
        #         the_str = str_low
        #         while len(the_str) < len(str_low):
        #             the_str += str((int(the_str[len(the_str)-1]) + 1))
        #         if low <= int(the_str) <= high:
        #             return_list.append(int(the_str))
        #     else:
        #         the_str = str_low[0]
        #         while len(the_str) < len(str_low):
        #             the_str += str((int(the_str[len(the_str)-1]) + 1))
        #         if low <= int(the_str):
        #             return_list.append(int(the_str))
        #         leading_num = int(str_low[0]) + 1      
        #         while leading_num < int(str_high[0]):
        #             the_str = str(leading_num)
        #             while len(the_str) < len(str_low):
        #                 the_str += str((int(the_str[len(the_str)-1]) + 1))
        #             if the_str[len(the_str)-1] == 0:
        #                 break
        #             return_list.append(int(the_str))
        #             leading_num += 1

        #         the_str = str_high[0]
        #         while len(the_str) < len(str_high):
        #             the_str += str((int(the_str[len(the_str)-1]) + 1))
        #         if high >= int(the_str):
        #             return_list.append(int(the_str))
        # else:
        #     while new_high < high:
        #         str_high = str(new_high)
        #         if str_low[0] == str_high[0]:
        #             the_str = str_low
        #             while len(the_str) < len(str_low):
        #                 the_str += str((int(the_str[len(the_str)-1]) + 1))
        #             if low <= int(the_str) <= high:
        #                 return_list.append(int(the_str))
        #         else:
        #             the_str = str_low[0]
        #             while len(the_str) < len(str_low):
        #                 the_str += str((int(the_str[len(the_str)-1]) + 1))
        #             if low <= int(the_str):
        #                 return_list.append(int(the_str))
        #             leading_num = int(str_low[0]) + 1      
        #             while leading_num < int(str_high[0]):
        #                 the_str = str(leading_num)
        #                 while len(the_str) < len(str_low):
        #                     the_str += str((int(the_str[len(the_str)-1]) + 1))
        #                 if the_str[len(the_str)-1] == 0:
        #                     break
        #                 return_list.append(int(the_str))
        #                 leading_num += 1

        #             the_str = str_high[0]
        #             while len(the_str) < len(str_high):
        #                 the_str += str((int(the_str[len(the_str)-1]) + 1))
        #             if high >= int(the_str):
        #                 return_list.append(int(the_str))
        str_low = str(low)
        str_high = str(high)
        return_list = []
        for each in range(len(str_low), len(str_high)+1):
            for all_num in range(1,11 - each):
                the_str = str(all_num)
                for nums in range(each-1):
                    the_str += str(int(the_str[len(the_str)-1]) + 1)
                
                if low <= int(the_str) <= high:
                    return_list.append(int(the_str))
        return return_list