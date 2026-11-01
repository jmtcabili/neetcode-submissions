class Solution:

    #caesar's cipher
        #offset ascii value of char per string in the array
    OFFSET = 14
    def encode(self, strs: List[str]) -> str:
       
        encoded = []
        for word in strs:
            encoded.append(str(len(word)) + "$" + word)
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0 
        decoded=[]
        word_length = []
        while (i < len(s)):
            #loop until not #
            if (s[i] != "$"):
                word_length.append(s[i])
            else: 
                length = int("".join(word_length))
                word = s[i+1 : i+length+1]
                decoded.append(word)
                i +=length+1
                word_length = []
                continue

            #end of loop
            i+=1


        return decoded
