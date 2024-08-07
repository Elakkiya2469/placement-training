email=input("Enter your pasword:\n")
b=[]
count1=0
count2=0
count3=0
count4=0
a=len(email)
for i in email:
  b.append(i)
for i in b:
  if(i>='a' and i<='z'):
    count1+=1
  if(i>='A' and i<='Z'):
    count2+=1
  if(i.isdigit()==True):
    count3+=1
  if(i=='$'or i=='#' or i=='@'):
    count4+=1
  if(count1>=1 and count2>=1 and count3>=1 and count4>=1 and a>=6 and a<=16):
    print("Valid password\n")
  else:
    print("Not Valid password\n")
