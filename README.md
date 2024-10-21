# Merge PDF files into a single PDF

Example usage:

```
python3 -m venv python
cd python
bin/pip3 install git+https://github.com/fadend/merge_pdfs
bin/python3 -m merge_pdfs.merge_pdfs -o merged.pdf *.pdf
```

This is an extremely thin wrapper around the [PyPDF2](https://pypi.org/project/PyPDF2/) package,
which I learned about from
[Automate the Boring Stuff with Python, Chapter 15](https://automatetheboringstuff.com/2e/chapter15/).
