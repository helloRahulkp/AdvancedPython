def feb():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
for i in feb():
    if i > 100:
            break
    print(i)