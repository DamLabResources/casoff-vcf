#!/usr/bin/env python
"""Wrapper for cas9 off-finder to find matches with SNPs"""
# Copyright (C) 2017 Will Dampier. See LICENSE for terms of use.
import sys
import logging

import click
from click import echo

__version__ = '0.1'


@click.command()
@click.help_option('--help', '-h')
@click.version_option(version=__version__)
@click.option('--debug', is_flag=True,
    help='enable debug logging')
def main(debug):
    """Wrapper for cas9 off-finder to find matches with SNPs"""
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger(__name__)
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Enabled debug output")

