f=open("class_log.txt","a+")
print("student attenance :")
p=0
a=0
print("present - p \nabsent  - a")
try :
    z=int(input("Enter the total no. of students :"))
except ValueError as e:
    print("Error ",e)
for i in range(1,z+1):
    x=input(f"Roll.no.{i} : ")
    if x=='p' or x== 'P':
        p+=1
    elif x=="a" or x== "A":
        a+=1
    else:
        print("invalid input")
a=f"\nthe total no. of students :{str(z)},no. of students present :{str(p)},no. of students absent :{str(a)}\n"
print(a)
f.write(a)
f.close()
def review_class_log():
    try:
        with open("class_log.txt", "r") as file:
            log_contents = file.read()
            print("Class Log:")
            print(log_contents)
    except FileNotFoundError:
        print("No class log found for today.")
review_class_log()
