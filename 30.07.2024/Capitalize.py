l=['a','an','is','the','in','on','but','between','because','of','under']
x=input("enter the sentence :")
x=x.split()
y=""
for i in x:
    if x.index(i)==0 or i.lower() not in l:
        y+=i.capitalize()+" "
    else:
        y+=i+" "
print(y)
