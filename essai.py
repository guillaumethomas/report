from collections import defaultdict
from tabulate import tabulate
from prettytable import PrettyTable

def essai():
    print('Essai')

    essai_lst = [{'name':'guillaume', 'id':150},{'name':'ben','id':180},\
                 {'name': 'guillaume', 'id': 180}]


    print(essai_lst)

    name_dict = defaultdict(list)
    nb_dict = defaultdict(int)

    for dc in essai_lst:
        name_dict[dc['name']].append(dc['id'])
        nb_dict[dc['name']] += 1

    name_lst = list(nb_dict.keys())

    table = PrettyTable(['Name','Bugs'])
    for name in name_lst:
        table.add_row([name,nb_dict[name]])

    print(table)

    table_txt = table.get_string()

    file = open('report.txt', 'w')
    file.write(table_txt)
    file.close()

if __name__ == "__main__":
    essai()