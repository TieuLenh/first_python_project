#300 bai code thieu nhi
#Bai 1
def bai1():
    print('Hello, World!')

def bai2():
    name = input('Enter your name: ')
    print(f'Hello {name}, nice to meet you.')
    print('Hello {}, nice to meet you.'.format(name)) 

def bai3():
    a = int(input('a = '))
    b = int(input('b = '))
    print(f'{a} + {b} = {a + b}')

def bai4():
    n = int(input('n = '))
    if n % 2 == 0:
        print(f'{n} la so chan.')
    else:
        print(f'{n} la so le')
    
def bai5():
    n = int(input('n = '))
    print(f'Bang cuu chuong cua {n} la:')
    for i in range(1,10):
        print(f'{n} x {i} = {i * n}')

from math import sqrt
def bai6():
    n = int(input('n = '))
    snt = True
    if(n <= 2):
        snt = False
    for i in range (2,int(sqrt(n)) + 1):
        if n % i == 0:
            snt = False
            break
    if snt:
        print(f'{n} la so nguyen to.')
    else:
        print(f'{n} khong phai la so nguyen to.')

def bai7():
    n = int(input('n = '))
    result = 1
    for i in range(2,n+1):
        result *= i
    print(f'{n}! = {result}')

def bai8():
    for i in range(1,101):
        print(i, end=' ')
    print()

def bai9():
    for i in range(2,101,2):
        print(i, end=' ')
    print()

def bai10():
    for i in range(1,101,2):
        print(i, end=' ')
    print()

def bai11():
    a = list(map(int,input('Nhap day so: ').split()))
    print('so lon nhat trong day tren la:',max(a))

def bai12():
    a = list(map(int,input('Nhap day so: ').split()))
    print('so nho nhat trong day tren la:',min(a))

def bai13():
    str = input('Nhap chuoi: ')
    print(len(str))

# In ra dòng chữ "Hello, World!"
# Nhập vào tên và in ra lời chào tên đó.
# Nhập vào hai số, in ra tổng của chúng.
# Nhập vào một số, kiểm tra số đó chẵn hay lẻ.
# Nhập vào một số, in ra bảng cửu chương của số đó.
# Nhập vào một số, kiểm tra số đó có phải số nguyên tố không.
# Nhập vào một số, tính giai thừa của số đó.
# In ra các số từ 1 đến 100.
# In ra các số chẵn từ 1 đến 100.
# In ra các số lẻ từ 1 đến 100.
# Nhập vào một dãy số, in ra số lớn nhất.
# Nhập vào một dãy số, in ra số nhỏ nhất.
# Nhập vào một chuỗi, đếm số ký tự trong chuỗi đó.
# Nhập vào một chuỗi, đếm số nguyên âm trong chuỗi.
# Nhập vào một chuỗi, in ra chuỗi đảo ngược.
# Nhập vào một số, kiểm tra số đó có phải số Palindrome không.
# Nhập vào một số, kiểm tra số đó có phải số hoàn hảo không.
# Nhập vào một số, kiểm tra số đó có phải số Armstrong không.
# Nhập vào một danh sách, in ra các phần tử trùng nhau.
# Nhập vào một danh sách, in ra các phần tử không trùng nhau.
# Nhập vào một danh sách, sắp xếp tăng dần.
# Nhập vào một danh sách, sắp xếp giảm dần.
# Nhập vào một số, in ra dãy Fibonacci đến số đó.
# Nhập vào một số, kiểm tra số đó có phải số chính phương không.
# Nhập vào một số, kiểm tra số đó có phải số chia hết cho 3 và 5 không.
# Nhập vào một chuỗi, in ra từng ký tự trên một dòng.
# Nhập vào một chuỗi, đếm số từ trong chuỗi.
# Nhập vào một danh sách, tính tổng các phần tử.
# Nhập vào một danh sách, tính trung bình cộng các phần tử.
# Nhập vào một số, in ra hình tam giác sao có chiều cao bằng số đó.
