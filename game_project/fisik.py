x1, y1, w1, h1 = list(map(int, input().split()))
x2, y2, w2, h2 = list(map(int, input().split()))
if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2:
    print("YES")
else:
    print("NO")