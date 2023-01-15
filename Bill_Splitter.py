import streamlit as st

st.header("Welcome to Bill Splitter!")
#people=int(input("How many people are at your table?  "))
meal=float(st.number_input("How much is the meal? (Jus the meal:no taxes/tips) "))
gross= meal*1.08

tip=int(st.number_input("How much is the tip?(what percentage. e.g 15.) "))
tip_amount=meal*tip/100

total=gross+tip_amount
st.write(f"Your total amount with tax is ${round(total,2)}.")
people=int(st.number_input("How many people are at your table?  "))
if st.button('Calculate'):
    share=round(total/people,3)
    st.write(f"There are {people} people to share the bill. ${share} per person :smile:")
    st.balloons()
