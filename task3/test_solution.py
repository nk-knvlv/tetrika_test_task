import csv


def write_dict_into_csv(target_dict: dict, filename: str):
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for name in target_dict:
            writer.writerow([target_dict[name]])


animals = {'A': 213, 'B': 3245}

write_dict_into_csv(animals, 'beasts2.csv')
