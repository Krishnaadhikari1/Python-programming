mark=int(input("enter your mark :"))
if(mark>=90):
    grade="A+"
elif(mark>=80 and mark<=90):
    grade="A"
elif(mark>=70 and mark<=80):
    grade="B+"
elif(mark>=60 and mark<=70):
    grade="B"
elif(mark>=50 and mark<=60):
    grade="c+"
elif(mark>=40 and mark<=50):
    grade="c"
else:
    grade="fail"
print("grade of the student=",grade)
