import sys
import copy

input = sys.stdin.readline

N = int(input())
initial_state = list(map(int, list(input().rstrip())))
final_state = list(map(int, list(input().rstrip())))

def flipFirstBulb(i_state, f_state):
    i_state[0] = (i_state[0] + 1) % 2
    i_state[1] = (i_state[1] + 1) % 2
    switch_click_cnt = 1
    
    for i in range(1, N):
        if i_state[i-1]==f_state[i-1]: continue
        
        if i!=N-1:
            for idx in [i-1, i, i+1]:
                i_state[idx] = (i_state[idx] + 1) % 2
            switch_click_cnt += 1
        else:
            for idx in [i-1, i]:
                i_state[idx] = (i_state[idx] + 1) % 2
            switch_click_cnt += 1 
    
    if i_state[-1]==f_state[-1]: return switch_click_cnt
    else: return float('inf')
    
def notFlipFirstBulb(i_state, f_state):
    switch_click_cnt = 0
    
    for i in range(1, N):
        if i_state[i-1]==f_state[i-1]: continue
        
        if i!=N-1:
            for idx in [i-1, i, i+1]:
                i_state[idx] = (i_state[idx] + 1) % 2
            switch_click_cnt += 1
        else:
            for idx in [i-1, i]:
                i_state[idx] = (i_state[idx] + 1) % 2
            switch_click_cnt += 1   
    
    if i_state[-1]==f_state[-1]: return switch_click_cnt
    else: return float('inf')

i_state_1 = copy.deepcopy(initial_state)
i_state_2 = copy.deepcopy(initial_state)    
case1 = flipFirstBulb(i_state_1, final_state)
case2 = notFlipFirstBulb(i_state_2, final_state)

result = min(case1, case2)

if result==float('inf'): print(-1)
else: print(result)