num= int(input())
days= int(input())
max_ro= list(map(int,input().split()))
price_list=[]
for i in range(num):
    temp = list(map(int,input().split()))
    price_list.append(temp)

# print(max_ro,price_list)#[4, 5, 6] [[1, 2, 3], [4, 3, 2], [1, 5, 3]]
# def  get_result(max_ro,price_list):
#
max_ro = [4, 5, 6]
nums=3
days=3
price_list=[[1, 2, 3], [4, 3, 2], [1, 5, 3]]
lirui=0
for i in range(nums):
    chazhi = 0
    for l in range(days-1):
        for r  in range(l+1,days):
            chazhi=max(chazhi,price_list[i][r] - price_list[i][l])
    lirui+= chazhi*max_ro[i]


    # while left < right:
    #     if price_list[i][right] > price_list[i][left]:
    #         chazhi=price_list[i][right] - price_list[left]
    #     if price_list[left+1] < price_list[left]:
    #         left+=1
    #     if price_list[right-1] > price_list[right]:
    #         right-=1


print(lirui)







