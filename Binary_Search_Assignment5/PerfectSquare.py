#Time Complexity : O(log(number))
n = int(input())
l = 0 
r= n
while True:
    mid= (r+l)//2
    if l>r:
        print("False")
        break
    if mid*mid == n:
        print("True")
        break
    if mid*mid > n:
        r=  mid-1
    else:
        l= mid+1