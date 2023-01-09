#ASSIGNMENT 2
#Q1(a)
word = "Python is a case sensitive language"
print(len(word))
#Q1(b)
word = "Python is a case sensitive language"
print(word[::-1])
#Q1(c)
word = "Python is a case sensitive language"
a = word[10:27]
print(a)
#Q1(d)
word = "Python is a case sensitive language"
print(word.replace("a case sensitive", "an object oriented"))
#Q1(e)
word = "Python is a case sensitive language"
print(word.index("a"))
#Q1(f)
word = "Python is a case sensitive language"
print(word.replace(" ", ""))


#Q2
name = input("enter your name")
sid = input("enter your sid")
branch = input("enter your branch")
cgpa = float(input("enter your cgpa"))
print("hey,"+name+" here!\nmy sid is "+sid+"")
print("i am from "+branch+" branch and my cgpa is "+str(cgpa)+"")

#Q3
a = 56
b = 10
print(a & b)
print(a|b)
print(a^b)
#Q3(d)
a = 56
b = 10
print(a << 2)
print(b << 2)
#Q3(e)
a = 56
b = 10
print(a >> 4)
print(b >> 4)


#Q4
a = float(input("enter your first number"))
b = float(input("enter your second number"))
c = float(input("enter your third number"))
if a > b > c or a > c > b:
    print(a)
elif b > c > a or b > a > c:
    print(b)
elif c > b > a or c > a > b:
    print(c)
elif a==b==c:
    print("numbers are equal")
else:
    print("error")


#Q5
word = input("enter your string")
needed_word = ("name")
if needed_word in word:
    print("word found")
else:
    print("word not found")

#Q6
a = float(input("enter your first length"))
b = float(input("enter your second length"))
c = float(input("enter your third length"))
if a > b + c or b > a + c or c > a + c:
    print("triangle cannot be formed")
else:
    print("triangle can be formed")
