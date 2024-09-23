for baris in range(7):
    for kolom in range(13):
        if (baris == 0 and (kolom in range(1, 4) or kolom in range(9, 12))) or \
           (baris == 1 and (kolom >= 0 and kolom <= 12)) or \
           (baris == 2 and (kolom >= 0 and kolom <= 12)) or \
           (baris == 3 and (kolom >= 2 and kolom <= 10)) or \
           (baris == 4 and (kolom >= 4 and kolom <= 8)) or \
           (baris == 5 and (kolom >= 5 and kolom <= 7)) or \
           (baris == 6 and kolom == 6):
            print("*", end="")
        else:
            print(" ", end="")
    print()
