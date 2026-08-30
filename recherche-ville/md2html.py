#!/usr/bin/env python3
"""Markdown -> HTML autonome (aucune dependance). Sous-ensemble suffisant
pour rapport.md : titres, tableaux, listes, blockquotes, hr, emphase,
code inline, blocs ::: et badges de registre FAIT/LECTURE/INCERTAIN."""
import html, re, sys

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'~~([^~]+)~~', r'<del>\1</del>', t)
    t = t.replace('&lt;br&gt;', '<br>')
    t = re.sub(r'&lt;sub&gt;(.*?)&lt;/sub&gt;', r'<sub>\1</sub>', t)
    for tag in ('FAIT', 'LECTURE', 'INCERTAIN'):
        t = t.replace(f'<code>{tag}</code>', f'<span class="tag {tag.lower()}">{tag}</span>')
    return t

def convert(md):
    out, lines, i = [], md.split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith(':::'):
            name = l[3:].strip()
            if name:
                out.append(f'<div class="callout {name}">'); i += 1
                while i < len(lines) and not lines[i].startswith(':::'):
                    if lines[i].strip():
                        out.append('<p>' + inline(lines[i].rstrip('  ')) + '</p>')
                    i += 1
                out.append('</div>')
            i += 1; continue
        if re.match(r'^#{1,6} ', l):
            n = len(l) - len(l.lstrip('#'))
            out.append(f'<h{n}>{inline(l[n+1:])}</h{n}>'); i += 1; continue
        if l.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i+1]):
            hdr = [c.strip() for c in l.strip('|').split('|')]
            out.append('<table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in hdr) + '</tr></thead><tbody>')
            i += 2
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>')
                i += 1
            out.append('</tbody></table>'); continue
        if l.startswith('> '):
            buf = []
            while i < len(lines) and lines[i].startswith('>'):
                buf.append(lines[i].lstrip('> ').rstrip()); i += 1
            out.append('<blockquote><p>' + inline(' '.join(buf)) + '</p></blockquote>'); continue
        if re.match(r'^---+$', l):
            out.append('<hr>'); i += 1; continue
        if re.match(r'^\d+\. ', l):
            out.append('<ol>')
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                out.append('<li>' + inline(re.sub(r'^\d+\. ', '', lines[i])) + '</li>'); i += 1
            out.append('</ol>'); continue
        if re.match(r'^[-*] ', l):
            out.append('<ul>')
            while i < len(lines) and re.match(r'^[-*] ', lines[i]):
                out.append('<li>' + inline(lines[i][2:]) + '</li>'); i += 1
            out.append('</ul>'); continue
        if l.strip():
            buf = []
            while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,6} |\||> |---+$|\d+\. |[-*] |:::)', lines[i]):
                buf.append(lines[i].rstrip()); i += 1
            out.append('<p>' + inline(' '.join(buf)) + '</p>'); continue
        i += 1
    return '\n'.join(out)

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm; }
* { box-sizing: border-box; }
body { font: 10.5pt/1.55 "Helvetica Neue", Helvetica, Arial, sans-serif;
       color: #1a1a1a; margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1 { font-size: 21pt; letter-spacing: -.4pt; margin: 0 0 .2em; }
h2 { font-size: 13pt; margin: 1.9em 0 .55em; padding-bottom: .3em;
     border-bottom: 1.5px solid #1a1a1a; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 1.3em 0 .4em; color: #333; page-break-after: avoid; }
p { margin: 0 0 .65em; orphans: 3; widows: 3; }
hr { border: 0; border-top: 1px solid #d8d8d8; margin: 1.6em 0; }
code { font: 9.2pt/1.4 "SF Mono", Menlo, Consolas, monospace;
       background: #f2f2f0; padding: .1em .35em; border-radius: 3px; }
del { color: #8a8a8a; }
blockquote { margin: 1em 0; padding: .7em 1em; background: #faf8f4;
             border-left: 3px solid #c9a227; page-break-inside: avoid; }
blockquote p { margin: 0; font-size: 9.8pt; }
table { width: 100%; border-collapse: collapse; margin: 1em 0; font-size: 9pt;
        page-break-inside: avoid; }
th { text-align: left; background: #1a1a1a; color: #fff; padding: .5em .6em; font-weight: 600; }
td { padding: .45em .6em; border-bottom: .5px solid #e2e2e2; vertical-align: top; }
tbody tr:nth-child(even) td { background: #fafafa; }
sub { font-size: 7.5pt; color: #777; }
ul, ol { margin: 0 0 .8em; padding-left: 1.4em; }
li { margin-bottom: .3em; }
.tag { font: 600 7.5pt/1 "Helvetica Neue", Arial, sans-serif; letter-spacing: .06em;
       padding: .3em .5em; border-radius: 2px; vertical-align: .08em; margin-right: .15em; }
.tag.fait      { background: #1c4d3a; color: #fff; }
.tag.lecture   { background: #e8e2d0; color: #5a4a1f; border: .5px solid #c9a227; }
.tag.incertain { background: #fff; color: #8a3324; border: 1px dashed #8a3324; }
.callout { background: #f7f7f5; border: .5px solid #ddd; border-radius: 4px;
           padding: .8em 1em; margin: 1.2em 0; page-break-inside: avoid; }
.callout p { margin: .25em 0; font-size: 9.3pt; }
"""

def main():
    src, dst = sys.argv[1], sys.argv[2]
    body = convert(open(src, encoding='utf-8').read())
    title = 'Rapport'
    m = re.search(r'<h1>(.*?)</h1>', body)
    if m: title = re.sub(r'<[^>]+>', '', m.group(1))
    open(dst, 'w', encoding='utf-8').write(
        f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
        f'<title>{html.escape(title)}</title><style>{CSS}</style></head>'
        f'<body>{body}</body></html>')

if __name__ == '__main__':
    main()
