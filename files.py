import os


files_data = []
for item in ['1.txt', '2.txt', '3.txt']:
    with open(os.path.join(os.getcwd(), item), 'rt', encoding='utf-8') as file:
        data = file.readlines()
        files_data.append([item + '\n', str(len(data)) + '\n', data])

files_data.sort(key=lambda i: i[1])

with open(os.path.join(os.getcwd(), 'merged_files.txt'), 'wt', encoding='utf-8') as file:
    for item in files_data:
        file.writelines([item[0], item[1]])
        file.writelines(item[2])
        file.write('\n')