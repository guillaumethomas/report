from collections import defaultdict

def essai():
    print('Essai')

    essai_lst = [{'name':'guillaume', 'id':150},{'name':'ben','id':180},\
                 {'name': 'guillaume', 'id': 180}]


    print(essai_lst)

    name_dict = defaultdict(list)

    for dc in essai_lst:
        name_dict[dc['name']].append(dc['id'])

    print(name_dict)



if __name__ == "__main__":
    essai()