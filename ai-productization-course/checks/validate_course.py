#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
import re, sys
ROOT = Path(__file__).resolve().parents[1]
required = [
 'index.html','README.md','package.json','assets/style.css','assets/slide.js','assets/diagrams.css',
 *[f'slides/{i:02d}-{name}.html' for i,name in enumerate(['overview','llm-app-and-rag','rag-retrieval-design','rag-generation-design','rag-evaluation','llmops-and-production','case-study-ocr-to-rag','final-exercises'])]
]
for rel in required:
    if not (ROOT/rel).exists():
        print(f'MISSING: {rel}'); sys.exit(1)
class LinkParser(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        for k,v in attrs:
            if k in {'href','src'} and v and not re.match(r'^(https?:|mailto:|#)', v): self.links.append(v)
def fail(msg): print(msg); sys.exit(1)
for html in (ROOT/'slides').glob('*.html'):
    text=html.read_text(encoding='utf-8')
    if len(re.findall(r"class=['\"][^'\"]*slide", text)) < 8: fail(f'NOT_ENOUGH_SLIDES: {html.name}')
    for word in ['学習ゴール','まとめ','確認問題']:
        if word not in text: fail(f'MISSING_{word}: {html.name}')
for p in [ROOT/'index.html', *sorted((ROOT/'slides').glob('*.html'))]:
    parser=LinkParser(); parser.feed(p.read_text(encoding='utf-8'))
    for link in parser.links:
        target=(p.parent/link.split('#')[0]).resolve()
        if link.split('#')[0] and not target.exists(): fail(f'BROKEN_LINK: {p.relative_to(ROOT)} -> {link}')
idx=(ROOT/'index.html').read_text(encoding='utf-8')
for html in sorted((ROOT/'slides').glob('*.html')):
    if f"slides/{html.name}" not in idx: fail(f'INDEX_MISSING_LINK: {html.name}')
if len(list((ROOT/'exercises').glob('*.md'))) < 3: fail('NOT_ENOUGH_EXERCISES')
bad=re.compile('|'.join(['TO'+'DO','FIX'+'ME','仮'+'置き','lorem'+' ipsum']), re.I)
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.html','.css','.js','.md','.py','.json'}:
        if bad.search(p.read_text(encoding='utf-8')): fail(f'PLACEHOLDER_FOUND: {p.relative_to(ROOT)}')
print('GOAL ACHIEVED: AI productization course is complete.')
