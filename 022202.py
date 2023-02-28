#给出一个待挖掘问题内容字符串content和一个词的字符串word，找到content中
#所有word的新词


# content = input()
# word = input()
content = "qweebaewqd"
word = "qwe"
#方法一、暴力枚举，时间复杂度较高
def get_result(content,word):
    n = len(content)
    if n <= 1:
        return 0
    word_list = list(word)
    word_list.sort()
    res=0
    res_list=[]
    for l in range(n):
        for r in range(l+1,n):
            temp=content[l:r+1]

            temp1 = list(temp)
            temp1.sort()
            if temp1 == word_list:
                res+=1
                res_list.append(temp)
            else:
                pass
    return res,res_list

#方法2  定长看内容
def get_result(content,word):
    if len(content) < len(word):
        return 0
    ans = 0

    count = {}
    m = len(content)
    n = len(word)
    l = 0

    for c in word:
        if c not in count:
            count[c] = 1
        else:
            count[c] +=1
    count1={}
    for k,v in count.items():
        count1[k] = v

    while l  <= m-n:
        temp = content[l:l+n]
        print(temp)
        mark=0
        count1 = {}
        for k, v in count.items():
            count1[k] = v

        for c in temp:
            if c not in count1:
                break
            else:
                count1[c] -=1
        for c in count1:
            if count1[c] != 0:
                mark=1
                break
            else:
                pass
        if mark == 0:
            ans+=1

        l +=1
    return ans

#滑动窗口

def get_result(content,word):
    m = len(content)
    n = len(word)
    if m < n:
        return 0
    ans = 0
    count={}
    dictr = {}
    for c in word:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    l = 0
    # for c in word:
    #     count[c] = 0-count[c]
    for c in content[0:n]:
        if c not in dictr:
            dictr[c] = 1
        else:
            dictr[c] += 1
    total = n
    for c in dictr:
        if count.get(c) is not None:
            if count[c] > 0:
                total -=1
            count[c] -=1
    if total == 0:
        ans +=1


    while l+n < m:
        temp = content[l:l+n]
        if content[l+n]  in count :
            total -= 1
        if content[l]  in count:
            total +=1
        if total == 0:
            ans += 1


        l+=1

    return ans
print(get_result(content, word))