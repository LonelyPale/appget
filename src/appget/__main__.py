#!/usr/bin/env python3

import sys

from . import appget, log

DEBUG = True


def main():
    try:
        appget.cli()
        return 0
    except Exception as err:
        if DEBUG:
            raise
        log.error(err)
        return 1


if __name__ == "__main__":
    sys.exit(main())
