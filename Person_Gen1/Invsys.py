def invsys():
    r = rdint(0,100)
    drugs = ["drug_x", "drug_y", "drug_z"]
    weapons = ["gun_a", "gun_b", "gun_c"]
    average = ["av_v", "av_d", "av_n"]

    illegal = []
    illegal.append(drugs[rdint(0,2)])
    illegal.append( weapons[rdint(0,2)])

    npcinventory = []

    if r <= 65:
        Illegal == True
        npcinventory.append(average[rdint(0,2)])
        npcinventory.append(illegal)
    else:
        for x in range(2):
            npcinventory.append(average[rdint(0,2)])
        Illegal == False