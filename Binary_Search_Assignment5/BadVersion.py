#Time Complexity : O(log(n))   n = Length Of List
quality_check = [0,1,1,1,1,1,1,1,1]
l = 0
r =len(quality_check)-1
while  l<r:
    mid = (l+r)//2 
    if quality_check[mid] == 1 and quality_check[mid-1] == 0:
        break
    if quality_check[mid] == 0  and quality_check[mid+1] == 1:
        mid+=1
        break
    if quality_check[mid] == 1:
        r = mid-1
    else:
        l = mid+1
print(mid)