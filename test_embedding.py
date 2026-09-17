# from app.embeddings.service import EmbeddingService
# import numpy as np

# embedding_service = EmbeddingService()

# texts = [
#     "من یک لپ تاپ خریدم",
#     "من یک کامپیوتر قابل حمل خریدم",
#     "امروز هوا بسیار گرم است"
# ]

# vectors = []

# for text in texts:
#     vector = embedding_service.embed(text)
#     vectors.append(vector)

# similarity_1_2 = np.dot(vectors[0],vectors[1])
# similarity_1_3 = np.dot(vectors[0],vectors[2])


# print("Similarity 1-2:", similarity_1_2)
# print("Similarity 1-3:", similarity_1_3)

# magnitude_1 = np.linalg.norm(vectors[0])
# magnitude_2 = np.linalg.norm(vectors[1])
# magnitude_3 = np.linalg.norm(vectors[2])

# print("Magnitude 1:", magnitude_1)
# print("Magnitude 2:", magnitude_2)
# print("Magnitude 3:", magnitude_3)

# cosine_1_2 = np.dot(vectors[0],vectors[1]) / (
#     np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[1])
# )

# cosine_1_3 = np.dot(vectors[0],vectors[2]) / (
#     np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[2])
# )

# print("Cosine Similarity 1-2:", cosine_1_2)
# print("Cosine Similarity 1-3:", cosine_1_3)


# texts = [
#     "شرایط بازگرداندن کالا تا هفت روز پس از خرید امکان پذیر است.",
#     "هزینه ارسال سفارش بر اساس وزن بسته محاسبه می‌شود.",
#     "تمام محصولات دارای یک سال گارانتی هستند.",
#     "برای پرداخت می‌توانید از کارت بانکی استفاده کنید.",
#     "در صورت خرابی محصول می‌توانید درخواست تعویض ثبت کنید."
# ]

# query = "چند روز فرصت دارم تا کالایی را که خریداری کرده ام پس بدهم؟"

# document_vector = []
# query_vector = embedding_service.embed(query)

# for text in texts:
#     vector = embedding_service.embed(text)
#     document_vector.append(vector)

# results = []

# for text, vector in zip(texts, document_vector):

#     similarity = np.dot(query_vector, vector)

#     results.append((text, similarity))

# # results.sort(key=lambda x: x[1], reverse=True)

# k = 3

# top_k = results[:k]

# print("\nTop-K Results:")


# for text, similarity in top_k:
#     print(similarity, "->", text)


from app.embeddings.service import EmbeddingService
import numpy as np
import pymupdf

embedding_service = EmbeddingService()
texts = []
query = None
query_vector = None
vectors = {}
vector = None
threshold = 5
k = 5
# highest_similarity = None
# answer = None


texts = [
    "How do I reset my password?",
    "How long does shipping take?",
    "What is your return policy?",
    "Do you ship internationally?",
    "How can I track my order?",
    "How do I change my email address?",
    "Can I cancel my order?",
    "How can I contact customer support?",
    "What payment methods do you accept?",
    "How do I create an account?",
    "Why has my order not arrived yet?",
    "Can I change my shipping address?",
    "How do I get a refund?",
    "Is my personal information secure?",
    "How can I update my account information?"
]

query = input("what can i help you ? ...\n" )
query_vector = embedding_service.embed(query)


vectors = {
    "text": [],
    "vector": []
}

for text in texts:
    vector = embedding_service.embed(text)
    vectors["text"].append(text)
    vectors["vector"].append(vector)

# highest_similarity = -1
# answer = None

result = []

for i,vector in enumerate(vectors["vector"]):
     
    tmp_cos_sim = np.dot(query_vector, vector) / (
    np.linalg.norm(query_vector) * np.linalg.norm(vector)
    )

    if tmp_cos_sim >= threshold :
        result.append((vectors["text"][i], tmp_cos_sim))

    # if tmp_cos_sim > highest_similarity:
    #     highest_similarity = tmp_cos_sim
    #     answer = vectors["text"][i]

result.sort(key=lambda x: x[1], reverse=True)

for i in range(k):
    print(f"\n- {i + 1} result is {result[i][0]} by score : {result[i][1]}")


