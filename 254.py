
fact=[1,1,2,6,24,120,720,5040,40320,362880]
def f(n):
    nums = [int(i) for i in str(n)]
    x = 0
    for num in nums:
        num = int(num)
        x += fact[num]
    return x

def sf(n):
    nums = [int(i) for i in str(f(n))]
    return sum(nums)

def g(n):
    i = 0
    while(n != sf(i)):
        i += 1
    return i

def sg(n):
    nums = [int(i) for i in str(g(n))]
    return sum(nums)

for run in range(0,int(input())):
    n, m = input().split(" ")
    n, m = int(n), int(m)
    curSum = 1
    for num in range(1, n + 1):
        curSum += sg(num)
    print(curSum%m)
