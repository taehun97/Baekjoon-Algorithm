import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

N, K = map(int, input().split())

# 다익스트라 알고리즘
def N_to_K(N, K):
    SSSP = [INF]*(100001)
    SSSP[N] = 0
    q = [(0, N)]
    
    while q:
        cnt_time, cnt_x = heapq.heappop(q)
        
        if cnt_time > SSSP[cnt_x]:
            continue
        
        # 0부터 100000까지의 모든 노드들은, 조건 범위 안에서
        # 자신의 -1, +1, *2의 인접 노드를 가짐
        # 그래서 제너레이터를 통해 직접 인접 노드를 구하여 순회하면 됨
        for adc_x, adc_time in [(cnt_x-1, 1), (cnt_x+1, 1), (2*cnt_x, 0)]:
            cal_time = cnt_time + adc_time
            
            # 인접 노드로 구한 값이 조건 범위 안에 있어야 함
            if 0 <= adc_x <= 100000 and cal_time < SSSP[adc_x]:
                SSSP[adc_x] = cal_time
                heapq.heappush(q, (cal_time, adc_x))
    
    return SSSP[K]

print(N_to_K(N, K))