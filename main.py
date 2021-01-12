import random
# new comment
# second comment
# 1) новый код: генерируем 0 массив
# generate void string
line = []
# n - длина массива
n = 11
# заполнять будем символами new_element
new_element = 1
for s in range(n):
    line.append(new_element)  # заполнили массив new_elemetами (добавляем их в список)
# 2) take 1 string
# modify by random inject "000"
m = random.randint(n - (n - 3), n - 3)
line[m] = 0
# line[m - 1] = 0
# line[m + 1] = 0
print("SLine", line)

# нужно реализовать: look where is start
# move randomly left or right
# randomly +1 to the left or right
lnum = 0

for i in range(100):

    md = random.randint(-1, 1)
    # print(m)
    if m == (n-(n-2)):
        m -= 1
        md = -1
        # md = -1
    elif m == 2:
        # md = 1
        m += 1
        md = 1
    else:
        m = m + md
    # m = m + md

    lineTwo = line
    lineTwo[m] = 0
    lineTwo[m - 1] = 0
    lineTwo[m + 1] = 0

    if md == -1:
        lineTwo[m + 2] = 1
    elif md == 1:
        lineTwo[m - 2] = 1
    else:
        pass

    print("Line2", lineTwo)
    lnum += 1
print("Сгенерировано:", lnum, "строк")
