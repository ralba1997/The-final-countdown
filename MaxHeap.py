class MaxHeap:

    def __init__(self, items=[]):
        self.name = None

        super().__init__()

        self.heap = [0]

        for i in items:

            self.heap.append(i)

            self.__floatUp(len(self.heap) - 1)



    def insert(self, data):

        self.heap.append(data)

        self.__floatUp(len(self.heap) - 1)



    def peek(self):

        if self.heap[1]:

            return self.heap[1]

        else:

            return False



    def delMax(self):

        if len(self.heap) > 2:

            self.__swap(1, len(self.heap) - 1)

            max = self.heap.pop()

            self.__bubbleDown(1)

        elif len(self.heap) == 2:

            max = self.heap.pop()

        else:

            max = False

        return max



    def getMax(self):

        if len(self.heap) > 2:

            max = self.heap[1]

        elif len(self.heap) == 2:

            max = self.heap[2]

        else:

            max = False

        return max





    def __swap(self, i, j):

        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]



    def __floatUp(self, index):

        parent = index // 2

        if index <= 1:

            return

        elif self.heap[index] > self.heap[parent]:

            self.__swap(index, parent)

            self.__floatUp(parent)



    def __bubbleDown(self, index):

        left = index * 2

        right = index * 2 + 1

        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:

            largest = left

        if len(self.heap) > right and self.heap[largest] < self.heap[right]:

            largest = right

        if largest != index:

            self.__swap(index, largest)

            self.__bubbleDown(largest)





m = MaxHeap([95, 96, 5, 4])



print(str(m.heap))



m.insert(22)

m.insert(135)

print(str(m.heap))

print(str(m.getMax()))

print(str(m.heap))
print(str(m.getMax()))

print(str(m.heap))

print(str(m.delMax()))
print(str(m.heap))
print(str(m.delMax()))
print(str(m.heap))
print(str(m.delMax()))
print(str(m.heap))
print(str(m.delMax()))

def genrandomnumbers(length):  # GENERATE length RANDOM NUMBERS  IN RANGE 1-maxval
    maxval = 1000000
    string = ""
    for n in range(length):
        string += str(randint(1, maxval)) + " "
    L = list(map(int, string.split()))
    return L


def insertnumbersinheap(aheap):
    for i in range(len(L)):
        aheap.insert(L[i])
    return aheap


def gettime(funcname, param, param2):
    if param2 == "":
        fn = funcname.__name__ + "(" + param.name + ")"
    else:
        fn = funcname.__name__ + "(" + param.name + "," + str(param2) + ")"
    setpar = "from __main__ import " + funcname.__name__ + "," + param.name
    t1 = Timer(fn, setpar)
    time = str(t1.timeit(1)) + " "
    return time

def maxelement(aheap):
    maxnodevalue = aheap.getMax()
    return maxnodevalue


def delmaxelement(aheap):
    aheap.delMax()


def writef(filename, myres):
    with open(filename, "w") as f:
        text = myres
        f.write('{}'.format(text))
    return


def readf(filename):
    with open(filename, "r") as f:
        r_n = f.readline()
    return r_n


from timeit import Timer

# import timeit
import random
from random import randint
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# import math

if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)
    if not os.path.exists("Data1"):
        os.makedirs("Data1")
    os.chdir(path + "\Data1")
    maxpoweroften = 6
    numberoftests = 5

    insertion_times = ""
    findmax_times = ""
    delmaxelement_times = ""

    for nrtest in range(numberoftests):
        for dim in [10 ** p for p in range(1, maxpoweroften + 1)]:
            L = genrandomnumbers(dim)
            myheap = MaxHeap()
            myheap.name="myheap"
            time = gettime(insertnumbersinheap, myheap, "")
            insertion_times += time
            time = gettime(maxelement,myheap, "")
            findmax_times += time
            time = gettime(delmaxelement, myheap, "")
            delmaxelement_times += time
        insertion_times += "\n"
        findmax_times += "\n"
        delmaxelement_times += "\n"

    writef("insertion.txt", insertion_times)
    writef("maxheap.txt", findmax_times)
    writef("delmaxelement.txt", delmaxelement_times)

filenames = ["insertion", "maxheap", "delmaxelement"]
for filein in filenames:
    filename = filein + ".txt"
    t = []
    with open(filename, "r") as f:
        for i in range(numberoftests):
            t.append(list(map(float, f.readline().split())))

    # maxtimes = []
    # mintimes = []
    meantimes = []
    for j in range(maxpoweroften):
        # mintimes.append(min(t[i][j] for i in range(numberoftests)))
        # maxtimes.append(max(t[i][j] for i in range(numberoftests)))
        sumt = sum(t[i][j] for i in range(numberoftests))
        meantimes.append(sumt / numberoftests)

    if filein == "insertion":
        insertiontimes = meantimes
    elif filein == "maxheap":
        maxheaptimes = meantimes
    elif filein == "delmaxelement":
        delmaxtimes = meantimes

N = [10 ** p for p in range(1, maxpoweroften + 1)]

fig = plt.figure()
plt.plot(N, insertiontimes, "vb--")
plt.plot(N, maxheaptimes, "vg--")
plt.plot(N, delmaxtimes, "vc--")
plt.xscale('log', basex=10)
plt.yscale('log', basey=10)
plt.title("Max Heap")
plt.xlabel("Length of list of random numbers")
plt.ylabel("Times")
blue_patch = mpatches.Patch(color = "blue", label = "Max Heap- Insertion")
green_patch = mpatches.Patch(color = "green", label = "Max Heap- Get the max ")
cyan_patch = mpatches.Patch(color = "cyan", label = "Max Heap- Delete the max")
plt.legend(handles = [blue_patch, green_patch, cyan_patch])
axes = plt.gca()
axes.set_ylim([10**(-6), 10**2])
# plt.ylim(10**-6,1)
# plt.show()
fig.savefig("Binary Tree.png")