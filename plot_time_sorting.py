import timeit
import random
import matplotlib.pyplot as plt

def rand(N):
    l=[random.randint(0,1000000) for i in range(N)]
    return l


size_10=rand(10)
size_100=rand(100)
size_1000=rand(1000)
size_10000=rand(10000)
size_100000=rand(100000)

# print(size_10)
# print(size_100)
# print(size_1000)
# print(size_10000)
# print(size_100000)




def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        pivot=l[0]
        less=[]
        greater=[]
        for i in l:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)


        return quick_sort(less) + [pivot] + quick_sort(greater)


def merge_sort(l):

    if len(l)<=1:
        return l

    midpoint=len(l)//2

    left = merge_sort(l[:midpoint])
    right = merge_sort(l[midpoint:])

    return merge_leftright(left, right)


def merge_leftright(left, right):
    result=[]

    left_pointer=0
    right_pointer=0

    while left_pointer<len(left) and right_pointer< len(right):
        if left[left_pointer] <= right[right_pointer]:

            result.append(left[left_pointer])
            left_pointer+=1

        else:
            result.append(right[right_pointer])
            right_pointer+=1

    result+=(left[left_pointer:])
    result+=(right[right_pointer:])

    return result


print(merge_sort(size_10))
print(merge_sort(size_100))
print(quick_sort(size_1000))
print(quick_sort(size_10000))

if __name__ == '__main__':
    time_test_merge=[]
    t_10 = timeit.timeit("merge_sort(size_10)", number=5, globals=globals())
    time_test_merge.append(t_10)
    t_100 = timeit.timeit("merge_sort(size_100)", number=5, globals=globals())
    time_test_merge.append(t_100)
    t_1000 = timeit.timeit("merge_sort(size_1000)", number=5, globals=globals())
    time_test_merge.append(t_1000)
    t_10000 = timeit.timeit("merge_sort(size_10000)", number=5, globals=globals())
    time_test_merge.append(t_10000)
    t_100000 = timeit.timeit("merge_sort(size_100000)", number=5, globals=globals())
    time_test_merge.append(t_100000)
    print(time_test_merge)

    time_test_quick=[]
    t_10 = timeit.timeit("quick_sort(size_10)", number=5, globals=globals())
    time_test_quick.append(t_10)
    t_100 = timeit.timeit("quick_sort(size_100)", number=5, globals=globals())
    time_test_quick.append(t_100)
    t_1000 = timeit.timeit("quick_sort(size_1000)", number=5, globals=globals())
    time_test_quick.append(t_1000)
    t_10000 = timeit.timeit("quick_sort(size_10000)", number=5, globals=globals())
    time_test_quick.append(t_10000)
    t_100000 = timeit.timeit("quick_sort(size_100000)", number=5, globals=globals())
    time_test_quick.append(t_100000)
    print(time_test_quick)


a=[10,100,1000,10000,100000]
x=a
plt.figure()
plt.subplot(311)
y=time_test_merge
plt.plot(x,y)
plt.xscale('log')
plt.yscale("log")
plt.title('Mergesort')
plt.ylabel("time")
plt.xlabel("size")
plt.subplot(313)
y=time_test_quick
plt.plot(x,y)
plt.xscale('log')
plt.yscale('log')
plt.title('Quicksort')
plt.ylabel("time")
plt.xlabel("size")
plt.show()
#plt.savefig("sorting.png")

