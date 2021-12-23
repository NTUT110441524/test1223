# -*- coding: utf-8 -*-

#1A2B game
import random
import streamlit as st

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)#範圍隨機產出
answer=''
a_count=0 # initial A count
b_count=0 # initial B count
for i in range(4):
    answer+=str(items[i])
while(True):
    st.number_input('Enter the number: ')
    #number=st.text_input('Enter the number: ')
    #if not numberst.isdigit():  #判斷數字
   # if not number.isdigit():  #判斷數字
        pass
    else:
        if number==answer:
            st.write('excellent you guess the correct number')
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
        
        
