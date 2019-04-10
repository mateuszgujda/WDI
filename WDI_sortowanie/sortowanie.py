import random
import time

random.seed()


def select_sort(to_sort):
    for i in range(len(to_sort)-1):
        min = i
        for j in range(i+1,len(to_sort)):
            if(to_sort[min]>to_sort[j]):
                min = j
        to_sort[i], to_sort[min] = to_sort[min], to_sort[i]

    return to_sort



def insert_sort(to_sort):
    for i in range(1,len(to_sort)):
        for j in range (i,0,-1):
            if to_sort[j-1]>to_sort[j]:
                to_sort[j-1],to_sort[j]=to_sort[j],to_sort[j-1]
            else:
                break
    return to_sort


def bubble_sort(to_sort):
    for i in range(len(to_sort)-1):
        for j in range(len(to_sort)-i-1):
            if(to_sort[j]>to_sort[j+1]):
                to_sort[j+1], to_sort[j] = to_sort[j], to_sort[j+1]

    return to_sort


def mergeSort(tablica):
    wynik = list()
    if(len(tablica)<2):
        return tablica
    srodek = len(tablica)//2
    tab1 = mergeSort(tablica[:srodek])
    tab2 = mergeSort(tablica[srodek:])
    i = 0
    j = 0
    while( i<len(tab1) and j<len(tab2)):
        if(tab1[i]>tab2[j]):
            wynik.append(tab2[j])
            j+=1
        else:
            wynik.append(tab1[i])
            i+=1
    wynik+=tab1[i:]
    wynik+=tab2[j:]
    return wynik

def quickSort(tablica):
    mniejsze = list()
    rowne = list()
    wieksze = list()

    if (len(tablica) > 1):
        pivot = tablica[0]
        for i in tablica:
            if (i > pivot):
                wieksze.append(i)
            elif (i < pivot):
                mniejsze.append(i)
            else:
                rowne.append(i)
        return quickSort(mniejsze) + rowne + quickSort(wieksze)
    else:
        return tablica

def heapSort(tablica):
    for i in range(len(tablica),-1,-1):
        heapify(tablica,i,len(tablica))
    for i in range(len(tablica) - 1, 0, -1):
        tablica[0], tablica[i] = tablica[i], tablica[0]
        heapify(tablica, 0, i)
    return tablica


def heapify(tablica,root,size):
    max = root
    leftChild = 2*max +1
    rightChild = 2*max+2
    if(leftChild<size and tablica[leftChild]>tablica[max]):
        max = leftChild
    if(rightChild<size and tablica[rightChild]>tablica[max]):
        max = rightChild
    if(max != root):
        tablica[root],tablica[max]=tablica[max], tablica[root]
        heapify(tablica,max,size)


def bucketSort(tablica,min,max,bucketnum):
    space = (max-min)//bucketnum;
    buckets = [[] for i in range(bucketnum)]
    for i in tablica:
        bucket_notfound = True
        j=0;
        while(bucket_notfound):
            if(i>=min+(space*j) and i<min+(space*(j+1))):
                bucket_notfound = False
                buckets[j].append(i)
            else:
                j=j+1;
    sorted=[]
    for i in range(0,bucketnum):
        sorted.extend(insert_sort(buckets[i]))
    return sorted




to_sort = [random.randrange(100)+1 for x in range(50)]
copy_1 = to_sort.copy()
copy_2 = to_sort.copy()
copy_3 = to_sort.copy()
copy_4 = to_sort.copy()
copy_5 = to_sort.copy()
copy_6 = to_sort.copy()

print("Nieposortowana :")
print(to_sort)
print("Sortowanie bąbelkowe:")
print(bubble_sort(to_sort))
print("Sortowanie przez wstawianie:")
print(insert_sort(copy_1))
print("Sortowanie przez wybieranie:")
print(select_sort(copy_2))
print("Szybkie sortowanie")
print(quickSort(copy_3))
print("Sortowanie przez scalanie:")
print(mergeSort(copy_4))
print("Sortowanie przez kopcowanie:")
print(heapSort(copy_5))
print("Sortowanie kubełkowe:")
print(bucketSort(copy_6,1,101,50))


def test(sort_method,kubelkowe=False):
    czas = []
    for i in range(1000,2001,100):
        sortowanie=[random.randrange(100)+1 for x in range(i)]
        srednia = 0
        dane = i
        for i in range(1000):
            temp = sortowanie.copy()
            start_time = time.time()
            if not kubelkowe:
                sort_method(temp)
            else:
                sort_method(temp,1,101,100)
            finish_time = time.time() - start_time
            srednia = srednia+finish_time

        czas.append(srednia/1000)


test(bubble_sort)
test(insert_sort)
test(select_sort)
test(quickSort)
test(mergeSort)
test(heapSort)
test(bucketSort,True)




