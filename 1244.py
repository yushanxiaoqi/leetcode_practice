string= "ABC123"
res=0
l =0
r =len(string)-1
while l < r:
    temp = string[i:j]
    for c in temp:
        if c not in dict1:
            dict1[c] =1
        else:
            dict1[c] +=1
    res =max(res,j-i)
print(res)