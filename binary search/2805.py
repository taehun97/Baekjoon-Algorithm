import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort()

def treeLengthAcquired(treeAry, height):
    sumLength = 0
    for i in range (len(treeAry)):
        if treeAry[i] - height > 0: sumLength += (treeAry[i] - height)
    
    return sumLength

acquiredTree=0
startLength=1
endLength = tree[len(tree)-1]

while(endLength>=startLength):
    middleLength = (endLength + startLength)//2
    acquiredTree = treeLengthAcquired(tree, middleLength)
    
    if acquiredTree>=M:
        startLength=middleLength+1
    elif acquiredTree<M:
        endLength=middleLength-1

print(endLength)