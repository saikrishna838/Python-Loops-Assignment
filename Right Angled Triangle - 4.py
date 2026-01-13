n = int(input())
sum = 0
count = 1
while count <= n:
        star1 = sum + count
        star1 = ("* " * count)
        print(star1)
        count = count + 1
while count > n and count <= (n * 2):
        star2 = sum + 1
        star2 = ("* " * star2)
        print(star2)
        sum = sum + 1
        count = count + 1
        