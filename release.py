#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import json
from dataclasses import dataclass
from pathlib import Path
from typing import List
from urllib.parse import quote

INDENT = " " * 4
ROOT = Path(__file__).resolve().parent / "docs"


class BasicItem:
    text: str


@dataclass
class Page(BasicItem):
    text: str
    link: str


@dataclass
class Group(BasicItem):
    text: str
    collapsed: bool
    items: List[BasicItem]


class MyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (Page, Group)):
            return o.__dict__
        return super().default(o)


def build_structure(root: Path) -> Group:
    root_group = Group(text="root", collapsed=False, items=[])
    for p in root.iterdir():
        if p.name.startswith("."):
            # skip hidden files and directories
            continue
        if p.is_dir():
            item = build_group(p, root)
            if item.items:
                root_group.items.append(item)
        elif p.is_file():
            if p.suffix.lower() != ".md":
                continue
            item = build_page(p, root)
            root_group.items.append(item)
    return root_group


def build_group(d: Path, root: Path, depth: int = 0) -> Group:
    collapsed = depth >= 1
    group = Group(text=d.name, collapsed=collapsed, items=[])
    for p in d.iterdir():
        if p.is_dir():
            item = build_group(p, root, depth=depth + 1)
            if item.items:
                group.items.append(item)
        elif p.is_file():
            if p.suffix.lower() != ".md":
                continue
            item = build_page(p, root)
            group.items.append(item)
    return group


def build_page(p: Path, root: Path) -> Page:
    text = p.stem
    link = "/" + quote(str(p.relative_to(root)).replace("\\", "/"))
    return Page(text=text, link=link)


def main():
    root = Path(ROOT).resolve()
    assert root.exists()

    # print(json.dumps(build_structure(root), indent=2, cls=MyJSONEncoder))
    structure = build_structure(root)
    with (root / "structure.json").open("w+", encoding="utf8") as f:
        json.dump(structure.items, f, indent=2, cls=MyJSONEncoder, ensure_ascii=False)

    # file_paths = find_markdowns(root)
    # side_bars_list = create_sidebar(file_paths)

    # with (root / "_sidebar.md").open("w+", encoding="utf8") as f:
    #     f.write("\n".join(side_bars_list))

    print("Done")


if __name__ == "__main__":
    main()
