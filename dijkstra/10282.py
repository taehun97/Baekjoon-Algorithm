import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    time = [float('inf') for _ in range(n+1)]
    time[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        cur_time, cur_node = heapq.heappop(queue)
        
        if time[cur_node]<cur_time: continue
        
        for next_node, next_time in dependency[cur_node]:
            new_time = next_time + cur_time
            if time[next_node]>new_time:
                time[next_node] = new_time
                heapq.heappush(queue, (new_time, next_node))

    return time            

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    dependency = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        dependency[b].append((a, s))
        
    elapsed_times = dijkstra(c)
    
    infected_computer_count = 0
    total_time = 0
    for t in elapsed_times:
        if t==float('inf'): continue
        else: infected_computer_count += 1
        
        if total_time<t: total_time = t
    
    print(infected_computer_count, total_time)
        
    