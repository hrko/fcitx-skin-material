# Run the following command in this folder to generate the set of ime icons.
# Dependencies: parallel, inkscape

parallel 'cp pinyin.svg {1}.svg; sed s/拼/{2}/g -i {1}.svg; inkscape -d 96 -e {1}.png {1}.svg' :::: ime_names.txt ::::+ ime_icon_letters.txt
