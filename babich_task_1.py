duration = int(input('Введите продолжительность времени в секундах'))
if duration < 60:
    print(duration, 'сек.')
elif 60 <= duration < 3600:
    min = duration // 60
    sec = duration % 60
    print(min, 'мин.', sec, 'сек.')
elif 3600 <= duration < 86400:
    h = duration // 3600
    min = (duration % 3600) // 60
    sec = (duration % 3600) % 60
    print(h, 'ч.', min, 'мин.', sec, 'сек')
elif 86400 <= duration:
    day = duration // 86400
    h = (duration % 86400) // 3600
    min = ((duration % 86400) % 3600) // 60
    sec = ((duration % 86400) % 3600) % 60
    print(day, 'д.', h, 'ч.', min, 'мин.', sec, 'сек')
