PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_price_list = dict(map(lambda x: (x.split()[0], int(x.split()[1][:-1])), PRICE_LIST.split('\n')))
print(new_price_list)
