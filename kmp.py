


def kmp(pat, txt):
    plen = len(pat)
    tlen = len(txt)
    lps = [0] * plen
    ti = 0
    pindex = 0
    lps1(pat, plen, lps)
    for i in range(tlen):
        if pat[pindex] == txt[ti]:
            pindex += 1
            ti += 1
        if pindex == plen:
            print("pattern found at" + str(ti - pindex))
            pindex = lps[pindex - 1]
        elif ti < tlen and pat[pindex] != txt[ti]:
            if pindex:
                pindex = lps[pindex - 1]
            else:
                ti += 1

def lps1(pat, plen, lps):
    i = 1
    len = 0

    while i < plen:
        if pat[i] == pat[len]:
            len += 1
            i += 1
            lps[i] = len
        else:
            if len:
                len = lps[len - 1]
            else:
                i += 1



kmp("ritu", "ritupraritu")
