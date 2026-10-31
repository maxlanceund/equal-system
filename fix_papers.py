import os, re
for root, _, files in os.walk('./papers'):
    for f in files:
        if f.endswith('.md'):
            p = os.path.join(root, f)
            c = open(p, encoding='utf-8').read()
            # 提取开头的标题（支持多行##）和紧接着的表格
            m = re.search(r'^((?:#.*\n?)+)\s*(\|.*\|(?:\n|$)+)', c)
            if m and '<br>' not in c[:150]:
                new_c = m.group(2) + '\n\n---\n\n<br>\n\n' + m.group(1).strip() + '\n\n' + c[m.end():].lstrip()
                open(p, 'w', encoding='utf-8').write(new_c)
                print('✅ 已修改:', f)
