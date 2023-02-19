#!/usr/bin/env python3

import nyx.starter
import sys
from memory_profiler import profile


@profile
def main():
    try:
        nyx.starter.main()
    except ImportError as exc:
        print("Unable to start nyx: %s" % exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
