# Darkest Dungeon 模组管理

## 需求

- Python3
- Linux/Windows

## 使用方法

### 维护模组列表

- 创建 CSV 格式的模组列表，满足以下条件：
    - 至少包含以下两列信息：
        - `XID` - 作为模组文件夹名称。比如 steam_1234567, nexus_12345, custom_101
        - `项目名` - 作为模组名称显示
    - 第一行为表头
    - 按照模组加载顺序排列

```csv
项目名,XID
[A3:通用本地化] 女性化人物名,steam_2799235099
[A3:通用本地化] 怪物技能图鉴（完全版）,steam_3189357943

```

- （可选）克隆我的 [Notion 数据库](https://www.notion.so/dearrrfish/97c86daab96c40e98639bcdd9da85d28)。 编辑后，导出想要使用的模组视图到 CSV

### 维护本地模组源文件

- 下载模组并以 `XID` 重命名文件夹为
- 把所有模组放在同一父文件夹内。默认使用程序目录下 `./all_mods`

### 运行 main.py 生成或更新 `mods` 文件夹

`python3 main.py`

#### 可用参数

- `--csv`: CSV 文件名。默认值：`./ddm_mods_list.csv`
- `--src`: 模组库源路径。默认值：`<SCRIPT_PATH>/all_mods`
- `--out`: 生成路径。默认值：`<SCRIPT_PATH>/mods`

#### 示例

```bash

# 使用默认参数
python3 main.py

# 以上命令相当于：
python3 main.py --csv ./ddm_mods_list.csv --src ./all_mods --out ./mods

# 直接写入游戏目录：
python3 main.py --out <to-steam-folder>/DarkestDungeon/mods
```

#### 示例输出日志

```
PS E:\Mods\DarkestDungeon> python.exe .\main.py --out E:\SteamLibrary\steamapps\common\DarkestDungeon\mods
exists:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\001_steam_2799235099
exists:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\002_steam_3189357943
exists:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\003_steam_3222492353
exists:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\004_steam_3200615686
del:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\005_steam_3173467642
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\011_steam_3215254893
del:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\007_steam_2578065886
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\013_steam_2129710534
del:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\009_steam_3173601015
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\014_steam_3242499472
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\005_steam_900123064
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\006_steam_1500516865
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\007_steam_2862945396
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\015_steam_3129401071
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\016_steam_3233535198
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\017_custom_111
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\018_steam_3112340555
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\019_steam_3270322755
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\020_steam_2614658199
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\021_steam_2979505704
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\022_steam_3012711092
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\023_steam_2632051966
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\024_steam_3209739352
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\025_steam_2991940788
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\026_custom_113
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\027_steam_2469408896
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\028_custom_114
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\029_steam_2537880572
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\030_steam_3214277340
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\031_steam_2070082784
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\032_steam_1624470590
rename:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\033_steam_2615711863
del:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\033_custom_109
del:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\034_custom_77
del:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\035_custom_78
exists:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\036_custom_82
exists:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\037_steam_1434609021
copy:  E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\008_steam_2862923606

-------------------------------------------------------------------------------
   ROBOCOPY     ::     Robust File Copy for Windows
-------------------------------------------------------------------------------

  Started : Thursday, July 18, 2024 3:46:35 PM
   Source : E:\Mods\DarkestDungeon\all_mods\steam_2862923606\
     Dest : E:\SteamLibrary\steamapps\common\DarkestDungeon\mods\008_steam_2862923606\

    Files : *.*

  Options : *.* /S /E /DCOPY:DA /COPY:DAT /R:1000000 /W:30

------------------------------------------------------------------------------

          New Dir          4    E:\Mods\DarkestDungeon\all_mods\steam_2862923606\
100%        New File                 715        modfiles.txt
100%        New File              131501        preview_icon.png
100%        New File                 671        project.xml
100%        New File                 655        project.xml.bak
```
