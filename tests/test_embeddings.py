from src.embeddings.service import embed_query


vector = embed_query(
    "CUDA is a parallel computing platform."
)


print("TYPE:")
print(type(vector))

print("\nVECTOR DIMENSIONS:")
print(len(vector))

print("\nFIRST 10 VALUES:")
print(vector[:10])