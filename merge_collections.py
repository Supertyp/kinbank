import glob
import os
from shutil import move
from pathlib import Path
import pandas as pd

def new_path(path):
    return("/".join(Path(path).parts[2:]))

print(new_path("collections/kinura/kinbank/raw/Uralic/Finnish_finn1318.csv"))

def move_files(filenames):
    new_filenames =  ['./' + new_path(f) for f in filenames]
    for old, new in zip(filenames, new_filenames):
        print(old + "  " + os.path.dirname(new))
        if not os.path.isdir(os.path.dirname(new)):
            Path(os.path.dirname(new)).mkdir(parents=True, exist_ok=True)
        move(old, new)

## Varikin
print("Copying Varikin")
varikin_files = glob.glob("collections/varikin/kinbank/raw/**/*.csv", recursive=True)
move_files(varikin_files)

## Parabank
print("Copying Parabank")
parabank_files = glob.glob("collections/parabank/kinbank/raw/**/*.csv", recursive=True)
move_files(parabank_files)

## Goeldi
print("Copying Goeldi")
goeldi_files = glob.glob("collections/goeldi/kinbank/raw/**/*.csv", recursive=True)
move_files(goeldi_files)

## Kinura
print("Copying Kinura")
kinura_files = glob.glob("collections/kinura/kinbank/raw/**/*.csv", recursive=True)
move_files(kinura_files)

### Combine metadata
all_filenames = [
    "collections/varikin/kinbank/etc/languages.csv",
    "collections/parabank/kinbank/etc/languages.csv",
    "collections/kinura/kinbank/etc/languages.csv",
    "collections/goeldi/kinbank/etc/languages.csv",
]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv("kinbank/etc/languages.csv", index=False, encoding='utf-8-sig')