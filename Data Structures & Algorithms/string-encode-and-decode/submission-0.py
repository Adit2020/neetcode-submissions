class Solution:

    def encode(self, strs: List[str]) -> str:
            
        encoded = ""
        
        for s in strs:
            encoded += str(len(s)) + "#" + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
            
        res = []
        i = 0

        while i < len(s):
            # Find the '#'
            j = i
            while s[j] != '#':
                j += 1

            # Get the length
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract the string
            word = s[j:j + length]
            res.append(word)

            # Move pointer forward
            i = j + length

        return res
