#!/usr/bin/python3 
 
# 该实例演示了数字猜谜游戏
import random
print("数字猜谜游戏!")
again = 'y'
def guess_number():
    guess = 0
    number = random.choice(range(10))
    while guess != number:
        guess = int(input("请输入你猜的数字："))
        if guess == number:
            print("恭喜，你猜对了！")
        elif guess < number:
            print("猜的数字小了...")
        elif guess > number:
            print("猜的数字大了...")

while 1:
    if(again == 'y' or again == 'yes'):
        guess_number()
        again = 'n'
    again = str(input("重新开始请输入：y 或 yes ")).lower()
