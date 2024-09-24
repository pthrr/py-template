#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import sys
import typing

from libx import calc

logger = logging.getLogger(__name__)


def main(args: argparse.Namespace) -> int:
    print(f"1+1= {calc(1, 1)}")
    return 0


def str_to_bool(value: typing.Union[str, bool]) -> bool:
    if isinstance(value, bool):
        return value

    if value.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif value.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug",
        type=str_to_bool,
        nargs="?",
        const=True,
        default=False,
        help="Activate debug mode.",
    )
    parser.add_argument(
        "argv",
        nargs="*",
    )
    args = parser.parse_args()

    LOGGING_LEVEL = logging.ERROR

    if args.debug:
        LOGGING_LEVEL = logging.DEBUG

    LOGGING_FORMAT_STRING = (
        "%(asctime)s | %(name)s | %(levelname)s | %(module)s, %(threadName)s, %(funcName)s, %(lineno)d | %(message)s"
    )
    logging.basicConfig(format=LOGGING_FORMAT_STRING, level=LOGGING_LEVEL)
    logging.debug("PATH: %s", sys.path)
    logging.debug("args: %s", args)
    return_code = main(args)
    logging.info("Done.")
    sys.exit(return_code)
