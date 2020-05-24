import json
import subprocess
import tempfile
from pathlib import Path

svg_proto_path = Path("./prototype.svg")
svg_proto_str = svg_proto_path.read_text(encoding='utf_8')

tmpdir = tempfile.TemporaryDirectory()
tmpdir_path = Path(tmpdir.name)
outdir_path = Path('./png')
outdir_path.mkdir(exist_ok=True)

ime_list_path = Path("./ime_list.json")
ime_list_str = ime_list_path.read_text(encoding='utf_8')
ime_list = json.loads(ime_list_str)

for item in ime_list:
    print(item)
    svg_str = svg_proto_str.replace(
        'ime-char-placeholder', item['ime-char']).replace('font-family-placeholder', item['font-family'])

    svg_path = tmpdir_path / (item['ime-name'] + ".svg")
    svg_path.write_text(svg_str, encoding='utf_8')

    png_path = outdir_path / (item['ime-name'] + ".png")
    subprocess.run(['inkscape', '-d', '96', '-e', png_path, svg_path])
    pass

tmpdir.cleanup()
