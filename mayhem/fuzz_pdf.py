#!/usr/bin/env python3
import io
import atheris
import sys

from pdfminer.pdfparser import PDFSyntaxError

with atheris.instrument_imports():
    import pdfannots

@atheris.instrument_func
def TestOneInput(data):
    if not data:
        return -1
    try:
        with io.BytesIO(data) as f:
            pdfannots.process_file(f)
    except PDFSyntaxError:
        pass
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == '__main__':
    main()
