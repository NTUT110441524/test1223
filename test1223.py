#1A2B game
import streamlit as st
import random

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
answer=random.shuffle(items)
answer=''
a_count=0 # initial A count
b_count=0 # initial B count

for i in range(4):
    answer+=str(items[i])
while(True):
    #number=st.text_input('請輸入數字： ')
     number=st.number_input('請輸入數字： ')
    st.write(answer)
    if not number.isdigit():  #cheak all input is digit
        pass
    else:
        if number==answer:
            st.write('很棒你答對了')
            break
        for i in range(4):
            for j in range(4):
                if i==j and number[i]==answer[j]:
                    a_count+=1
                elif number[i]==answer[j]:
                    b_count+=1
        st.write('{0}A{1}B'.format(a_count,b_count))
        a_count=0
        b_count=0
        
