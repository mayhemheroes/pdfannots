#!/usr/bin/env python3
import io
import atheris
import sys

from pdfminer.pdfparser import PDFSyntaxError

with atheris.instrument_imports(exclude=["pdfminer.pdfinterp", "pdfminer.cmapdb", "pdfminer.pdfdevice",
                                         "pdfminer.converter", "pdfminer.layout", "pdfminer.utils", "pdfminer.encodingdb",
                                         "pdfminer.glyphlist", "pdfminer.latin_enc", "pdfminer.pdfcolor", "pdfminer.pdffont",
                                         "pdfminer.fontmetrics", "pdfminer.pdfpage", "pdfminer.pdfdocument", "pdfminer.arcfour",
                                         "pdfminer.data_structures", "pdfminer.image", "pdfminer.jbig2"]):
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
