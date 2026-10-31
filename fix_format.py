import os
import re

md_files = []
for root, dirs, files in os.walk('.'):
    if '.git' in root: continue
    for file in files:
        if file.endswith('.md'):
            md_files.append(os.path.join(root, file))

print(f"找到 {len(md_files)} 个 md 文件，开始处理...\n")

# 极其严苛：必须从第一行开始，必须是一级标题，后面必须紧跟表格
pattern = r'^\s*(# (.*?))\s*\n+((?:\|.*\|(?:\n|$))+)'

success_count = 0

for filepath in md_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.match(pattern, content) # 使用 re.match 确保从头开始
        
        if match:
            title = match.group(1).strip()
            table = match.group(3).strip()
            
            # 强校验：必须是元数据表格
            if '| 项目 |' in table or '| Item |' in table or '| 标题 |' in table or '| Title |' in table:
                
                # 检查是否已经改过
                if "<br>" in content[:len(match.group(0)) + 10]:
                    print(f"⏭️  跳过: {filepath}")
                    continue
                
                # 绝对安全的切片拼接：把匹配到的部分替换掉，后面的正文原封不动保留
                remaining_content = content[len(match.group(0)):].lstrip()
                new_header = f"{table}\n\n---\n\n<br>\n\n{title}\n\n"
                new_content = new_header + remaining_content
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ 已修改: {filepath}")
                success_count += 1
    except Exception as e:
        print(f"❌ 出错 {filepath}: {e}")

print(f"\n🎉 处理完毕！成功修改 {success_count} 篇。")
print("⚠️ 如果发现任何不对劲，立刻输入： git restore . 即可全部还原！")
