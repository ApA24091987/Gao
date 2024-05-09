y = 37
print('hie')
if y < 0:
    print('меньше нуля')
print('bye')
# пример
a,  b = 15, 8
if a > b:
    print('a > b')
if a > b and a > 0:
    print('ok')
if (a > b) and (a > 0 or b > 200):
    print('yapi')
if a > b and (a < 0 or b > 200):
    print('ok')
if 8 < b and b < 10:
    print('yapi')
# сравнения - числа, строки, списки.
if '65' > '634':
    print('ok')
if '634' > '36':
    print('yapi')
if [2, 6] > [2, 9]:
    print('ok')
# нельзя сранить
#if '7' > 5:
    #print('ok')
#if [7, 8] > 7:
    #print('ok')
# есть лазейки
if '7' != 8:
    print('yapi')
if [7, 8] != 7:
    print('ok')