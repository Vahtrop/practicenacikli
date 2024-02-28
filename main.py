a = input('введите слово')
v = ''
for b in range(len(a)):
    if b % 2 == 0:
        v += a[b]. upper()
    else:
        v += a[b]. lower()
print(v)
vvod = int(input('Ввудите число от 0-1000'));
if vvod > 1000:
    print('фй фй фй какой плохой мальчик');
else:
    for b in range(0, vvod+1):
        print(b)