import timeit

def search_sorted_1(data, target):
    count = 0
    for item in data:
        count += 1
        if item == target:
            return count # Found it
    return count # Didn't find it

def search_sorted_2(data, target):
    count = 0
    start = 0
    end = len(data) - 1
    while start <= end:
        count += 1
        middle = ((end - start) // 2) + start
        if data[middle] == target:
            return count # Found it
        elif data[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return count # Didn't find it

print("{:>15}{:>15}{:>15}{:>15}{:>15}".format("n","sort1-count","sort2-count","sort1-time","sort2-time","alg3-time"))
print("{:>15}{:>15}{:>15}{:>15}{:>15}".format("-"*10,"-"*10,"-"*10,"-"*10,"-"*10))
for n in range(0,10001,100):
    test_data = [x for x in range(n)]
    count1 = search_sorted_1(test_data, n)
    count2 = search_sorted_2(test_data, n)
    time1 = timeit.timeit("search_sorted_1(test_data, n)", number=100, globals=globals()) / 100 * 1000
    time2 = timeit.timeit("search_sorted_2(test_data, n)", number=100, globals=globals()) / 100 * 1000
    print("{:>15}{:>15}{:>15}{:>15.5f}{:>15.5f}".format(n, count1, count2, time1, time2))
       

