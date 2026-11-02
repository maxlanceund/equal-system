import os, re

for root, dirs, files in os.walk('.'):
    if '.git' in root: continue
    for file in files:
        if not file.endswith('.md'): continue
        filepath = os.path.join(root, file)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content

        # 1. 删除 "核心论点" 引用块 (包括中文和英文)
        # 匹配以 > 开头，且包含“核心论点”的连续行
        content = re.sub(r'^>[^\n]*核心论点[^\n]*\n(?:>[^\n]*\n?)*', '', content, flags=re.MULTILINE)
        content = re.sub(r'^>[^\n]*Core Thesis[^\n]*\n(?:>[^\n]*\n?)*', '', content, flags=re.MULTILINE)

        # 2. 删除连续重复的相同一级标题
        # 匹配形如: # 标题 \n (任意空行) # 同样的标题
        content = re.sub(r'^(# .+?)\s*\n+\1\s*\n', r'\1\n\n', content, flags=re.MULTILINE)

        # 清理多余的空行 (防止删掉内容后留下3个以上的连续换行)
        content = re.sub(r'\n{3,}', '\n\n', content)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已清理: {filepath}")

print("🎉 清理完毕！")
