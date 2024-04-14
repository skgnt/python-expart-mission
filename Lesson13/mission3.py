#問題名:mission3
#概要:1~100の乱数を10個生成し、リストに格納してまとめて表示するプログラム
import random

rand_list=10

for i in range(10):
    rand_list.append(random.randint(1,100))

print(rand_list)