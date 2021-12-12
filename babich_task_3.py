t = ("Процент")
a = ("Процента")
ov = ("Процентов")
excl = [11, 12, 13, 14]
for i in range(100):
    i = i + 1
    if i in excl:
        print(i, ov)
    elif i % 10 == 1:
        print(i, t)
    elif 1 < i % 10 < 5:
        print(i, a)
    else:
        print(i, ov)
