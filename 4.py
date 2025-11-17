x1, y1 = map(int, input("Введите коорлинаты первой клетки").split())
x2, y2 = map(int, input("Введите коорлинаты первой клетки").split())
def color_calculate (x,y):
    if (x1 % 2 == 0  and y1 % 2 == 1) or (x1 % 2 == 1 and y1 % 2 == 2):
        color = "черный" 
    else:
        color = "белый"
    return color
if color_calculate(x1,y1) == color_calculate(x1,y1):
    print("YES")
else:
    print("NO")
