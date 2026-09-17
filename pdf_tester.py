from app.embeddings.service import EmbeddingService
import pymupdf
import numpy as np


embedding_service = EmbeddingService()

doc = pymupdf.open("AI (RAG).pdf")
out = open("output.txt","wb")
for page in doc:
    text = page.get_text().encode("utf8")
    out.write(text)
    out.write(bytes((12,)))

out.close()
doc.close()

if pymupdf.Document.is_pdf == True:
    print("Hello World")

text_vector = embedding_service.embed(str(text))

print(text_vector.shape)

print()