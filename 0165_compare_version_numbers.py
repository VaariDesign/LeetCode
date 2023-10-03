class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        list1 = version1.split('.')
        list2 = version2.split('.')
        max_length = max(len(list1), len(list2))
        
        i = 0
        while i < max_length:
            
            if i < len(list1):
                num1 = int(list1[i])
            else:
                num1 = 0
                
            if i < len(list2):
                num2 = int(list2[i])
            else:
                num2 = 0   
                
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            
            i += 1
        return 0
