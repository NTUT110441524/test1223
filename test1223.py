import random
import streamlit as st

ranlist = []
def generate(lst):
    while len(lst) < 4:
        lst.append(randint(1,9))
        if len(lst) > 1:
            x = 0
            while x < len(lst)-1:
                if lst[x] == lst[len(lst)-1]:
                    del lst[len(lst)-1]
                else:
                    x += 1
    final_ans = ""
    for i in range(0,len(lst)):
        final_ans = final_ans + str(lst[i])
    return final_ans
def gamer():
    print("歡迎來到1A2B，密碼已經產生，請在四次之內猜中正確答案")
    finans = generate(ranlist)
    starter = True
    counter = 1
    while starter:
        if counter == 4:
            st.write("Game Over!!")
            starter = False
        while counter < 5:
            result = 0
            answer = input("請輸入你的答案：")
            for i in range(0,len(finans)):
                for j in range(0,len(finans)):
                    if answer[i] == finans[j]:
                        if i == j:
                            result += 10
                        else:
                            result += 1
            print(str(int(result/10)) + 'A' + str(result%10) + 'B')
            counter += 1
            if result == 40:
                print("恭喜你，答案就是" + str(finans))
                starter = False
gamer()
