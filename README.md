# Darkest Dungeon Mod Management

## Requirements

- Python3
- Linux/Windows

## Usage

### Maintain a mod list

- Create and maintain a CSV with:
    - at least two required columns:
        - `XID` - folder name of mod files. e.g. steam_1234567, nexus_12345, custom_101
        - `项目名` - mod project name to display.
    - first line as header of column names
    - ordered by loading priority

```csv
项目名,XID
[A3:通用本地化] 女性化人物名,steam_2799235099
[A3:通用本地化] 怪物技能图鉴（完全版）,steam_3189357943

```

- (Optional) Duplicate from my [Notion page](https://dearrrfish.notion.site/97c86daab96c40e98639bcdd9da85d28?v=ccb0aed20f3c44c382f4cd279f4769e1)

    - Export for CSV dump of the mods to be included
    - Make sure required fields `XID`, `项目名` are exported.

### Maintain local mod files

- Download mods and rename the folder to `XID` value in the CSV file
- Put all mods in same folder as library source. By default, the script prefers a `all_mods` folder in script location

### Run script to generate `mods` collection

`main.py`

#### Parameters:

- `--csv`: CSV file location. Defaults to `./ddm_mods_list.csv`
- `--src`: Path to the location of all mods. Defaults to `<SCRIPT_PATH>/all_mods`
- `--out`: Path to output folder. Defaults to `<SCRIPT_PATH>/mods`

#### Example runs:

```bash

# quick run with default parameters:
python3 main.py

# above command equals to:
python3 main.py --csv ./ddm_mods_list.csv --src ./all_mods --out ./mods

# update `mods` in the game folder directly
python3 main.py --out <to-steam-folder>/DarkestDungeon/mods

```
