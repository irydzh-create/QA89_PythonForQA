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


numbers=[12,56,94,6]
print(max(numbers))
print(min(numbers))

res=sorted(numbers)
print(res)
print(numbers)

print(sorted(numbers,reverse=True))
print(sorted(fruits))
print(sorted(fruits,reverse=True))

word = 'python'
print(sorted(word))
result= ''.join(sorted(word))
print(result) #в алфавитном порядке отсотрировал hnopty

names=['Aleks', 'Kristina','Bob','Tom']
print(sorted(names)) #po alfavity Imena sort
print(sorted(names,key=len))#po dline
#sorted -  функц берет кол и возвразает новую soydaet new list no ne menyaet
# sort - метод списка только листа , меняет список

#по алфавиту
names.sort()#меняет список и возвращает нан
print(names)

names.sort(key=len)#сравни имена по кол символов
print(names)


