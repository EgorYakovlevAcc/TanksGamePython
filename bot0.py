def move(me, enemies, bullets, bonuses, m):
    if me['pos'][1] < 600:
        m.down()

    m.shot(400, 300)