# # from sentence_transformers import SentenceTransformer


# # class EmbeddingService:

# #     def __init__(self, model_name:str = "all-MiniLM-L6-v2"):
# #         self.model = SentenceTransformer(model_name)

# #     def embed(self, text: str):
# #         return self.model.encode(text)

# # Priya's minimal domain embedding trainer
# # CSV format: query, passage, score  (score in [0, 1])

# from sentence_transformers import SentenceTransformer, InputExample, losses
# from torch.utils.data import DataLoader
# import csv, math, random

# MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # fast baseline
# BATCH_SIZE = 32
# EPOCHS = 3
# WARMUP = 250

# def load_pairs(csv_path):
#     ex = []
#     with open(csv_path, newline='', encoding="utf-8") as f:
#         reader = csv.reader(f)
#         for q, p, s in reader:
#             try:
#                 score = float(s)
#             except:
#                 score = 1.0
#             ex.append(InputExample(texts=[q, p], label=score))
#     random.shuffle(ex)
#     return ex

# train_examples = load_pairs("annual-enterprise-survey-2025-financial-year-provisional.csv")
# model = SentenceTransformer(MODEL_NAME)

# # Contrastive objective (CosineSimilarityLoss works well for pairwise scoring)
# train_loader = DataLoader(train_examples, batch_size=BATCH_SIZE, shuffle=True)
# loss_fn = losses.CosineSimilarityLoss(model)

# warmup_steps = min(WARMUP, math.ceil(len(train_loader) * EPOCHS * 0.1))

# model.fit(
#     train_objectives=[(train_loader, loss_fn)],
#     epochs=EPOCHS,
#     warmup_steps=warmup_steps,
#     show_progress_bar=True,
# )

# model.save("models/domain-emb-v1")


from sentence_transformers import SentenceTransformer

class EmbeddingService():

    def __init__(self, model : str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model)

    def embed(self, text : str):
        return self.model.encode(text)