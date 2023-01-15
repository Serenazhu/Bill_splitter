print("Welcome to Bill Spliter!")
#people=int(input("How many people are at your table?  "))
meal=float(input("How much is the meal? (Jus the meal:no taxes/tips) "))
gross= meal*1.08

tip=int(input("How much is the tip?(what percentage. e.g 15.) "))
tip_amount=meal*tip/100

total=gross+tip_amount
print(f"Your total amount with tax is ${total}.")
people=int(input("How many people are at your table?  "))
share=total/people
print(f"There are {people} people to share the bill. ${share} per person :)")


