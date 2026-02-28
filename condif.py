math= int(input("Enter math marks "))
bio= int(input("Enter bio marks "))
db= int(input("Enter db marks "))
total= math + bio + db
avg= total/3 
print("Total marks is ", total, "and average is ", avg)
if avg < 40 and avg >= 0:
    print("Fail")
elif avg >=40 and avg <=50:
    print("Pass")
elif avg > 50 and avg <=60:
    print("Merit")
elif avg > 60 and avg <=70:
    print("Dist")
