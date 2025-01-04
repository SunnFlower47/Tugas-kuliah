from builtins import input, int, print
print()
print('##  Program mebaca sebuahh bilangan bulat positif, negatit atau nol  ##')
print('=' * 71)
print()

a=int(input("masukan bilangan bulat :"))

if (a > 0):
    print(f"{a} adalah bilangan bulat positif.")
elif (a < 0):
    print(f"{a} adalah bilangan bulat negatif.")
else:
    print(f"{a} adalah bilangan nol.")
