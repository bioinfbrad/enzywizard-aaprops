from __future__ import annotations
from argparse import Namespace, ArgumentParser
from ..services.aaprops_service import run_aaprops_service

def add_aaprops_parser(parser: ArgumentParser) -> None:
    parser.add_argument("-i","--input_path", required=True, help="Path to the input cleaned protein structure file in CIF or PDB format.")
    parser.add_argument("-o","--output_dir", required=True, help="Path to the output directory for saving the JSON report.")
    parser.set_defaults(func=run_aaprops)

def run_aaprops(args: Namespace) -> None:
    run_aaprops_service(input_path=args.input_path, output_dir=args.output_dir)

