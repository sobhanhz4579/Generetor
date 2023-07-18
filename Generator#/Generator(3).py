def g_rrange2():
    nummer=6
    yield nummer
    nummer+=1
    yield nummer
    nummer+=2
    yield nummer

mein_generator=g_rrange2()
print(next(mein_generator))
print(next(mein_generator))
print(next(mein_generator))
print(next(mein_generator))