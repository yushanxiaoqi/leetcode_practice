content = input()
word = input()
word_list = list(word)

nemb = len(content)
res = 0
for i in range(nemb - 1):
    for j in range(i + 1, nemb):
        temp = list(content[i:j + 1])

        if temp == word_list:
            res += 1
print(res)