a12 = input('Enter the range of a (example: 23 45): ')
b12 = input('Enter the range of b: ')
c12 = input('Enter the range of c: ')
print()

a1 = int(a12.split()[0])
b1 = int(b12.split()[0])
c1 = int(c12.split()[0])
a2 = int(a12.split()[1])
b2 = int(b12.split()[1])
c2 = int(c12.split()[1])

result0 = []
result00 = []
result000 = []
results_2 = []
results_1 = []
results_complex = []

for a in range(a1, a2 + 1):
    for b in range(b1, b2 + 1):
        for c in range(c1, c2 + 1):
            if a != 0:
                disc = b**2 - 4 * a * c
                if disc > 0:
                    r1 = round((-b + disc**0.5) / (2 * a), 2)
                    r2 = round(((-b - disc**0.5) / 2), 2)
                    results_2.append([a, b, c, r1, r2])
                elif disc == 0:
                    r = round(-b / (2 * a), 2)
                    results_1.append([a, b, c, r])
                else:
                    r12_real = round(-b / (2 * a), 2)
                    r1_im = round((-disc)**0.5 / (2 * a), 2)
                    r2_im = round(-((-disc)**0.5) / (2 * a), 2)
                    results_complex.append([a, b, c, r12_real, r1_im, r12_real, r2_im])
            else:
                if b != 0:
                    r = round(-c / b, 2)
                    result0.append([a, b, c, r])
                else:
                    if c != 0:
                        result00.append([a, b, c])
                    else:
                        result000.append([a, b, c])

print('Your solutions: \n')

for i in result000:
    print(f' {i[0]}x^2 + {i[1]}x + {i[2]}  has every x as a root')

for i in result00:
    print(f' {i[0]}x^2 + {i[1]}x + {i[2]}  has no roots')

for i in result0:
    print(f' {i[0]}x^2 + {i[1]}x + {i[2]}  has one root: {i[3]}')

for i in results_1:
    print(f' {i[0]}x^2 + {i[1]}x + {i[2]}  has one root: {i[3]}')

for i in results_2:
    print(f' {i[0]}x^2 + {i[1]}x + {i[2]}  has two roots: {i[3]} and {i[4]}')

for i in results_complex:
    print(f' {i[0]}x^2 + {i[1]}x + {i[2]}  has two complex roots: {i[3]} + {i[4]} * i and {i[5]} + {i[6]} * i')
print()

'''
Хотів ще зробити так, щоб замість штук 1х^2 або 0x^2 виводилось просто x^2 або 0, для краси, 
але як це зробити елегантно не придумав, тому забив
'''

