import sys

input = sys.stdin.readline

###################### solution 1 ######################

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     ary = [input().rstrip() for _ in range(n)]
    
#     ary.sort()
    
#     flag = True
#     for i in range(len(ary)-1):
#         if ary[i]==ary[i+1][:len(ary[i])]:
#             flag = False
#             break
    
#     print("YES") if flag else print("NO")
    
###################### solution 2 ######################

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
    
class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        current_node = self.head
        
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string
        
    def search_prefix(self, string):
        current_node = self.head
        
        for char in string:
            current_node = current_node.children[char]
        
        if current_node.children:
            return False
        else:
            return True
        
t = int(input())
for _ in range(t):
    n = int(input())
    arys = []
    trie = Trie()
    
    for _ in range(n):
        string = input().rstrip()
        arys.append(string)
        trie.insert(string)
    
    flag = True
    for ary in arys:
        if not trie.search_prefix(ary):
            flag = False
            break
    
    print("YES") if flag else print("NO")