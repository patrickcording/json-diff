import argparse
import json
from deepdiff import DeepDiff


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i', '--ignore-order', dest='ignore_order', type=bool, default=False, help='Ignore order of arrays')

    parser.add_argument('from_file', metavar='from_file', type=argparse.FileType('r'), help='Path to file')
    parser.add_argument('to_file', metavar='to_file', type=argparse.FileType('r'), help='Path to other file')

    args = parser.parse_args()

    from_file_json = json.load(args.from_file)
    to_file_json = json.load(args.to_file)

    ddiff = DeepDiff(from_file_json, to_file_json, ignore_order=args.ignore_order)

    print(json.dumps(json.loads(ddiff.to_json()), indent=2, sort_keys=True))