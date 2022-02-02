import random

def sonni_top_user(x):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar+=1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Kattaroq son ayting:", end="")
        elif taxmin > tasodifiy_son:
            print("Kichikroq son ayting:", end="")
        else:
            print("Yutdingiz!")
            break
    print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar

def sonnitop_komp(x):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(
            f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
            f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
        )

        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x):
    is_continue = True

    while is_continue:
        taxminlar_komp = sonnitop_komp(x)
        taxminlar_user = sonni_top_user(x)
        if taxminlar_user < taxminlar_komp:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        elif taxminlar_user > taxminlar_komp:
            print(f"Men {taxminlar_komp} taxmin bilan topdim va yutdim!")
        else:
            print("Durrang")
        is_continue = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
