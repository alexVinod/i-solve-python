a=input("Enter Number1 :")
b=input("Enter Number2 :")
c=input("Enter Number3 :")

try:
    a,b,c = int(a),int(b),int(c)
    print("Max is :",max(int(a),int(b),int(c)))
except Exception as e:
    print(e,'\n',"Given Only Integer")
