# A - Pinecone ( Upsert + Query )

# pip install "pinecone-client"

from pinecone import Pinecone
import os

# Initialize Pinecone (v3 syntax)
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "my-doc-index"
index = pc.Index(index_name)

# -------------------------
# UPSERT BATCH
# -------------------------
def upsert_batch(items):
    # items → list of {id, embedding, metadata}
    vectors = [
        {
            "id": it["id"],
            "values": it["embedding"],
            "metadata": it["metadata"]
        }
        for it in items
    ]

    index.upsert(vectors=vectors)
    print("Upserted:", len(vectors))


# -------------------------
# QUERY
# -------------------------
def pinecone_query(query_emb, top_k=5, namespace=None):
    res = index.query(
        vector=query_emb,
        top_k=top_k,
        include_metadata=True,
        namespace=namespace
    )
    return res["matches"]
