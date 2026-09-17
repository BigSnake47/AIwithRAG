text = """
The return policy allows customers to return a product within seven days.
The customer must return the product in good condition and without using it.
The shipping cost for the return will be covered by the store.
"""

# words = text.split()

# chunk_size = 5
# overlap = 2

# chunks = []

# start = 0

# while start < len(words):

#     end = start + chunk_size

#     chunk = words[start:end]

#     chunks.append(" ".join(chunk))

#     start += chunk_size - overlap


# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i + 1}:")
#     print(chunk)
#     print()



words = text.split()

chunk_size = 5
overlap = 2

chunks = []

start = 0

while start < len(words):
    end = start + chunk_size

    chunk = words[start:end]

    chunks.append(" ".join(chunk))

    start += chunk_size - overlap


for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}")
    print(chunk)
    print()
