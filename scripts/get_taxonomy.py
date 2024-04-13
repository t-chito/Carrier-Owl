"""
https://arxiv.org/category_taxonomy の分類を
dict として持っておくための変換関数を提供する
"""

import json
import re


def parse_category(text):
    lines = text.strip().split("\n")
    category, name = re.match(r"(\S+)\s*\((.+)\)", lines[0]).groups()
    description = " ".join(lines[1:])
    return {"category": category, "name": name, "description": description}


def parse_categories(text):
    categories = re.split(r"\n{2,}", text.strip())
    return {category.split(" ")[0]: parse_category(category) for category in categories}


# 今は cs だけ
with open("./src/category_taxonomy.txt") as f:
    taxonomy_text = f.read()

with open("./src/category_taxonomy.json", "w") as f:
    json.dump(parse_categories(taxonomy_text), f)
