#!/usr/bin/env python3

"""
PDF to HTML conversion - first step of the process. Batch processes a folder full of PDFs using pdf2htmlEX producing a HTML folder.

This HTML uses just CSS positioning for layout. We need further work to add sematic tags: transcript.py
"""

import glob, os
import config


def pdf2html(pdf_path):
    print(pdf_path)
    # splittext returns filename and extension
    # We want just the filename, without path
    filename = os.path.splitext(pdf_path)[0].split("/")[-1]

    # --embed cfijo = don't embed Css, Fonts, Images, Js, Outlines (> man pdf2htmlEX)
    # Double quotes to allow spaces in paths
    os.system('docker run -ti --rm -v "{}":/pdf bwits/pdf2htmlex pdf2htmlEX --embed-external-font 0 --external-hint-tool ttfautohint --process-nontext 0 --embed cfijo "{}".pdf'.format(config.DATA_DIR, filename))


if __name__ == '__main__':
    # Run pdf2htmlEX on each pdf in the data directory
    for i, path in enumerate(glob.glob(config.DATA_DIR + '/*.pdf')):
        pdf2html(path)
