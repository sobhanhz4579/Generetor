
def g_range(anfang,ende):
    while anfang<ende:
        yield anfang
        anfang+=1

g=g_range(10,34)

for i in g:
    if i==14:
        g.throw(ValueError("Error"))
    print(i)