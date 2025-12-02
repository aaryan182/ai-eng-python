# B- Redis ( rediSearch vector field + hybrid)

# pip install redis

from redis import Redis
import numpy as np
import json
import os

r = Redis(host="localhost", port=6379)  # default Redis port

#create index(one-time) with vector field

# Example using HNSW vector field + text:

def create_index():
    r.ft("idx_docs").create_index(
        fields=[
            redis.commands.search.field.TextField("text"),
            redis.commands.search.field.VectorField(
                "vector",
                "HNSW",
                {
                    "TYPE": "FLOAT32",
                    "DIM": 768,
                    "DISTANCE_METRIC": "COSINE"
                }
            )
        ]
    )

# Example uses FT.CREATE 

# upsert : store metadata + vector in HASH
def upsert_redis(doc_id, text, embedding, metadata):
    key = f"doc:{doc_id}"

    r.hset(
        key,
        mapping={
            "text": text,
            "metadata": json.dumps(metadata),
            "vector": np.array(embedding, dtype=np.float32).tobytes(),
        }
    )

# Query: perform vector search with FT.SEARCH 
# Hybrid Search (BM25 + Vector Search)

def redis_query(query_text, query_emb, top_k=5):
    query = (
        f'(@text:"{query_text}")=>[KNN {top_k} @vector $vec AS score]'
    )

    params = {"vec": np.array(query_emb, dtype=np.float32).tobytes()}

    result = r.ft("idx_docs").search(
        query,
        query_params=params,
        sort_by="score",
        dialect=2
    )

    return result


# Example Usage
create_index()

upsert_redis(
    doc_id="1",
    text="Redis vector search example",
    embedding=[0.1, 0.2, 0.3] * 256,  # 768-dim example
    metadata={"source": "test"}
)

res = redis_query("vector", [0.1, 0.2, 0.3] * 256)
print(res.docs)
