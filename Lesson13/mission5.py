#問題名:mission5
#概要:1から100までのランダムな数字を10個配列に格納し、それぞれの数字を表示するプログラム
import random

num_list=[]
for i in range(10):
    num_list.append(random.randint(100))

for i in range(10):
    print(f"{i+1}つ目にランダムに選ばれた数字は{num_list[i]}です。")

print(num_list)