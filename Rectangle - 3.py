m = int(input())
n = int(input())
count = 0
while count < m:
    result = count + 1
    result = str(result) + " "
    result = (result * n)
    print(result)
    count = count + 1