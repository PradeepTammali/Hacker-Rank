import os
def maximumProfit(tubes, l, m):
    new_tube =  int(m/7)
    count = 0
    for tube in tubes:
        if new_tube >= tube:
            count +=1 
    return count

if __name__ == '__main__':
    result = []
    a = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    n = int(input())
    for i in range(n):
        l, m = list(map(int, input().rstrip().split()))
        result.append(maximumProfit(a, l, m))
    for i in result:
        print(i)
    