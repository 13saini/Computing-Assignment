#q=1

text_input=input("enter text here\n")
if (" "not in text_input):
    char_counter={}

    for i in text_input:
       char_counter[i]=text_input.count(i)
    print(char_counter)
else:
    print("the inputshould not start with space")


#q=2

    
Day = int(input("enter day "))
Month = int(input("enter month "))
Year = int(input("enter year "))

if 1<=Day<30 and Month != 2:
    date = Day ++1
    print("Next Date is:",date,"/",Month,"/",Year)
elif Day == 31 and Month == 12:

    date = 1
    mon = 1
    yr = Year +1
    print("Next Date is:",date,"/",mon,"/",yr)
elif Day == 30 and Month == 4 or 6 or 9 or 11:
    date = 1
    mon = Month +1
    print("Next Date is:",date,"/",mon,"/",Year)
elif Day == 28 and Month == 2:
    if Year%4 != 0:
        date = 1
        mon = Month +1
        
    else:
        if Day == 28:
            date = 29
            print("Next Date is:",date,"/",Month,"/",Year)
        else:
            date = 1
            mon = Month +1
            print("Next Date is:",date,"/",mon,"/",Year)
        
    


else:
    date = 1
    mon = Month + 1
    print("Next Date is:",date,"/",mon,"/",Year)



#q=3

my_list = [2, 7, 8]
sq_list=[]
for i in my_list:
     sq_tup=(i,i**2)
     sq_list.append(sq_tup)
print(sq_list)


#q=4

marks=int(input("Marks\n"))

if(marks>=4 and marks<=10):
     if(marks==4):
         grade="D"
         perf="poor"
     elif(marks==5):
         grade="C"
         perf="below average"
     elif(marks==6):
         grade="C+"
         perf="average"
     elif(marks==7):
         grade="B"
         perf="good"
     elif(marks==8):
         grade="B+"
         perf="very good"
     elif(marks==9):
         grade="A"
         perf="excellent"
     elif(marks==10):
         grade="A+"
         Perf="outstanding"
else:
     print("error")

print(f"Your Grade is {grade} and Your Performance is {perf}.")


#q=5

           
print('Question Number5')

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(alphabets[counter], end="")
            counter=counter+1
        column=column+1
    print("")
  

#q=6

condition=True
Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        SID=int(input("Please Enter SID of Student- "))
        name=input("Please enter the name of the Student- ")
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N- ")
        condition = True

    else:
        condition = False

print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("Part b")
Val_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

print("Part c")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("Part D")
SID_tbf=int(input("Please enter the student's SID whose detail you need- "))
if SID_tbf in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_tbf]}")
else:
    print("The SID is not present in the given Data")
print("")


                 
#q=7
number=int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))


a_n1=1
a_n2=0
n=0

sum=a_n1+a_n2


print(f"Fibonnaci sequence with {number} terms")
print(a_n2)
print(a_n1)

while n<number-2:
    a_n=a_n2+a_n1
    a_n2=a_n1
    a_n1=a_n
    print(a_n)
    n=n+1
    sum+=a_n
average=sum/number
#printing the program end prompt
print(f"Average of total {number} terms of sequence is {average}")



#q=8


set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

set_a=(set1|set2)-(set1&set2)
print("part a:",set_a)

set_b=(set1|set2|set3)-(set1&set2)-(set2&set3)-(set3&set1)
print("part b:",set_b)

set_c=(set1&set2)|(set2&set3)|(set3&set1)-(set1&set2&set3)
print("part c:",set_c)

list_d=[]
for i in set1:
    if i>=1 and i<10:
       list_d.append(i)
set_d=set(list_d)
print("part d:",set_d)

list_e=[]
for i in (set1|set2|set3):
    if i>=1 and i<10:
       list_e.append(i)
set_eout=set(list_e)
print("part e:",set_eout)

