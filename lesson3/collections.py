empty_list=[]
mixed_list=[]
fruits=['orange','strawberry','mango','banana']
print(fruits)
print(fruits[0])

fruits[1]="lemon"
print(fruits)
print(fruits[1])

list1=['orange','lemon']
list2=['shampoo','soap']
combo_list=list1+list2
print(combo_list)

fruits=['orange','strawberry','mango','apple']
first=fruits[0]
second=fruits[1]
first,second,third, *rest=fruits
print(first)
print(second)
print(third)


fruits=['orange','strawberry','mango']
for item in fruits:
    print(f"item in fruits: {item}")

correct_answers=['orange','strawberry','mango']
correct=[word.lower() for word in correct_answers]
user_answers=['orange','strawberry','apple']



if correct_answers==user_answers:
    print("Correct answer")
else:
    print("Incorrect answer")

print(len(fruits))
max(fruits)
print(max(fruits))
