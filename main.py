def task():
    players = [19, 19, 26, 25, 20, 18, 30, 24, 27]
    find_medium_year = 0
    step = 0
    find_young_year = players[0]

    for el in players:
        find_medium_year += el
        step += 1

    result = find_medium_year / step
    print('Середній вік ', result)

    for el in players:
        if el < find_young_year:
            find_young_year = el
    print('Наймолодший вік ', find_young_year)
    print('Сума Наймолодшого і Найстаршого ', find_young_year + result)

print(task())