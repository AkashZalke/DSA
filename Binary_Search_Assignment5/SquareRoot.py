#Time Complexity : O(log(number))
number = int(input())
l = 0 
r = number
while l<=r:
    mid = (r+l)//2
    if mid*mid == number:
        break
    if mid*mid > number:
        r = mid-1
    else:
        l = mid+1 
print(mid)




