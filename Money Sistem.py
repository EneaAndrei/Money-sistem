P = int(input())
def findMin(V):


    Bancnote = [1, 5, 10, 50,
            100, 200, 500]
    n = len(Bancnote)


    ans = []


    i = n - 1
    while(i >= 0):


        while (V >= Bancnote[i]):
            V -= Bancnote[i]
            ans.append(Bancnote[i])

        i -= 1


    for i in range(len(ans)):
        print(ans[i], end = " ")


if __name__ == '__main__':
    n = P

    print("Avem nevoie de următoarele bancnote pentru",
           n, ": ", end = "")
    findMin(n)

    import sys

def minBanc(Banc, m, V):

    table = [0 for i in range(V + 1)]

    table[0] = 0

    for i in range(1, V + 1):
        table[i] = sys.maxsize

    for i in range(1, V + 1):

        for j in range(m):
            if (Banc[j] <= i):
                sub_res = table[i - Banc[j]]
                if (sub_res != sys.maxsize and
                    sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    if table[V] == sys.maxsize:
        return -1

    return table[V]

if __name__ == "__main__":

    Bancnote = [1, 5, 10, 50,
            100, 200, 500]
    m = len(Bancnote)
    V = P
    print("iar numărul minim de bancnote este:",
                 minBanc(Bancnote, m, V))
