class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        j = 0
        len_name = len(name)
        len_typed = len(typed)
        
        while i < len_name and j < len_typed:
            if name[i] != typed[j]:
                return False

            name_successive = 1
            while (i+name_successive < len_name) and (name[i] == name[i+name_successive]):
                name_successive += 1
            
            typed_successive = 1
            while (j+typed_successive < len_typed) and (typed[j] == typed[j+typed_successive]):
                typed_successive += 1

            if typed_successive < name_successive:
                return False
            
            i += name_successive
            j += typed_successive
        return i == len_name and j == len_typed
