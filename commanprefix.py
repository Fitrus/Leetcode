    
def commanprefix():
    strs = ["flower","flow","flight"]


    for k, v in enumerate(strs[0]):
        
        for s in strs[1:]:
            if k >= len(s) or v != s[k]:
                return(strs[:k])

commanprefix()