n = 0

def checkBorder (x, y):
    if (x > 100) and (x < 500):
        if (y > 100) and (y < 500):
            n = n + 100
    else:
        n = n + 100


def move(me, enemies, bullets, bonuses, m):

    global n
    n = n + 1

    if bonuses:
        m.dir(bonuses[0]['pos'][0] - me['pos'][0], bonuses[0]['pos'][1] - me['pos'][1])

    else:

        if (n // 100) % 4 == 0:
            m.left()

        if (n // 100) % 4 == 1:
            m.up()

        if (n // 100) % 4 == 2:
            m.right()

        if (n // 100) % 4 == 3:
            m.down()

    m.shot(enemies[0]['pos'][0], enemies[0]['pos'][1])