#問題名:mission3
#概要:最初に10を代入したリストに1から100までのランダムな数字を10個追加して、表示するプログラム
import random

rand_list=10

for i in range(10):
    rand_list.append(random.randint(1,100))

print(rand_list)