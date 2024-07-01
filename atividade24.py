# The program is going to return "true" if the first city's name be "Santo"

city = str(input('Em qual cidade você nasceu? ')).strip()
print(city[:5].upper() == 'SANTO')