import sys

input = sys.stdin.readline

T = int(input())
for test_case in range(1, T+1):
    # 배열 크기 / 프로그램 코드 크기 / 입력의 크기
    sm, sc, si = map(int, input().split())
    array = [0 for _ in range(sm)]
    code = list(input().rstrip())
    ipt = list(input().rstrip())
    
    # 배열 한 칸에 들어가는 정수의 범위 0 ~ 255
    # 만약 0에서 1 감소되어 -1이 된다면 255로 변환되어야 한다.
    # 255에서 1 증가되어 256이 된다면 0으로 변환되어야 한다.
    
    bracket = {}
    idx = 0
    stack = []
    while idx < sc:
        if code[idx] == "[":
            stack.append(idx)
        elif code[idx] == "]":
            open, close = stack.pop(), idx
            bracket[open] = close
            bracket[close] = open
        idx += 1
    
    ptr = 0
    code_ptr = 0
    ipt_ptr = 0
    output = []
    
    isLoop = False
    loop = float('inf')
    cnt = 0
    while code_ptr<len(code):
        cnt += 1
        if code[code_ptr]=='-':
            array[ptr] = (array[ptr] - 1) % 256
        elif code[code_ptr]=='+':
            array[ptr] = (array[ptr] + 1) % 256
        elif code[code_ptr]=='<':
            ptr = (ptr - 1) % sm
        elif code[code_ptr]=='>':
            ptr = (ptr + 1) % sm
        elif code[code_ptr]=='.':
            output.append(array[ptr])
        elif code[code_ptr]==',':
            if ipt_ptr==len(ipt):
                array[ptr] = 255
            else:
                array[ptr] = ord(ipt[ipt_ptr])
                ipt_ptr += 1
        elif code[code_ptr]=='[':
            if array[ptr]==0:
                code_ptr = bracket[code_ptr] # jump to ']'
        elif code[code_ptr]==']':
            if array[ptr]!=0:
                code_ptr = bracket[code_ptr] # jump to '['

        if cnt>50000000:
            loop = min(loop, code_ptr)

        code_ptr += 1
        
        if cnt>2*50000000: # '무한루프 구간' 중 '가장 바깥' bracket pair를 출력해야 되기 때문에
            print("Loops", loop, bracket[loop])
            isLoop = True
            break
        
         
    if not isLoop:
        print("Terminates")