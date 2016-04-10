def solve(K, C, S):
    if K > 1 and S < 2:
        return []

    half = K / 2
    return [half+1, (K**C-1)-(half+1)]

if __name__ == '__main__':
    T = int(raw_input())

    for i in range(T):
        K, C, S = map(int, raw_input().split())
        ans = solve(K, C, S)
        if ans:
            print 'Case #%d: %s' % (i+1, ' '.join([str(x) for x in ans]))
        else:
            print 'Case #%d: IMPOSSIBLE' % (i+1)