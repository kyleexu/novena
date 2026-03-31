#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import urllib.parse


EXCLUDE_DIRS = {
    ".git",
    ".github",
    ".idea",
    ".vscode",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
}

SECTION_TITLES = {
    "zh": "## 中文内容",
    "en": "## English Content",
}

LANGUAGE_ORDER = ["zh", "en"]

DIRECTORY_TITLES = {
    "project": "项目经验",
    "repository": "技术知识库",
    "hongkong": "香港",
    "tax": "税务",
    "market": "行情服务",
    "otc": "OTC",
    "rate-limit": "限流服务",
    "rule-engine": "规则引擎",
    "flink": "Flink",
    "java": "Java",
    "kafka": "Kafka",
    "mqtt": "MQTT",
    "mysql": "MySQL",
    "others": "其他",
    "redis": "Redis",
}

DIRECTORY_ORDER = {
    "zh": ["project","hongkong","repository"],
    "zh/project": ["market", "otc", "rate-limit", "rule-engine"],
    "zh/repository": ["flink", "java", "kafka", "mqtt", "mysql", "others", "redis"],
    "zh/hongkong": ["tax"],
    "en": ["java", "market", "rule-engine"],
}


def get_display_name(name):
    """将目录名映射为更适合 README 展示的标题。"""
    return DIRECTORY_TITLES.get(name, name)


def encode_link(path):
    """对文档路径进行 URL 编码。"""
    return urllib.parse.quote(path, safe="/")


def sort_entries(entries, order):
    """按配置顺序排序，未配置项按名称补在后面。"""
    order_index = {name: index for index, name in enumerate(order)}
    return sorted(entries, key=lambda entry: (order_index.get(entry, len(order)), entry))


def scan_directory(dir_path, base_path, relative_dir="", heading_level=3):
    """递归扫描目录，生成分层 Markdown。"""
    items = []
    if not os.path.isdir(dir_path):
        return items

    entries = sorted(os.listdir(dir_path))
    files = []
    directories = []

    for entry in entries:
        if entry.startswith(".") or entry in EXCLUDE_DIRS:
            continue

        entry_path = os.path.join(dir_path, entry)
        if os.path.isfile(entry_path) and entry.endswith(".md"):
            files.append(entry)
        elif os.path.isdir(entry_path):
            directories.append(entry)

    directories = sort_entries(directories, DIRECTORY_ORDER.get(relative_dir, []))

    for file_name in files:
        file_path = os.path.join(dir_path, file_name)
        relative_path = os.path.relpath(file_path, base_path)
        display_name = os.path.splitext(file_name)[0]
        items.append(f"- [{display_name}]({encode_link(relative_path)})")

    for directory in directories:
        sub_dir_path = os.path.join(dir_path, directory)
        sub_relative_dir = f"{relative_dir}/{directory}" if relative_dir else directory
        sub_items = scan_directory(
            sub_dir_path,
            base_path,
            relative_dir=sub_relative_dir,
            heading_level=heading_level + 1,
        )
        if not sub_items:
            continue

        if items:
            items.append("")
        items.append(f"{'#' * heading_level} {get_display_name(directory)}")
        items.extend(sub_items)

    return items


def get_language_directories(base_path):
    """获取当前仓库中的语言目录。"""
    directories = []
    for language in LANGUAGE_ORDER:
        language_path = os.path.join(base_path, language)
        if os.path.isdir(language_path):
            directories.append(language)

    return directories


def generate_readme():
    """根据当前目录结构生成 README。"""
    base_path = os.path.dirname(os.path.abspath(__file__))

    content = [
        "# Novena - 个人技术知识库",
        "",
        "系统化整理的技术知识库，涵盖中文项目复盘、技术专题沉淀以及英文材料整理。",
        "",
        "> 📖 **在线阅读**: [https://kyleexu.github.io/novena](https://kyleexu.github.io/novena)",
        "",
        "---",
        "",
    ]

    total_docs = 0
    for language_dir in get_language_directories(base_path):
        content.append(SECTION_TITLES[language_dir])
        content.append("")

        items = scan_directory(
            os.path.join(base_path, language_dir),
            base_path,
            relative_dir=language_dir,
        )
        if items:
            total_docs += sum(1 for item in items if item.startswith("- ["))
            content.extend(items)
        else:
            content.append("暂无文档")

        content.append("")
        content.append("---")
        content.append("")

    readme_path = os.path.join(base_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as file:
        file.write("\n".join(content))

    print(f"✅ README.md 已更新 ({total_docs} 个文档)")


if __name__ == "__main__":
    generate_readme()