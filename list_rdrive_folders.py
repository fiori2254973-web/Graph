from __future__ import annotations

import argparse
import sys
from pathlib import Path


DEFAULT_ROOT = "Z:\\"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Elenca le cartelle presenti in un Drive montato tramite RaiDrive."
    )
    parser.add_argument(
        "--root",
        default=DEFAULT_ROOT,
        help=f"percorso radice di RaiDrive (default: {DEFAULT_ROOT})",
    )
    parser.add_argument(
        "--recursive",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="elenca anche le sottocartelle (default: true)",
    )
    return parser.parse_args()


def validate_root(root: Path) -> bool:
    if not root.exists():
        print(f"Errore: il percorso '{root}' non esiste.", file=sys.stderr)
        return False

    if not root.is_dir():
        print(f"Errore: il percorso '{root}' non e' una cartella.", file=sys.stderr)
        return False

    return True


def list_folders(root: Path, recursive: bool = True) -> list[Path]:
    folders: list[Path] = []
    stack = [root]

    while stack:
        current = stack.pop()

        try:
            children = sorted(
                current.iterdir(),
                key=lambda path: path.name.casefold(),
            )
        except PermissionError:
            continue
        except OSError:
            continue

        for child in children:
            try:
                is_directory = child.is_dir()
            except PermissionError:
                continue
            except OSError:
                continue

            if not is_directory:
                continue

            folders.append(child)

            if recursive:
                stack.append(child)

    return sorted(
        folders,
        key=lambda path: path.relative_to(root).as_posix().casefold(),
    )


def main() -> int:
    args = parse_args()
    root = Path(args.root)

    if not validate_root(root):
        return 1

    folders = list_folders(root, recursive=args.recursive)

    if not folders:
        print("Nessuna cartella trovata.")
        return 0

    for folder in folders:
        print(folder.relative_to(root).as_posix())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
