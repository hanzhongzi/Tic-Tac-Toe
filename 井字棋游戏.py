#!/bin/env python3
# author:root
# datetime:3/9/205:26 PM
# software:PyCharm
import random
import time
import os


flag = True
list1 = [
    [["   "], [" | "], ["   "], [" | "], ["   "]],
    [["---"], ["-|-"], ["---"], ["-|-"], ["---"]],
    [["   "], [" | "], ["   "], [" | "], ["   "]],
    [["---"], ["-|-"], ["---"], ["-|-"], ["---"]],
    [["   "], [" | "], ["   "], [" | "], ["   "]],
]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listplay = set()
listcom = set()
winset = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7})


def show():
    for i in list1:
        for j in i:
            print(''.join(j), end="")
        print()


listnum = '''
说明：井字棋输入方框内对应数字，您的棋就会下到该位
（已占的格子输入无效哦）：
你的棋子是X

  1 |  2  | 3  
----|-----|----
  4 |  5  | 6  
----|-----|----
  7 |  8  | 9  


'''

str1 = " X "
str2 = " O "


def playerInsert(pnum):

    pnum = int(pnum)
    list2.pop(list2.index(pnum))
    listplay.add(pnum)
    if pnum == 1:
        list1[0][0] = str1
    elif pnum == 2:
        list1[0][2] = str1
    elif pnum == 3:
        list1[0][4] = str1
    elif pnum == 4:
        list1[2][0] = str1
    elif pnum == 5:
        list1[2][2] = str1
    elif pnum == 6:
        list1[2][4] = str1
    elif pnum == 7:
        list1[4][0] = str1
    elif pnum == 8:
        list1[4][2] = str1
    elif pnum == 9:
        list1[4][4] = str1


def computerInsert(cnum):
    cnum = int(cnum)
    listcom.add(cnum)
    if cnum == 1:
        list1[0][0] = str2
    elif cnum == 2:
        list1[0][2] = str2
    elif cnum == 3:
        list1[0][4] = str2
    elif cnum == 4:
        list1[2][0] = str2
    elif cnum == 5:
        list1[2][2] = str2
    elif cnum == 6:
        list1[2][4] = str2
    elif cnum == 7:
        list1[4][0] = str2
    elif cnum == 8:
        list1[4][2] = str2
    elif cnum == 9:
        list1[4][4] = str2


def computerChoice():
    ccnum1 = random.choice(list2)
    computerInsert(ccnum1)
    list2.pop(list2.index(ccnum1))


def win():
    global flag
    global winset
    print("***********************")
    for i in winset:
        if listcom & i in winset:
            show()
            print("computer win~!")
            flag = False
        elif listplay & i in winset:
            show()
            print("you win~")
            flag = False
        elif len(list2) == 0:
             show()
             print("平局")
   # print("listplay: ", listplay)
   # print("listcom: ", listcom)


for i in listnum:
    print(i, end="", flush=True)
    time.sleep(0.1)
print()
time.sleep(1)
x = random.choice([1, 2])
if x == 1:
    print("电脑先手～！")
    while flag:
        flag1 = True
        if flag1:
            computerChoice()
            win()
            os.system('clear')
            show()
        else:
            num = input("请选择您要输入的位置")
            num = int(num)
            if num not in list2:
                print("你走的位置有棋了")
                flag1 = False
                continue
            playerInsert(num)
            win()
            flag1 = True


else:
    print("您先手～！")
    while flag:
        num = input("请输入您要输入的位置")
        num = int(num)
        if num not in list2:
            print("你走的位置有棋了")
            continue
        playerInsert(num)
        win()
        computerChoice()
        os.system('clear')
        show()
        win()
 #       print("listplay: ", listplay)
 #       print("listcom: ", listcom)
