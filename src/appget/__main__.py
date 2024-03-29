#!/usr/bin/env python3

import sys

from . import cli, log
from .utils import DEBUG


def main():
    try:
        cli.cli()
        return 0
    except Exception as err:
        if DEBUG:
            raise
        log.error(err)
        return 1


if __name__ == "__main__":
    sys.exit(main())
