from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIRS = [
    "bootstrap",
    "config",
    "councils",
    "samples",
    "sessions",
    "templates",
]
TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
    ".py",
    ".ps1",
    ".sh",
}


def iter_targets(args: list[str]) -> list[Path]:
    names = args or DEFAULT_DIRS
    targets: list[Path] = []
    for name in names:
        path = (ROOT / name).resolve()
        if path.exists():
            targets.append(path)
    return targets


def iter_files(target: Path):
    if target.is_file():
        if target.suffix.lower() in TEXT_EXTENSIONS:
            yield target
        return
    for path in target.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            yield path


def main() -> int:
    bad: list[tuple[Path, str]] = []
    checked = 0
    for target in iter_targets(sys.argv[1:]):
        for path in iter_files(target):
            checked += 1
            try:
                path.read_text(encoding="utf-8")
            except UnicodeDecodeError as exc:
                bad.append((path, str(exc)))

    print(f"checked: {checked}")
    if not bad:
        print("result: all checked files are valid UTF-8")
        return 0

    print("result: invalid UTF-8 files found")
    for path, error in bad:
        print(f"- {path.relative_to(ROOT)}")
        print(f"  {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
