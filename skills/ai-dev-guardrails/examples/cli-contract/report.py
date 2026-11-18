"""Read one record identifier per line and write a JSON array to stdout."""

import json
import sys


def main():
    identifiers = sys.stdin.read().splitlines()
    records = [{"id": value} for value in identifiers]
    print(json.dumps(records))


if __name__ == "__main__":
    main()
