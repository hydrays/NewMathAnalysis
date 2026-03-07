import os
import re
import argparse

def extract_js_from_html(html_file_path):
    """
    从 HTML 文件中提取内嵌 JavaScript 并分离到独立文件
    """
    # 读取 HTML 文件
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # 创建 js 文件夹（如果不存在）
    js_dir = os.path.join(os.path.dirname(html_file_path), 'js')
    if not os.path.exists(js_dir):
        os.makedirs(js_dir)
    
    # 生成 JS 文件名（基于 HTML 文件名）
    html_filename = os.path.basename(html_file_path)
    js_filename = os.path.splitext(html_filename)[0] + '.js'
    js_file_path = os.path.join(js_dir, js_filename)
    
    # 提取所有内嵌 JavaScript
    js_code_blocks = []
    
    # 匹配 <script> 标签内的代码（包括带 type 属性的情况）
    script_pattern = r'<script[^>]*>(.*?)</script>'
    matches = re.finditer(script_pattern, html_content, re.DOTALL)
    
    for match in matches:
        script_tag = match.group(0)
        js_code = match.group(1).strip()
        
        # 跳过空脚本和外部引用脚本
        if js_code and not re.search(r'src\s*=', script_tag):
            js_code_blocks.append(js_code)
    
    if not js_code_blocks:
        print(f"在 {html_file_path} 中没有找到内嵌 JavaScript")
        return
    
    # 将所有 JavaScript 代码合并并写入 JS 文件
    all_js_code = '\n\n'.join(js_code_blocks)
    with open(js_file_path, 'w', encoding='utf-8') as js_file:
        js_file.write(all_js_code)
    print(f"JavaScript 代码已保存到: {js_file_path}")
    
    # 从 HTML 中移除内嵌 JavaScript，添加外部引用
    def replace_script(match):
        script_tag = match.group(0)
        js_code = match.group(1).strip()
        
        # 如果是内嵌脚本且非空，替换为外部引用
        if js_code and not re.search(r'src\s*=', script_tag):
            return f'<script src="js/{js_filename}" defer></script>'
        else:
            return script_tag  # 保持外部脚本不变
    
    # 替换所有内嵌脚本
    new_html_content = re.sub(script_pattern, replace_script, html_content, flags=re.DOTALL)
    
    # 移除重复的外部引用（如果多次替换产生了重复）
    new_html_content = re.sub(r'(<script src="js/' + re.escape(js_filename) + r'" defer></script>\s*)+', 
                             f'<script src="js/{js_filename}" defer></script>', 
                             new_html_content)
    
    # 备份原文件并写入新内容
    backup_path = html_file_path + '.bak'
    with open(backup_path, 'w', encoding='utf-8') as backup_file:
        backup_file.write(html_content)
    
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(new_html_content)
    
    print(f"HTML 文件已更新，原文件已备份为: {backup_path}")
    print(f"成功将 {len(js_code_blocks)} 个 JavaScript 代码块分离到外部文件")

def main():
    parser = argparse.ArgumentParser(description='将 HTML 文件中的内嵌 JavaScript 分离到外部文件')
    parser.add_argument('html_file', help='要处理的 HTML 文件路径')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.html_file):
        print(f"错误: 文件 {args.html_file} 不存在")
        return
    
    extract_js_from_html(args.html_file)

if __name__ == "__main__":
    # 如果直接运行脚本，处理 chapter1.html
    if os.path.exists('chapter1.html'):
        extract_js_from_html('chapter1.html')
    else:
        print("请提供 HTML 文件路径作为参数")
        print("用法: python script.py chapter1.html")