
def compare(a,b):
    c1 = [0]*26
    c2 = [0]*26
        
    for i in range(len(a)):
        pos = ord(a[i])-ord('a')
        c1[pos] += 1
    for i in range(len(b)):
        pos = ord(b[i])-ord('a')
        c2[pos] += 1
        
    j = 0
    flag = True
    while j < 26 and flag:
        if (c1[j] == c2[j]):
            j += 1
        else:
            flag = False
    return flag
        
        

y = compare('apple','pleaa')
print(y)
                
