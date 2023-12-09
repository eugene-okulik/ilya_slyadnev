temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

hot_day = list(filter(lambda temp: temp > 28, temperatures))

if hot_day:
    high_t = max(hot_day)
    low_t = min(hot_day)
    mid_t = sum(hot_day) / len(hot_day)

    print(f'Самая высока температура: {high_t}')
    print(f'Самая низкая температура: {low_t}')
    print(f'Средняя температура: {mid_t}')
