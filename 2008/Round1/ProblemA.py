__author__ = 'Peihong'

if __name__ == "__main__":
    f = open('A-large-practice.in', 'r')
    fout = open('A-large-result.out', 'w')
    cases = int(f.readline())
    for i in range(cases):
        n = int(f.readline())
        a = map(int, f.readline().split())
        b = map(int, f.readline().split())

        a = sorted(a, lambda x, y: x-y)
        b = sorted(b, lambda x, y: y-x)
        c = zip(a, b)
        d = map(lambda (x, y): x*y, c)
        res = reduce(lambda x, y: x+y, d, 0)
        print 'Case #%d: %d' % (i+1, res)
        fout.write('Case #%d: %d\n' % (i+1, res))
    f.close()
    fout.close()
