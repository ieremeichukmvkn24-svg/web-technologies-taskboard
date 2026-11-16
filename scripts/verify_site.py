"""Прості автономні перевірки структури навчального TaskBoard.

Це не повноцінний W3C HTML validator і не тест інтерактивності в браузері.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
PAGES = [ROOT / 'index.html', ROOT / 'about.html', ROOT / 'docs' / 'links.html']

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.tags = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.tags.append(tag)
        if d.get('id'):
            self.ids.add(d['id'])
        for attr in ('href', 'src'):
            if attr in d:
                self.refs.append((tag, attr, d[attr]))


def check_page(path: Path):
    text = path.read_text('utf-8')
    doc = LinkParser()
    doc.feed(text)
    assert '<!doctype html>' in text.lower(), f'{path.name}: no DOCTYPE'
    assert 'lang="uk"' in text, f'{path.name}: missing Ukrainian lang'
    assert '<meta charset="UTF-8"' in text or '<meta charset="utf-8"' in text, f'{path.name}: missing UTF-8'
    for tag in ['header', 'nav', 'main', 'footer']:
        assert tag in doc.tags, f'{path.name}: missing semantic <{tag}>'

    for tag, attr, ref in doc.refs:
        parsed = urlsplit(ref)
        if parsed.scheme in ('https', 'http', 'mailto', 'tel', 'javascript', 'data') or ref.startswith('//'):
            continue
        if not parsed.path and parsed.fragment:
            assert parsed.fragment in doc.ids, f'{path.name}: no anchor #{parsed.fragment}'
            continue
        if not parsed.path:
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        assert target.is_relative_to(ROOT), f'{path.name}: escaping project root'
        assert target.is_file(), f'{path.name}: missing {ref}'
        if parsed.fragment and target.suffix.lower() == '.html':
            target_doc = LinkParser()
            target_doc.feed(target.read_text('utf-8'))
            assert parsed.fragment in target_doc.ids, f'{path.name}: broken link to {ref}'
    return len(doc.refs)


def main():
    total = sum(check_page(p) for p in PAGES)
    assert 'localStorage' in (ROOT/'js'/'app.js').read_text('utf-8')
    assert '@media' in (ROOT/'css'/'style.css').read_text('utf-8')
    print(f'SITE CHECKS PASSED: {len(PAGES)} HTML pages, {total} local/external references inspected.')
    print('NOTE: tests do not replace W3C validation or browser interactions.')

if __name__ == '__main__':
    main()
