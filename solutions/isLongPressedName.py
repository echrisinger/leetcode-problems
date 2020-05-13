class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_tuples = self._getTuples(name)
        typed_tuples = self._getTuples(typed)
        
        if len(name_tuples) != len(typed_tuples):
            return False
        
        for i in range(len(name_tuples)):
            name_c, name_count = name_tuples[i]
            typed_c, typed_count = typed_tuples[i]
            if name_c != typed_c or name_count > typed_count:
                return False
            
        return True

    def _getTuples(self, name):
        name_tuples = []
        curr_char, count = name[0], 0
        for c in name:
            if curr_char == c:
                count += 1
            else:
                name_tuples.append((curr_char, count))
                curr_char = c
                count = 1
                
        name_tuples.append((curr_char, count))
        return name_tuples
 
