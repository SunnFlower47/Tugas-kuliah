def cetak_kelipatan():
    for i in range(1, 21):
        if i % 4 == 0 and i % 5 == 0:
            print(f"{i} adalah Kelipatan 4 dan 5")
        elif i % 4 == 0:
            print(f"{i} adalah Kelipatan 4")
        elif i % 5 == 0:
            print(f"{i} adalah Kelipatan 5")
        else:
            print(i)
cetak_kelipatan()
