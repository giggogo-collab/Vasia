import math

while True:
    try:
        x = float(input("Введите число: "))
        if x == 0:
            print(" x не может быть равен 0.")
            continue
        break
    except ValueError:
        print("Введите корректное число.")

y = (math.tan(math.pi)+math.sqrt(math.exp2(x)))/(2*x*x)
print("y = ", y)

if   math.isnan(y)or math.isinf(y):
    print("либо бесконечность либо Nan, you know вась")
    exit()
#gvjhjhvb.,ll
if y < 0:
    print("отрицательное")
else:
    print("положительное")

if y == int(y):
    if int(y) % 2 == 0:
        print("четное")
    else:
        print("нечетное")
else:
    print("значение не является целым, чётность не определена")
