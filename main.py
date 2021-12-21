'''
Program zwraca informację o tygodniu podanego roku, zgodnie z iso.

Próbowałam w nim wykorzystać jak namniej metod datetime
'''

from datetime import date

print('Który mamy rok? (np. 2021)')
UY = input()

print('Jaki mamy miesiąc? (np. 12)')
UM = input()

print('Jaki mamy dzień? (np. 09)')
UD = input()

A = int(UY)
B = int(UM)
C = int(UD)


def doy(Y,M,D):
    """ DOY - dzień roku """
    if is_leap_year(Y):
        K = 1
    else:
        K = 2
    N = int((275 * M) / 9) - K * int((M + 9) / 12) + D - 30
    return N

def is_leap_year(year):
    """ jeśli przestępne TRUE """
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


doy1 = doy(A, B, C)
iso_date = ((10 + doy1) - date(A, B, C).isoweekday())/7
print(int(iso_date))
