class Solution:

    def encode(self, strs: List[str]) -> str:
         sep = 'é'
         encoding_str = ""
         for i in strs:
            encoding_str += i+sep
         return encoding_str

    def decode(self, s:str) -> List[str]:
        sep = 'é'
        strs = s.split(sep)    
    
        return strs[:-1]

