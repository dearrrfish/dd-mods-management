import csv
import logging
import os
import re
import sys
from argparse import ArgumentParser
from subprocess import call

is_win = False
if sys.platform.startswith("win"):
    is_win = True


def copyWithSubprocess(src, dest):
    cmd = ["robocopy", src, dest, "/E"] if is_win else ["cp", "-r", src, dest]
    print("copy: ", dest)
    call(cmd)


def delWithSubprocess(path):
    print("del: ", path)
    cmd = ["rd", "/S", "/Q", path] if is_win else ["rm", "-r", path]
    call(cmd, shell=is_win)


# Define needed CSV field names
F_XID = "XID"
F_PROJECT_NAME = "项目名"

# Prepare arguments
N_ARGV = len(sys.argv)
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

parser = ArgumentParser()
parser.add_argument(
    "--csv",
    default="./ddm_mods_list.csv",
    help="Exported CSV format list of included mods. Default to `./ddm_mods_list.csv`",
)
parser.add_argument(
    "--src",
    default=os.path.join(SCRIPT_PATH, "all_mods"),
    help="Path to source location of all mods. Default to script location/all_mods",
)
parser.add_argument(
    "--out",
    default=os.path.join(SCRIPT_PATH, "mods"),
    help="Path to output location of all mods, eg. the game folder. Default to script location/mods",
)
# parser.add_argument(
#     "--merge",
#     default="0",
#     help="Mode to merge mod files. 0 (default) - don't merge; 1 - merge all into one; 2 - merge by priority groups; 1p/2p - merge and keep unmerged copy",
# )
args = parser.parse_args()

csvfile_path = args.csv
mods_src_path = args.src
mods_out_path = args.out
# merge_mode = int(args.merge)

if not os.path.isfile(csvfile_path):
    logging.error("ERROR: mods list csv was not provided - %s", csvfile_path)
    sys.exit(1)

if not os.path.isdir(mods_src_path):
    logging.error("ERROR: mods source folder does not exist. - %s", mods_src_path)
    sys.exit(1)

# if merge_mode not in [0, 1, 2]:
#     logging.error("ERROR: unknown merge mode. - %d", merge_mode)
#     sys.exit(1)

# Create output folder if not exist
os.makedirs(mods_out_path, exist_ok=True)

# Process csv file
count = 1
mods = {}
with open(csvfile_path, encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ord = str(count).zfill(3)
        xid = row[F_XID]
        mods[xid] = {
            "ord": ord,
            "projectName": row[F_PROJECT_NAME],
        }
        count += 1


# Scan and compare with old mods folder
mods_exists = []
old_mods_dirs = [d.name for d in os.scandir(mods_out_path) if d.is_dir()]
for od in old_mods_dirs:
    old_path = os.path.join(mods_out_path, od)
    _, xid = od.split("_", 1)
    if xid in mods:
        new_path = os.path.join(mods_out_path, f"{mods[xid]['ord']}_{xid}")
        mods_exists.append(xid)
        if old_path != new_path:
            print("rename: ", new_path)
            os.rename(old_path, new_path)
        else:
            print("exists: ", new_path)
    else:
        delWithSubprocess(old_path)

# Update project names in project.xml
for xid in [x for x in mods if x not in mods_exists]:
    mod = mods[xid]

    src_path = os.path.join(mods_src_path, xid)
    if not os.path.isdir(src_path):
        logging.error("ERROR: target mod folder does not exist. - %s", src_path)
        sys.exit(1)

    project_file = os.path.join(src_path, "project.xml")
    if not os.path.isfile(project_file):
        logging.error("ERROR: target project file does not exist. - %s", project_file)
        sys.exit(1)

    project_file_bak = os.path.join(project_file) + ".bak"

    if not os.path.exists(project_file_bak):
        os.rename(project_file, project_file_bak)

    with open(project_file, "w", encoding="utf8") as out:
        with open(project_file_bak, "r", encoding="utf8") as src:
            content = src.read()
            content_new = re.sub(
                "<Title>[^<]*</Title>",
                f"<Title>{mod['projectName']}</Title>",
                content,
                flags=re.M,
            )
            out.write(content_new)

    copyWithSubprocess(src_path, os.path.join(mods_out_path, f"{mod['ord']}_{xid}"))
