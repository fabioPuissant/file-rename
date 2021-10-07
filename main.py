from os.path import expanduser
from pathlib import Path
import os

user = os.getlogin()
home = expanduser("~")
target = os.path.join(home, 'test')


def rename_files(target_dir: str):
    for path in Path(target_dir).glob('*.pdf'):
        file_split = path.name.split('_')
        file = file_split[1] + '_' + file_split[-1]
        file = file[:-4] + '_' + file_split[0] + '.pdf'
        file = str(file[0]).upper() + file[1:]
        file_split = file.split('-')
        file_split[1] = file_split[1][0].upper() + file_split[1][1:]
        file = file_split[0] + '-' + file_split[1] + '-' + file_split[2]
        src = os.path.join(target_dir, path)
        dest = os.path.join(target_dir, file)
        os.rename(src, dest)


rename_files(target_dir=target)
for dire in os.walk(target):
    print(dire)
