#python list
a=[1,2,"roshan",30.50,False]
print(a)

#append
a.append(25)
print(a)

#extend
a.extend([68,"ganesh",50.3])
print(a)

#update
a[3]="rosh"
print(a)

#insert
a.insert(1,10)
print(a)

b=[1,"suman",45.5]
a.extend(b)
print(a,"\n")

#positive indexing
print("index 0 is", a[0])
print("index 1 is", a[1])
print("index 2 is", a[2])
print("index 3 is", a[3])
print("index 4 is", a[4])
print("index 5 is", a[5])
print("index 6 is", a[6])
print("index 7 is", a[7])
print("index 8 is", a[8])
print("index 9 is", a[9],"\n")

#negative indexing

print("index -1 is", a[-1])
print("index -2 is", a[-2])
print("index -3 is", a[-3])
print("index -4 is", a[-4])
print("index -5 is", a[-5])
print("index -6 is", a[-6])
print("index -7 is", a[-7])
print("index -8 is", a[-8])
print("index -9 is", a[-9])
print("index -10 is", a[-10],"\n")

#remove
a.remove(68)
print("The list after removing an element :",a,"\n")

#pop
a.pop(3)
print("The list after removing the element by using pop method :",a,"\n")

a.pop()
print(a)

#slicing
print(a[0:3:1],"\n")

print(a[0:],"\n")

print(a[0::3]"\n")

print(a[-1::-1],"\n")

print(a[5:])



#tuple

a=(1,"suresh",53.9,4)
print(a,"\n")
print(type(a),"\n")


#delete
del a

#Dictionary

student={"name":"roshan","idn":1, "marks":50, "percentage":95.5}
print(student)

#update
student["marks"]=80
print(student)

#append
student["gender"]="male"
print(student)

del student["idn"]
print(student)

#clear
student.clear()
print(student)

#delete the entire dictionary
del student

#set
s={34,"set",40.9,43}
print(s)

#update
s.update([45,39])
print(s)

#append
s.add("list")
print(s)

#remove
s.remove("set")
print(s)

#clear
s.clear()
print(s)

#del
del s

#union
s1={"rosh",123,50.0}
s2={"rahman",45,34.2}
s3=s1.union(s2)
print(s3)

print(s1.intersection(s2))

#concatination
str1=input("Enter the string :")
str2=input("Enter the another string: ")
print("The concatination of two strings is:",str1+str2)

#Addition of two numbers
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print("The sum of two numbers is:",num1+num2)


def cal():
  n1=int(input("Enter the First number:"))
  n2=int(input("Enter the second number:"))
  n3=int(input("Enter the third number:"))
  n4=int(input("Enter the fourth number:"))


  print("\nThe sum of four numbers:", n1+n2+n3+n4,"\n")

  print("The product of four numbers:", n1*n2*n3*n4,"\n")

  print("The subtraction of four numbers:", (n1-n2)-(n3-n4),"\n")

cal()

def det(name,roll,marks):
  print("Name of the student: ",name)
  print("Roll number of the student:", roll)
  print("Marks of the student:",marks)

det("Roshan",810,50)
