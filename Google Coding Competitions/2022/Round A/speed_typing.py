for test in range(int(input())):
    I = input()
    P = input()
    N = len(I)
    M = len(P)
    p_index = 0
    i_index = 0
    
    while i_index < N and p_index < M:
        if I[i_index] == P[p_index]:
            i_index += 1
        p_index += 1
        
    if i_index == N:
        print("Case #{}: {}".format(test, M-N))
    else:
        print("Case #{}: IMPOSSIBLE".format(test))