def g_range(anfang,ende):
    while anfang<ende:
        yield anfang
        print("Hallo")
        anfang+=1

for i in g_range(20,31):
    print(i)

mein_generator=g_range(20,26)
print(next(mein_generator))
print(next(mein_generator))