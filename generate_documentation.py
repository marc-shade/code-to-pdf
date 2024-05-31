import os
import requests
import json
from fpdf import FPDF
from tqdm import tqdm

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Repository Documentation', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title.encode('latin1', 'replace').decode('latin1'), 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        body = body.encode('latin1', 'replace').decode('latin1')
        self.multi_cell(0, 10, body)
        self.ln()

    def add_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

def generate_documentation(file_content):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3:8b",
        "prompt": f"Generate documentation and commentary for the following code:\n\n{file_content}",
        "temperature": 0.5,
        "max_tokens": 1500,
        "stream": True,  # Enable streaming response
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        full_response = ""
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                try:
                    json_response = json.loads(decoded_line)
                    if 'response' in json_response:
                        full_response += json_response['response']
                except json.JSONDecodeError as e:
                    print(f"Skipping invalid JSON line: {decoded_line}")

        return full_response.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error making request to {url}: {e}")
        return "Error generating documentation: Request failed"

def get_all_code_files(root_dir):
    code_files = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):  # You can include other extensions if needed
                code_files.append(os.path.join(subdir, file))
    return code_files

def main():
    root_dir = "/your_repository/"  # Replace with the path to your repository
    pdf = PDF()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    pdf.add_page()

    code_files = get_all_code_files(root_dir)

    # Add a progress bar
    for file_path in tqdm(code_files, desc="Processing files", unit="file"):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
        except UnicodeDecodeError:
            print(f"Error reading file {file_path}: UnicodeDecodeError")
            continue

        documentation = generate_documentation(file_content)
        chapter_title = f"File: {file_path}"

        # Combine documentation and code into the chapter body
        chapter_body = f"{documentation}\n\n{file_content}"

        pdf.add_chapter(chapter_title, chapter_body)

    output_pdf_path = "/your_repository/repository_documentation.pdf"
    pdf.output(output_pdf_path, 'F')
    print(f"PDF documentation generated: {output_pdf_path}")

if __name__ == "__main__":
    main()
