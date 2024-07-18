#!/usr/bin/env bash

game_folder=$1

src="${game_folder}/mods.bak"
out="${game_folder}/mods/all_in_one"
extra="${game_folder}/mods.extra"

[ -d "$out" ] && rm -r $out
mkdir -p "$out"

ls -r "$src" | grep "^0" | xargs -i sh -c 'cp -rv '$src'/{}/* '$out'/'

sed -i 's/<Title>.*<\/Title>/<Title>All In One<\/Title>/' "$out/project.xml"

rm "$out/modfiles.txt"
find $out -type f \( -name \*.psd -o -name \*.bak -o -name \*.zip \) | xargs -i sh -c 'rm {}'
find $out -type d -regex '^_.*' | xargs -i sh -c 'rm -r {}'
