print ('Program Untuk Menentukan Bilangan Terbesar Dari 3 Buah Bilangan')
print ('\nMasukkan 3 buah bilangan!')
a=int(input('Bilangan A = '))
b=int(input('Bilangan B = '))
c=int(input('Bilangan C = '))

if a > b and a> c:
    print("\nBilangan A: ",a, "adalah bilangan terbesar ")
elif b > c and b > a:
    print("\nBilangan B: ",b, "adalah bilangan terbesar ")
else:
    print("\nBilangan C: ",c, "adalah bilangan terbesar ")


