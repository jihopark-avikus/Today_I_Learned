"""
Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        assert len(strs) >= 1 and len(strs) <= 200, "not complying with constraints."
        for elem in strs:
            assert len(elem) >= 0 and len(elem) <= 200, "not complying with constraints."
            assert elem.islower(), "not complying with constraints."
        
        common_char = ""
        base_elem = strs[0]
        
        while True:
            x = base_elem[:len(common_char)+1]

            for idx in range(1, len(strs)):
                next_elem = strs[idx]
                y = next_elem[:len(common_char)+1]

                if x == y and idx == len(strs)-1:
                    common_char += base_elem[len(common_char)]
                elif idx < len(strs)-1:
                    continue

            if len(common_char) == len(x)-1:
                break

        return common_char

if __name__ == "__main__":
    solver = Solution()
    
    input_1 = ["flower", "flow", "flight"]
    ans_1 = solver.longestCommonPrefix(input_1)
    assert ans_1 == "fl", "not expect output"

    input_2 = ["dog", "racecar", "car"]
    ans_2 = solver.longestCommonPrefix(input_2)
    assert ans_2 == "", "not expect output"
   