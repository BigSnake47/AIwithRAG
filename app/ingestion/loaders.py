
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import pymupdf as pdf
from docx import Document as Doc
from bs4 import BeautifulSoup as BS

@dataclass
class Document:

    content = str
    metadata : dict[str, str | int | float] = field(defualt_factory=dict)
    doc_id : str = ""

class DocumentLoader:


    SUPPORTED_EXTENSIONS : set[str] = {".txt", ".pdf", "docx", ".html"}

    def __init__(
            self,
            base_path: Path | str | None = None,
            recusive : bool = True,
            max_file_mb_size : float = 50.0,
            max_pdf_pages : int = 1000
    ) -> None:
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.recusive = recusive
        self.max_file_size_bytes = int(max_file_mb_size * 1024 * 1024)
        self.max_pdf_pages = max_pdf_pages

    def _load_pdf(self, file_path: Path | str) -> Document:
        
        if file_path.suffix.lower() == ".pdf":
            doc = pdf.open(file_path)
            out = open("output.txt","wb")
            for page in doc:
                text = page.get_text().encode("utf8")
                out.write(text)
                out.write(bytes((12,)))

            out.close()
            doc.close()

        return text

    def _load_text(self, file_path: Path | str) -> Document:

        if file_path.suffix.lower() == ".txt":
            file_path.read_text(encoding="utf-8", errors="replace")

    def _load_docx(self, file_path: Path | str) -> Document:

        if file_path.suffix.lower() == ".docx":
            doc = Doc(file_path)

            for paragraph in doc.paragraphs:
                print(paragraph.text)
            
    def _load_html(self, file_path: Path | str) -> Document:

        if file_path.suffix.lower() == ".html" | ".xml":
            soup = BS(file_path, "html.parser")

            print(soup.get_text())
        