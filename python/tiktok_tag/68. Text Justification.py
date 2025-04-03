class Solution:     #time:O(n)     #space:O(n)
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        #line to record the processing line, and the length
        line, length = [], 0
        i = 0
        
        #when we need to switch the line
        while i < len(words):
            # Check if adding this word would exceed maxWidth
            if length + len(line) + len(words[i]) > maxWidth:
                #calculate the extra space
                extra_space = maxWidth - length
                
                # Handle case with single word differently
                if len(line) == 1:
                    res.append(line[0] + " " * extra_space)
                else:
                    spaces = extra_space // (len(line) - 1)
                    remainder = extra_space % (len(line) - 1)
                    
                    # Create a new line with spaces properly distributed
                    new_line = ""
                    for j in range(len(line) - 1):
                        new_line += line[j]
                        new_line += " " * spaces
                        if j < remainder:
                            new_line += " "
                    
                    # Add the last word
                    new_line += line[-1]
                    res.append(new_line)
                
                # Reset line and length for next line
                line, length = [], 0
            else:
                # Add word to current line
                line.append(words[i])
                length += len(words[i])
                i += 1
        
        # Handle the last line - left justified with single spaces
        if line:
            last_line = " ".join(line)
            trail_space = maxWidth - len(last_line)
            res.append(last_line + " " * trail_space)
        
        return res