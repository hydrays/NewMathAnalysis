import glob
from bs4 import BeautifulSoup

# 收集所有 chapter?.html 文件
html_files = glob.glob('chapter*.html')

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    css_content = ''
    for style in soup.find_all('style'):
        css_content += style.string or ''
        style.decompose()

    head = soup.head
    if head:
        link_tag = soup.new_tag('link', rel='stylesheet', href='style.css')
        head.append(link_tag)

    # 保存新的 HTML
    out_html = html_file
    with open(out_html, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    # 保存 CSS
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

    print(f'{out_html} 分离完成')