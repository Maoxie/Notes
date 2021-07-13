#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import itertools
from pathlib import Path
from urllib.parse import quote


INDENT = " " * 4
ROOT = Path(__file__).resolve().parent / "docs"


def find_markdowns(root):
    file_paths = [
        p.relative_to(root)
        for p in Path(root).rglob("*.md")
        if not p.stem.startswith("_") and p.is_file()   # ignore "_sidebar.md"
    ]
    return file_paths


def create_sidebar(file_paths):
    lines = [
        "<!-- docs/_sidebar.md -->",
        "",
        "- [ABOUT](/)",
    ]
    current_folder = Path("")
    for path in file_paths:
        if str(path) == "README.md":
            continue
        level = len(path.parts)
        if path.parent != current_folder:
            lines.append("")
            i = 0
            for i, (x, y) in enumerate(itertools.zip_longest(current_folder.parts, path.parent.parts)):
                if x != y:
                    break
            for j, name in enumerate(path.parent.parts[i:], i):
                line = "{indent}- {name}".format(indent=INDENT * j, name=name)
                lines.append(line)
            current_folder = path.parent

        line = "{indent}- [{name}]({link})".format(
            indent=INDENT * (level - 1),
            name=path.stem,
            link=quote(str(path).replace("\\", "/"))
        )
        lines.append(line)

    return lines


def main():
    root = Path(ROOT).resolve()
    assert root.exists()
    file_paths = find_markdowns(root)
    side_bars_list = create_sidebar(file_paths)

    with (root / "_sidebar.md").open("w+", encoding="utf8") as f:
        f.write("\n".join(side_bars_list))

    print("Done")


if __name__ == "__main__":
    main()
