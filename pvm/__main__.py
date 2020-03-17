import argparse
import logging

from . import run

parser = argparse.ArgumentParser(
    prog="pvm",
    description="Run Python programs with a Python bytecode interpreter.",
)
parser.add_argument(
    '-v', '--verbose', dest='verbose', action='store_true',
    help="trace the execution of the bytecode.",
)
parser.add_argument(
    'prog',
    help="The program to run.",
)
parser.add_argument(
    'args', nargs=argparse.REMAINDER,
    help="Arguments to pass to the program.",
)
args = parser.parse_args()

run_fn = run.run_python_file

level = logging.DEBUG if args.verbose else logging.WARNING
logging.basicConfig(level=level)

argv = [args.prog] + args.args
run_fn(args.prog, argv)
