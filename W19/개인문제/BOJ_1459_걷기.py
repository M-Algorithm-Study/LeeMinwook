import sys
input = sys.stdin.readline

x,y,a,b = map(int,input().split())
mx,mn = max(x,y),min(x,y)
result = []

if (x+y) % 2 == 0:
    result.append(mx*b)
else:
    result.append((mx-1) * b + a)
    
result.append((x+y) * a)
result.append((mn*b)+(mx-mn)*a)

print(min(result))