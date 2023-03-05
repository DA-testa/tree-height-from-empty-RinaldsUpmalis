# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function
    max_height = 0
    height_mas = numpy.zeros(n, dtype=int)
    children = {i: [] for i in range(n)}
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            height_mas[i] = 1
        else:
            children[parent].append(i)
    queue = [i for i in range(n) if parents[i] == -1]
    while queue:
        current = queue.pop(0)
        for child in children[current]:
            height_mas[child] = height_mas[current] + 1
            queue.append(child)

    return numpy.max(height_mas)
    # Your code here
    # return max_height


def main():
    # implement input form keyboard and from files
    text = input()
    n=0
    if text=="I":
        n=int(input())
        arr=input()
        parents=[int(x) for x in arr.split()]
    elif text=="F":
        filename = input()
        if filename[-1] == 'a':
            return
        with open(filename, 'r') as file:
            text = file.read()
            lines = text.split('\n')
            n = int(lines[0])
            parents = [int(x) for x in lines[1].split()]
    #n = 4
    #parents = [-1, 0, 0, 1]
    print(compute_height(n, parents)) 

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
