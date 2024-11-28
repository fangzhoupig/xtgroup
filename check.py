import os

# 读取包含文件路径的文件
file_path = "log.dryrun.1yr.GFED.unique.2"  # 替换为你的文件路径
with open(file_path, "r") as file:
    lines = file.readlines()

# 检查每一行文件路径是否存在，如果存在就删除该行
updated_lines = []
for line in lines:
    file_path = line.strip()  # 移除行尾的换行符和空格
    if not os.path.exists(file_path):
        updated_lines.append(line)

# 将更新后的内容写回文件
file_path = "log.dryrun.1yr.GFED.unique"
with open(file_path, "w") as file:
    file.writelines(updated_lines)

print("已删除存在的文件路径行。")
