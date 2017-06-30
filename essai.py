from collections import defaultdict
from tabulate import tabulate
from prettytable import PrettyTable

def essai():
    print('Essai')

    essai_lst = [{'name': 'guillaume', 'id': 150}, {'name': 'ben','id': 180},\
                 {'name': 'guillaume', 'id': 180}]


    print(essai_lst)

    name_dict = defaultdict(list)
    nb_dict = defaultdict(int)

    for dc in essai_lst:
        name_dict[dc['name']].append(str(dc['id']))
        nb_dict[dc['name']] += 1

    name_lst = list(nb_dict.keys())



    table = PrettyTable(['Name','Bugs'])
    table_2 = PrettyTable(['Name', 'Bugs lists'])
    table_3 = PrettyTable(['Name','# Bugs', 'Bugs lists'])

    for name in name_lst:
        table.add_row([name,nb_dict[name]])
        table_2.add_row([name, ','.join(name_dict[name])])
        table_3.add_row([name, nb_dict[name],','.join(name_dict[name])])

    print(table)
    print(table_2)
    print(table_3)


    tables_txt = [table.get_string(), table_2.get_string(),table_3.get_string()]

    file = open('report.txt', 'w')

    for txt in tables_txt:
        file.write(txt)
        file.write('\n')


    file.close()

if __name__ == "__main__":
    essai()