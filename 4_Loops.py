#Task1
list1=[1,2,3,4]
list2=[1,4,5,6]
special_numbers = [4, 5]
for i in range(len(list1)):
    for j in range(len(special_numbers)):
        if list1[i] == special_numbers[j] or list2[i] == special_numbers[j]:
            print(special_numbers[j])
        else:
            print("Not in special numbers")
#Task2 (The task isnt complete one so Ill pass)
#Task3
i=0
while i<=10:
    print(i)
    i+=1
#Task4
def print_my_name():
    print("Abdullah")
#Task5
def print_my_name(first_name, last_name):
    print(f"My full name is {first_name,last_name}")
#Task6
def add(a, b =5):
    print(a + b)
#Task 7
def even_or_odd(list):
    for i in range(list):
        if list[i]%2==0:
            print(f"{list[i]}: is even")
        else:
            print(f"{list[i]}: is odd")
#Task8