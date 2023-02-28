s="abcsdfsadfafds"

# n = len(s)%8 #字符串长度除于8,取余，获知短于8的串的长度
# if n != 0: #补‘0’
#     s_0 = '0'*(8-n)
#     s = s+s_0
# s_c =[]
# for i in range(int(len(s)/8)):#要切几次片，存到新的列表中
#     if i==0 :#因为切片不能以0位index，另做一个判断
#         s_c.append(s[:8])
#     else:
#         s_c.append(s[i*8:(i+1)*8])
# for c in s_c:#打印
#     print(c)
# s = input()
n = len(s)
string=[]
if n % 8==0:
    num = int(n/8)-1
else:
    num=n//8
for i in range(num+1):
    string.append(s[8*i:8*i+8])
    print(string)
for i in range(num+1):
    string[i]=string[i].ljust(8,"0")

for i in range(num+1):
    print(string[i])
