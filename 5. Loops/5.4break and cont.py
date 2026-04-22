"""continue: terminate execution in the current iteration and 
             continues execution of the loop with the next iteration ."""
i=5
while(i<10):
    if(i==7):
        i+=1
        continue#skip
    print(i)
    i+=1

# break:used to terminate the loop when encountered.
i=1
while(i<5):
    print(i)
    if(i==4):
        break
    i+=1
print("end of the loop")