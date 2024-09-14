x=int(input('enter number \n'))
result =0

while x>0 :
    digit=x%10
    result = result + digit
    x=x//10
    
print("sum is", result)