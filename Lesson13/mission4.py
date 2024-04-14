#問題名:mission4
#概要:
#何がエラーの原因かを考えて修正してみましょう。
num=int(input("数字を入力してください:"))
res=[]

for i in range(10):
    
    res.append(num/i)

print(res)