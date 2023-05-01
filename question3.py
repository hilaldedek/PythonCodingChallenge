# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
print("...1. diziyi giriniz...")
array1 = []
sayi1 = int(input("eklenecek sayiyi giriniz: "))
array1.append(sayi1)
while (sayi1 != -1):
    sayi1 = int(input("eklenecek sayiyi giriniz: "))
    array1.append(sayi1)
array1.remove(-1)
print("...2. diziyi giriniz...")
array2 = []
sayi2 = int(input("eklenecek sayiyi giriniz: "))
array2.append(sayi2)
while (sayi2 != -1):
    sayi2 = int(input("eklenecek sayiyi giriniz: "))
    array2.append(sayi2)
array2.remove(-1)
sum_array = array1+array2
sum_array.sort()
medyan = 0
if (len(sum_array) % 2 == 1):
    indis = (len(sum_array)/2)-0.5
    medyan = sum_array[int(indis)]
else:
    indis1 = (len(sum_array)/2)
    indis2 = ((len(sum_array)/2)-1)
    medyan = ((sum_array[int(indis1)]+sum_array[int(indis2)])/2)
