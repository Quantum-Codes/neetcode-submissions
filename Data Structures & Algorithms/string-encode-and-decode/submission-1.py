class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += f"💀{string}💀"
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        if s == "":
            return []
        return s[1:len(s)-1].split("💀💀")
