import os
import re
import glob

def process_markdown_files():
    """
    处理所有chpt?.md文件，添加标题编号并保存为chapter?.md
    并在每个输出文件开头插入head.yaml内容（如果存在）
    """
    # 获取所有chpt?.md文件
    pattern = "chpt*.md"
    files = glob.glob(pattern)
    
    if not files:
        print(f"未找到匹配 {pattern} 的文件")
        return

    # 读取head.yaml内容（如果存在）
    head_yaml_path = "head.yaml"
    head_content = ""
    if os.path.exists(head_yaml_path):
        with open(head_yaml_path, 'r', encoding='utf-8') as f:
            head_content = f.read().rstrip() + "\n\n"  # 保证后面有空行分隔

    for file_path in files:
        # 提取章节数字
        match = re.search(r'chpt(\d+)\.md', file_path)
        if not match:
            print(f"跳过无法识别章节号的文件: {file_path}")
            continue
            
        chapter_num = match.group(1)

        print(f"处理文件: {file_path}, 章节号: {chapter_num}")
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 不处理标题编号
        #processed_content = add_title_numbers(content, chapter_num)
        processed_content = content
        
        # 保存为新文件
        new_filename = f"chapter{chapter_num}.md"
        with open(new_filename, 'w', encoding='utf-8') as f:
            # 先写head.yaml内容，再写正文
            if head_content:
                f.write(head_content)
            f.write(processed_content)
        
        print(f"已保存: {new_filename}")

def add_title_numbers(content, chapter_num):
    """
    为markdown内容添加标题编号
    """
    lines = content.split('\n')
    processed_lines = []
    
    # 计数器
    section_counter = 0
    subsection_counter = 0
    subsubsection_counter = 0
    
    for line in lines:
        # 检查标题级别
        if line.startswith('# '):
            # 一级标题：第X章
            processed_lines.append(f"# 第{chapter_num}章 {line[2:].strip()}")
            # 重置计数器
            section_counter = 0
            subsection_counter = 0
            subsubsection_counter = 0
            
        elif line.startswith('## '):
            # 二级标题：X.1, X.2, ...
            section_counter += 1
            subsection_counter = 0
            subsubsection_counter = 0
            processed_lines.append(f"## {chapter_num}.{section_counter} {line[3:].strip()}")
            
        elif line.startswith('### '):
            # 三级标题：X.1.1, X.1.2, ...
            subsection_counter += 1
            subsubsection_counter = 0
            processed_lines.append(f"### {chapter_num}.{section_counter}.{subsection_counter} {line[4:].strip()}")
            
        elif line.startswith('#### '):
            # 四级标题：X.1.1.1, X.1.1.2, ...
            subsubsection_counter += 1
            processed_lines.append(f"#### {chapter_num}.{section_counter}.{subsection_counter}.{subsubsection_counter} {line[5:].strip()}")
            
        else:
            # 其他行保持不变
            processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def preview_changes():
    """
    预览处理前后的变化
    """
    test_content = """# 极限

## 函数极限

### 定义

#### 左极限

#### 右极限

### 性质

## 数列极限

### 定义

### 收敛性
"""

    print("原始内容:")
    print(test_content)
    print("\n处理后的内容:")
    print(add_title_numbers(test_content, "1"))

if __name__ == "__main__":
    # 预览示例
    print("标题编号处理示例:")
    preview_changes()
    print("\n" + "="*50 + "\n")
    
    # 处理所有文件
    process_markdown_files()
    
    print("\n处理完成!")