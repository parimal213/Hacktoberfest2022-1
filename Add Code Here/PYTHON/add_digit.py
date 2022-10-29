print("Enter a Number")
num = int(input())
sum = 0
while num>0:
    rem = num%10
    sum = sum+rem
    num = int(num/10)
print("\nSum of Digits of Given Number: ", sum)
