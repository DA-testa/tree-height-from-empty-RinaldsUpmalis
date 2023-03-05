# python3

import sys
import threading
import numpy

def compute_height(n, parents):
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

def main():
    text = input()
    parents=[]
    n=0
    if text[0]=="I":
        n=int(input())
        arr=input()
        parents=[int(x) for x in arr.split()]
    elif text[0]=="F":
        filename = input()
        if filename[-1] == 'a':
            return
        with open(filename, 'r') as file:
            text = file.read()
            lines = text.split('\n')
            n = int(lines[0])
            parents = [int(x) for x in lines[1].split()]

    print(compute_height(n, parents)) 

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
