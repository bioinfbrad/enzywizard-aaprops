from __future__ import annotations

import argparse

from .commands.aaprops import add_aaprops_parser


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="enzywizard-aaprops",
        description="EnzyWizard-AAprops: Calculate amino acid properties from input CIF/PDB file and generate a detailed JSON report."
    )
    add_aaprops_parser(parser)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)