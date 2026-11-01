import json
with open('effectiveness.json') as json_file:
    data = json.load(json_file)

def remake_chart():
    global data
    strength_to_num={"super effective":2, "normal effective":1, "not very effective": 0.5, "no effect":0}
    data_changed = {}

    for strength in data:
        for attacker in data[strength]:
            if attacker not in data_changed.keys():
                data_changed[attacker] = {}
            for defender in data[strength][attacker]:
                data_changed[attacker][defender] = strength_to_num[strength]
    return data_changed

attackfield = remake_chart()
def attack(N1, N2, listpok):
    pokemoni = listpok.split(",")
    team1 = pokemoni[:N1]
    team2 = pokemoni[N1:N1 + N2]
    sila1 = 0
    sila2 = 0

    for pokemoni1 in team1:
        typy1 = pokemoni1.strip().split()
        for pokemoni2 in team2:
            typy2 = pokemoni2.strip().split()
            sila = 0
            for t1 in typy1:
                faktor = 1
                for t2 in typy2:
                    faktor *= attackfield[t1][t2]
                if faktor > sila:
                    sila = faktor
            sila1 += sila

    for pokemoni1 in team2:
        typy1 = pokemoni1.strip().split()
        for pokemoni2 in team1:
            typy2 = pokemoni2.strip().split()
            sila = 0
            for t1 in typy1:
                faktor = 1
                for t2 in typy2:
                    faktor *= attackfield[t1][t2]
                if faktor > sila:
                    sila = faktor
            sila2 += sila
            
    if sila1 > sila2:
        vitaz = "ME"
    elif sila2 > sila1:
        vitaz = "FOE"
    else:
        vitaz = "EQUAL"

    return round(sila1, 1), round(sila2, 1), vitaz
print(attack(2, 6, "Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))