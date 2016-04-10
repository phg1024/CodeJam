__author__ = 'Peihong'

if __name__ == "__main__":
    f = open('B-small-practice.in')
    fout = open('B-small-result.out')

    ncases = int(f.readline())
    for i in range(ncases):
        nflavors = int(f.readline())
        ncustomers = int(f.readline())

        