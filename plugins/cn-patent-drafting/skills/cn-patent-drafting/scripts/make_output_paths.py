#!/usr/bin/env python3
"""Generate timestamped output paths for Chinese patent case files."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


FORBIDDEN = r'[\\/:*?"<>|\r\n\t]'
PLACEHOLDERS = ("[待填写]", "【待填写】", "待填写", "[TODO]", "TODO")
PACKAGE_DOCS = [
    "00_专利草案总览",
    "01_技术交底书",
    "02_权利要求书",
    "03_说明书",
    "04_说明书摘要",
    "05_说明书附图",
    "06_摘要附图",
    "07_查新与差异化分析",
    "提交文件清单",
]


def normalize_case_name(name: str, max_len: int = 80) -> str:
    text = name.strip()
    for marker in PLACEHOLDERS:
        text = text.replace(marker, "")
    text = re.sub(FORBIDDEN, "", text)
    text = re.sub(r"\s+", "", text)
    text = text.strip("._- ")
    if not text:
        text = "中国发明专利"
    if len(text) > max_len:
        text = text[:max_len].rstrip("._- ")
    return text


def build_paths(case_name: str, case_dir: str, extensions: list[str]) -> dict[str, object]:
    safe_name = normalize_case_name(case_name)
    timestamp = datetime.now().astimezone().strftime("%Y%m%d%H%M%S")
    stem = f"{safe_name}_{timestamp}"
    base = Path(case_dir).expanduser()
    files = {ext: str(base / f"{stem}.{ext}") for ext in extensions}
    return {
        "case_name": case_name,
        "safe_case_name": safe_name,
        "timestamp": timestamp,
        "stem": stem,
        "case_dir": str(base),
        "files": files,
    }


def build_package(case_name: str, output_root: str, extensions: list[str]) -> dict[str, object]:
    safe_name = normalize_case_name(case_name)
    timestamp = datetime.now().astimezone().strftime("%Y%m%d%H%M%S")
    case_dir = Path(output_root).expanduser() / f"{safe_name}_{timestamp}"
    package_files = {
        doc: {ext: str(case_dir / f"{doc}.{ext}") for ext in extensions}
        for doc in PACKAGE_DOCS
    }
    return {
        "case_name": case_name,
        "safe_case_name": safe_name,
        "timestamp": timestamp,
        "case_dir": str(case_dir),
        "package_files": package_files,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-name", required=True, help="Chinese case/invention name.")
    parser.add_argument("--case-dir", default="outputs/case", help="Output case directory.")
    parser.add_argument("--output-root", default="outputs", help="Package output root.")
    parser.add_argument(
        "--package",
        action="store_true",
        help="Generate a complete patent package path map.",
    )
    parser.add_argument(
        "--ext",
        action="append",
        default=["md"],
        help="Output extension without dot. Can be repeated. Default: md.",
    )
    parser.add_argument("--also-docx", action="store_true", help="Also include a docx path.")
    parser.add_argument("--max-len", type=int, default=80, help="Maximum normalized name length.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    extensions = [ext.lstrip(".") for ext in args.ext]
    if args.also_docx and "docx" not in extensions:
        extensions.append("docx")
    if args.package:
        result = build_package(args.case_name, args.output_root, extensions)
    else:
        result = build_paths(args.case_name, args.case_dir, extensions)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
