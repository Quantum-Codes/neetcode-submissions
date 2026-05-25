class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length = len(string)
            string = string + "X" * (200-length) # pad string on end to make it 200 length
            encoded += f"#{string}{length}#"
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        if s == "":
            return []
        # every unit is a # + 200 len string padded + int of some size thats len of string + #
        # we will have a phase for extraction of each
        i = 0
        while i < len(s):
            current_str = ""
            length = ""
            # hashtag removal
            i += 1 # just skip it

            # read 200 chars
            current_str = s[i:i+200] # this is the padded str
            i += 200 # skip over string 
            
            # read the length
            while s[i] != "#":
                length += s[i]
                i += 1
            
            # now s[i] == "#". 
            i += 1 # ignore this hash. 

            # save extracted data
            current_str = current_str[:int(length)] # remove padding
            decoded.append(current_str)
        
        return decoded
