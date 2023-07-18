def neu_range(anfang,ende):
    L=[]
    while anfang<ende:
        L.append(anfang)
        anfang+=1
    yield L

neuRange=neu_range(10,16)
print(next(neuRange))