def rabin(pat, txt, prime):
    plen = len(pat)
    tlen = len(txt)
    hash = 1
    htxt = 0
    hpat = 0
    p1 = 0
    j=0
    for i in range(plen - 1):
        hash = (hash* 256) % prime  # 256-no of characters

    for i in range(plen):
        hpat = (256 * hpat + ord(pat[i])) % prime
        htxt = (256 * htxt + ord(txt[i])) % prime

    for i in range(tlen - plen + 1):
        if hpat == htxt:
            for j in range(plen):
                if txt[i + j] != pat[j]:
                    break
        j+=1
        if j == plen:
            print("pattern found at", i)

        if i < (tlen - plen):
            htxt = (256 * (hpat - ord(txt[i]) * hash) + ord(txt[i + plen])) % prime
            if htxt < 0:
                htxt = (htxt + prime)


rabin("ritu", "riuosritunfdn", 105)
