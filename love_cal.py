boy=input("Enter name of boy: ").lower()
girl=input("Enter name of girl: ").lower()
combine=boy+girl

t=combine.count("t")
r=combine.count("r")
u=combine.count("u")
e=combine.count("e")
true=t+r+u+e


l=combine.count("l")
o=combine.count("o")
v=combine.count("v")
e=combine.count("e")
love=l+o+v+e

score=int(str(true)+str(love))

if(score<=10 or score>=90):
    print(f"Your love score is {score} and you are like coke and mentos")
elif(score>=40 or score<=50):
    print(f"Your love score is {score} and you are alright together")
else:
    print(f"Your love score is {score}")



