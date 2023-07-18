def g_range(anfang,ende):
    while anfang<ende:
        yield anfang
        anfang+=1

g=g_range(6,12)
print(next(g))
g.close()
print(next(g))

