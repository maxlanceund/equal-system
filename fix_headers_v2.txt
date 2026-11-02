import os

md_files = []
for root, dirs, files in os.walk('.'):
    if '.git' in root: continue
    for file in files:
        if file.endswith('.md'):
            md_files.append(os.path.join(root, file))

success_count = 0
print(f"找到 {len(md_files)} 个 md 文件，开始抓捕漏网之鱼...\n")

for filepath in md_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 1. 在前 50 行中寻找元数据表格的起始位置
        table_start = -1
        for i, line in enumerate(lines[:50]):
            if line.strip().startswith('| 项目 |') or line.strip().startswith('| Item |') or line.strip().startswith('| 标题 |') or line.strip().startswith('| Title |'):
                table_start = i
                break
        
        if table_start != -1:
            # 2. 从表格位置向上寻找连续的标题（允许中间有空行）
            title_lines = []
            first_title_idx = -1
            for i in range(table_start - 1, -1, -1):
                if lines[i].strip().startswith('#'):
                    title_lines.insert(0, lines[i])
                    first_title_idx = i
                elif lines[i].strip() == '':
                    continue
                else:
                    break
            
            if title_lines:
                title_block = ''.join(title_lines).strip()
                
                # 3. 提取表格块
                table_end = table_start
                while table_end < len(lines) and lines[table_end].strip().startswith('|'):
                    table_end += 1
                table_block = ''.join(lines[table_start:table_end]).strip()

                content = ''.join(lines)
                # 4. 判断是否已经是新格式（如果标题在表格下方，且带有 <br>，说明已经改好了）
                if content.find(title_block) > content.find(table_block) and '<br>' in content:
                    continue # 已经改过，静默跳过

                # 5. 重新组装
                prefix = ''.join(lines[:first_title_idx])
                suffix = ''.join(lines[table_end:])
                
                new_content = prefix + table_block + '\n\n---\n\n<br>\n\n' + title_block + '\n\n' + suffix
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ 已修复漏网之鱼: {filepath}")
                success_count += 1

    except Exception as e:
        print(f"❌ 出错 {filepath}: {e}")

print(f"\n🎉 处理完毕！本轮共成功捕获并修改 {success_count} 篇。")
