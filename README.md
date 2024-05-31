# code-to-pdf
Use Ollama to document your code!


# Repository Documentation Generator

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
```

## Usage
1. Clone the repository to your local machine.
2. Set the `root_dir` variable in `main()` to the path of your target repository.
3. Run the script:
```sh
python generate_documentation.py
```

The output PDF will be saved in the specified directory.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
