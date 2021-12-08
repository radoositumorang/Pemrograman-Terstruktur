from datetime import *


def diffDate(x):
    skrg = datetime.date(datetime.now())
    wn = datetime.strptime(x, "%Y-%m-%d").date()
    waktu = (wn-skrg)
    print(waktu.days)


diffDate("2021-12-26")
