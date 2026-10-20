# 仅打包网站和必要源码，并验证压缩包与匿名版本。
from pathlib import Path
import json
import zipfile
root = Path(__file__).resolve().parent.parent
out = root / 'delivery'
team = json.loads((out / 'package-metadata.json').read_text(encoding='utf-8'))
formal = team['formal']
prefix = f"2026-{team['group']}-{team['team']}-{team['leader']}" if formal else '纹脉百工录'
names = [f"{prefix}-{'完整版本' if formal else '完整预览版'}.zip", f"{prefix}-{'匿名版本' if formal else '匿名预览版'}.zip"]
for anonymous, name in enumerate(names):
    with zipfile.ZipFile(out / name, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for file in (root / 'dist').rglob('*'):
            if file.is_file():
                archive.write(file, file.relative_to(root / 'dist').as_posix())
        for item in ['README.md', 'DESIGN.md', 'package.json', 'package-lock.json', '启动预览.cmd']:
            archive.write(root / item, item)
        for file in (root / 'scripts').glob('*'):
            if file.is_file():
                archive.write(file, file.relative_to(root).as_posix())
        archive.write(root / 'docs/IMAGE_PROMPT.md', 'docs/IMAGE_PROMPT.md')
        if not anonymous:
            archive.write(root / 'assets/img/celadon-still-life-source.png', 'assets/img/celadon-still-life-source.png')
            archive.writestr('docs/team.json', json.dumps({key: value for key, value in team.items() if key != 'formal'}, ensure_ascii=False, indent=2))
    with zipfile.ZipFile(out / name) as archive:
        assert archive.testzip() is None
        assert 'index.html' in archive.namelist()
        assert all('node_modules' not in item and '.git/' not in item for item in archive.namelist())
        if anonymous:
            assert 'docs/team.json' not in archive.namelist()
outer = f"{team['group']}-{team['team']}-{team['leader']}.zip" if formal else '纹脉百工录-本地交付总包.zip'
with zipfile.ZipFile(out / outer, 'w', zipfile.ZIP_DEFLATED) as archive:
    for name in names:
        archive.write(out / name, name)
with zipfile.ZipFile(out / outer) as archive:
    assert archive.testzip() is None
print('压缩包校验通过：' + '、'.join(names + [outer]))
