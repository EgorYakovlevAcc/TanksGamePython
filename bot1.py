from sympy.strategies.core import switch

n = 0
k = 0

def move(me, enemies, bullets, bonuses, m):

    global n
    n = n + 1

    if (n // 100) % 4 == 0:
        m.left()

    if (n // 100) % 4 == 1:
        m.up()

    if (n // 100) % 4 == 2:
        m.right()

    if (n // 100) % 4 == 3:
        m.down()

    m.shot(enemies[0]['pos'][0], enemies[0]['pos'][1])