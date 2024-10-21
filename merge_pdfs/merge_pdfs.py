"""Merge PDF files into a single PDF.

This is a very thin wrapper around the PyPDF2 library.

It was inspired by https://automatetheboringstuff.com/2e/chapter15/."""

import argparse

import PyPDF2

def main():
    parser = argparse.ArgumentParser(
        prog='merge_pdfs',
        description='Merge PDFs into a single PDF file')
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('input_files', nargs='+')
    args = parser.parse_args()
    writer = PyPDF2.PdfWriter()
    for input_file in args.input_files:
        writer.append(fileobj=input_file)
    writer.write(args.output)


if __name__ == '__main__':
    main()