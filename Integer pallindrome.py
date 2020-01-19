num = int(input("Enter any number"))
num1 = num
remainder, reverse = 0,0
while(num!=0):
    remainder = num%10
    #print("Remainder")
    #print(remainder)
    reverse = reverse*10
    reverse = reverse + remainder
    num = num//10
    #print(num)
if num1 == reverse:
    print("palindrome")
else:
    print("Not palindrome")
