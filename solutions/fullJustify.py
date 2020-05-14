class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not len(words):
            return []
        
        res = []
        curr_line = []
        curr_line_char_count = 0
        for word in words:
            curr_min_num_spaces = len(curr_line) - 1
            would_exceed_line = curr_line_char_count + curr_min_num_spaces + len(word) + 1 > maxWidth
            
            if would_exceed_line:
                self.add_spaced_line(curr_line, curr_line_char_count, maxWidth, res)
                curr_line_char_count = 0
                curr_line = []
            
            curr_line.append(word)
            curr_line_char_count += len(word)
        
        last_line = ' '.join(curr_line)
        last_line = last_line+(' '*(maxWidth - len(last_line)))
        res.append(last_line)
        
        return res
        
        
    def add_spaced_line(self, curr_line, curr_line_char_count, maxWidth, res):
        curr_min_num_spaces = len(curr_line) - 1
        num_spaces = maxWidth - curr_line_char_count
        if curr_min_num_spaces > 0:
            floor_num_spaces = num_spaces // curr_min_num_spaces
            num_with_extra = num_spaces % curr_min_num_spaces
            spaced_line = []
            for i, w in enumerate(curr_line):
                spaced_line.append(w)
                if i != len(curr_line) - 1:
                    space_count = floor_num_spaces+1 if num_with_extra else floor_num_spaces
                    num_with_extra = max(0, num_with_extra - 1)
                    spaced_line.append(' '*space_count)
            res.append(''.join(spaced_line))
        else:
            curr_line.append(' '*num_spaces)
            res.append(''.join(curr_line))
        
