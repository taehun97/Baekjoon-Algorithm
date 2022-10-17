def findPairIndex(start_idx, c):
    flag = 0
    next_idx = start_idx + 1
    while True:
        if flag==0:
            if c[next_idx]==']':
                return next_idx + 1
            else: next_idx += 1
        else:
            if c[next_idx]=='[': flag += 1
            elif c[next_idx] ==']': flag -= 1
            else: next_idx += 1

def makeEightBit(bin):
    length = len(bin)
    if length<8:
        remain = 8 - length
        for _ in range(remain):
            bin = ['0'] + bin
            
    return bin

T = int(input())
for _ in range(T):
    sm, sc, si = map(int, input().split())
    code = input().rstrip()
    ipt = input().rstrip()
    
    code_idx = 0
    ipt_idx = 0
    mem_ptr = 0
    mem = [0 for _ in range(8 * sm)]
    visited = [False for _ in range(sc)]
    hasLoops = False
    left_bracket_idx_list = []
    right_bracket_idx_list = []
    lb = -1
    rb = -1
    
    while code_idx<len(code):
        if visited[code_idx]:
            hasLoops = True
            break
        
        visited[code_idx] = True
        
        if code[code_idx]=='-':
            bin_number = mem[mem_ptr:mem_ptr+8]   
            bin_number.reverse()
            int_number = int('0b' + ''.join(map(str, bin_number)), 2)
            int_number = (int_number - 1) % 256
            
            converted_bin_number = bin(int_number)[2:]
            converted_list = list(converted_bin_number)
            
            converted_list = makeEightBit(converted_list)
            
            converted_list.reverse()

            for i in range(8):
                mem[i + mem_ptr] = int(converted_list[i])    
        elif code[code_idx]=='+':
            bin_number = mem[mem_ptr:mem_ptr+8]
            bin_number.reverse()        
            int_number = int('0b' + ''.join(map(str, bin_number)), 2)
            int_number = (int_number + 1) % 256
            
            converted_bin_number = bin(int_number)[2:]
            converted_list = list(converted_bin_number)
            
            converted_list = makeEightBit(converted_list)
            
            converted_list.reverse()

            for i in range(8):
                mem[i + mem_ptr] = int(converted_list[i]) 
        elif code[code_idx]=='<':
            mem_ptr -= 8
        elif code[code_idx]=='>':
            mem_ptr += 8
        elif code[code_idx]=='[':
            left_bracket_idx_list.append(code_idx)
            
            bin_list = mem[mem_ptr:mem_ptr+8]
            bin_list.reverse()
            bin_string = '0b' + ''.join(map(str, bin_list))
            
            int_number = int(bin_string, 2)
            
            temp_idx = findPairIndex(code_idx, code)
            right_bracket_idx_list.append(temp_idx - 1)
            if int_number==0: # jump to ']' pair
                code_idx = temp_idx
                continue
        elif code[code_idx]==']':
            bin_list = mem[mem_ptr:mem_ptr+8]
            bin_list.reverse()
            bin_string = '0b' + ''.join(map(str, bin_list))
            
            int_number = int(bin_string, 2)
            if int_number!=0: # jump to '[' pair
                print(left_bracket_idx_list)
                print(right_bracket_idx_list)
                index = right_bracket_idx_list.index(code_idx)
                left_bracket_idx = left_bracket_idx_list[index]

                lb = left_bracket_idx
                rb = code_idx
                
                code_idx = left_bracket_idx + 1
                
                continue
        elif code[code_idx]=='.':
            bin_list = mem[mem_ptr:mem_ptr+8]
            bin_list.reverse()
            bin_string = '0b' + ''.join(map(str, bin_list))
            
            int_number = int(bin_string, 2)
            # print(int_number)
        elif code[code_idx]==',':
            if ipt_idx==si:
                for i in range(8):
                    mem[i + mem_ptr] = 1
            else:
                ipt_bin_string = bin(ord(ipt[ipt_idx]))[2:]
                ipt_bin_list = list(ipt_bin_string)
                
                ipt_bin_list = makeEightBit(ipt_bin_list)
                
                ipt_bin_list.reverse()
                
                for i in range(8):
                    mem[i + mem_ptr] = int(ipt_bin_list[i])
                    
                ipt_idx += 1
            
        code_idx += 1
        
    if hasLoops: print("Loops", lb, rb)
    else: print("Terminates")