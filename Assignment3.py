#ASSIGNMENT 3

#QUESTION 1
user_inp=input("ENTER A VALUE:")
length=len(user_inp.split())
characters=len(user_inp)
if (length>1):
    print(length)
else: print(characters)

#QUESTION 2
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy/mm/dd] %d-%d-%d." % (year, month, day))


#QUESTION 3
n=int(input("ENTER YOUR NUMBER:"))
list_of_tuples=n
list_of_tuples2=[(n,n**2)]
print(list_of_tuples2)

#QUESTION 4
a = {4:['D','Poor'], 5:('C','Below Average'), 6:('C+','Average'), 7:('B','Good'), 8:('B+','Very Good'), 9:('A','Excellent'), 10:('A+','Outstanding')}

grade = int(input('Grade : '))
if grade >= 4 and grade <= 10:
    print('Your Grade is',a[grade][0], 'and', a[grade][1], 'Performance.')
else: raise ValueError("Grade invalid")


#QUESTION 5
str1 = "ABCDEFGHIJK"
i=0
while len(str1)-i*2>=1:
    print(" "*i, str1[0:len(str1)-i*2])
    i=i+1



#QUESTION 6
conti = False #change later
list_students = {1:'z',2:'a', 3:'b' }
while conti:
    list_students[int(input("Enter SID : "))] = ' '.join(input("Enter name : ").split()) #computes name first then sid
    yn = input("Add more entries(Y/N): ").lower()
    if yn == 'y' : conti = True
    elif yn == 'n' : conti = False
    else: raise RuntimeError("Please enter Y or N only")

#print(list_students.items())
for i in list_students.keys():print("SID :", i, "Name :", list_students[i])

#key is the custom function to sort the given list by (here .items()
#dict.items() has keys on 0th index and items on 1st, thus the (lambda) function gives the same as the sorting key
list_sorted_nam = sorted(list_students.items(), key = lambda ls:ls[1])
print(list_sorted_nam)
list_sorted_sid = sorted(list_students.items(), key = lambda ls:ls[0])
print(list_sorted_sid)

sid = int(input("Enter SID of registered student: "))
if sid in list_students.keys() : print("Name: ", list_students[sid])
else : print("Given SID not registered")



#QUESTION 7
from statistics import mean

def seq(terms):
    if terms <= 0: raise ValueError("Please enter a postive no. of terms")
    elif terms == 1 : return [0]
    elif terms == 2 : return [0,1]
    else:
        seq = [0,1]
        numb = 2 #number of terms calculated
        while(numb < terms) :
            seq.append(seq[numb - 1] + seq[numb - 2])
            #print(seq)
            numb += 1
        return seq

fib = seq(int(input("Enter number of terms in sequence : ")))
print(fib)
print(round(mean(fib),2))



#QUESTION 8
#predefined sets
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#part a)
#A = Set1.union(Set2) - Set1.intersection(Set2)
A = Set1^Set2
print(A)

#part b)
#print((Set1&Set2) | (Set2&Set3) | (Set3&Set1))
#print(Set1|Set2|Set3)
B = (Set1|Set2|Set3) - ((Set1&Set2) | (Set2&Set3) | (Set3&Set1))
print(B)

#part c)
C = (Set1&Set2) | (Set2&Set3) | (Set3&Set1)
print(C)

#part d)
D = set()
for i in range (1,11) :
    if i not in Set1:  D.add(i)
print(D)

#part e)
E = set()
for i in range (1,11) :
    if i not in Set1|Set2|Set3:
        #print(i)
        E.add(i)
print(E)
