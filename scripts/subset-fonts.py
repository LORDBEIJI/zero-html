# 裁剪本地页面字体，页面文字不离开工作区。
from pathlib import Path
from fontTools import subset
from fontTools.ttLib import TTFont
import re
root = Path(__file__).resolve().parent.parent
texts = []
for folder, suffix in [(root, '*.html'), (root / 'craft', '*.html'), (root / 'src/content', '*.js')]:
    for file in folder.glob(suffix):
        texts.append(file.read_text(encoding='utf-8'))
chars = ''.join(sorted(set(re.findall(r'[\u3400-\u9fff\u3000-\u303f\uff00-\uffef]', ''.join(texts)))))
font = TTFont(root / '.tooling/fonts/NotoSerifSC.ttf')
options = subset.Options()
options.flavor = 'woff2'
subsetter = subset.Subsetter(options=options)
subsetter.populate(text=chars)
subsetter.subset(font)
font.flavor = 'woff2'
font.save(root / 'assets/fonts/wenmai-serif.woff2')
print(f'本地宋体子集已生成，含 {len(chars)} 字。')
