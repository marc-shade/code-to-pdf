# code-to-pdf
Use Ollama to document your code!

## Repository Documentation Generator

This project provides a tool to generate comprehensive documentation for all Python files in a given repository and compile them into a PDF. It uses an AI model to generate documentation and the `fpdf` library to create the PDF.

## Features
- Recursively scans a specified directory for Python files.
- Generates documentation for each Python file using an AI model.
- Compiles the documentation and source code into a structured PDF.

## Prerequisites
- Python 3.x
- `fpdf` library
- `tqdm` library
- `requests` library

Install the necessary Python libraries using:
```sh
pip install fpdf tqdm requests
