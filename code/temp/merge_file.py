import os
import re
import glob

def remove_chapter_number(md_content):
    """
    去除'# 第n章'中的'第n章'，保留后面的名称
    """
    # 匹配如 "# 第四章 积分" 或 "# 第4章 ..."，只去掉"第n章"
    pattern = r'(^\s*#\s*)第[一二三四五六七八九十\d]+章(\s*)'
    # 替换为"# "加原有空格和后面的名称
    return re.sub(pattern, r'\1', md_content, count=1, flags=re.MULTILINE)

def merge_markdown_files(output_file="merged_lecture.md"):
    """
    合并所有以chpt开头的markdown文件，只保留第一个文件的头部
    """
    # 获取所有以chpt开头的md文件，并按数字排序
    chapter_files = sorted(glob.glob("chpt*.md"), 
                          key=lambda x: int(re.search(r'chpt(\d+)', x).group(1)))
    
    if not chapter_files:
        print("未找到以chpt开头的markdown文件")
        return
    
    print(f"找到以下文件将进行合并: {chapter_files}")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # 处理第一个文件 - 只保留头部
        with open(chapter_files[0], 'r', encoding='utf-8') as first_file:
            content = first_file.read()
            # 去除第n章编号，保留名称
            content = remove_chapter_number(content)
            toc_pos = content.find("[toc]")
            if toc_pos != -1:
                header_end = toc_pos + len("[toc]")
                header = content[:header_end].strip()
                outfile.write(header + "\n\n")
                print("已提取第一个文件的头部")
            else:
                print("警告: 第一个文件中未找到[toc]标记，将保留整个文件作为头部")
                outfile.write(content + "\n\n")
        
        # 合并所有文件的内容（第一个文件从头部之后开始）
        for i, filename in enumerate(chapter_files):
            print(f"正在处理: {filename}")
            with open(filename, 'r', encoding='utf-8') as infile:
                content = infile.read()
                # 去除第n章编号，保留名称
                content = remove_chapter_number(content)
                if i == 0:  # 第一个文件，跳过已写入的头部
                    toc_pos = content.find("[toc]")
                    if toc_pos != -1:
                        header_end = toc_pos + len("[toc]")
                        remaining_content = content[header_end:].strip()
                        if remaining_content:
                            outfile.write(remaining_content + "\n\n")
                else:  # 其他文件，直接写入全部内容
                    outfile.write(content + "\n\n")
    
    print(f"合并完成！输出文件: {output_file}")

def preview_merged_file(filename="merged_lecture.md", lines=50):
    """
    预览合并后的文件前几行
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f"\n合并文件的前{lines}行预览:")
            print("-" * 50)
            for i, line in enumerate(f):
                if i >= lines:
                    break
                print(line.rstrip())
            print("-" * 50)
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")

if __name__ == "__main__":
    # 合并文件
    merge_markdown_files("高等数学讲义_完整版.md")
    
    # 预览合并结果
    preview_merged_file("高等数学讲义_完整版.md", 30)