import argparse

parser = argparse.ArgumentParser()
parser.add_argument("commands", help="display all the available linux commands available in the linux cheatsheet")
parser.add_argument("-v", "--verbose", action="store_true", help="increases output verbosity")
args = parser.parse_args()
if args.verbose:
    argumentInput = args.commands
    print("verbosity has been turned on")

