import argparse
import sys
from typing import List

from .format_manifest import format_manifest_command
from .update import update_command
from .index import index_command


def parse_arguments(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=argv[0], description="nur management commands")

    subparsers = parser.add_subparsers(description="subcommands")

    format_manifest = subparsers.add_parser('format-manifest')
    format_manifest.set_defaults(func=format_manifest_command)

    update = subparsers.add_parser('update')
    update.set_defaults(func=update_command)

    index = subparsers.add_parser('index')
    index.set_defaults(func=index_command)

    return parser.parse_args(argv[1:])


def main() -> None:
    args = parse_arguments(sys.argv)
    args.func(args)
