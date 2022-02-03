arr = [1,2,3,4,5,6,7,8,9]
x = int(input("Enter a value:"))

arr.append(10)

n=25
for i in range(11,100):
    arr.append(i)

arr.remove(7)
#defining function for obtaining sum of values in array
def _sum(arr):
    sum = 0

    for i in arr:
        sum = sum + i
    return(sum)
ans = _sum(arr)
print('The sum of the array is:',ans)


#checking if user input is in array
if x in arr:
    print(x,"is present in the array")
        
    #checking if user input is divisible by 2    
    if x%2 == 0:
        print(x,"is an even value")

    else:
        print(x,"is an odd value")  
 
else:
    print(x,"is not present in the array")
