# Install
# pip install psycopg2-binary pgvector

import psycopg2, json, os
from pgvector.psycopg2 import register_vector

conn = psycopg2.connect(os.getenv("DATABASE_URL"))
register_vector(conn)
cur = conn.cursor()


# Create Table (fix: add UNIQUE constraint)

# We must declare:

# doc_id TEXT UNIQUE

# Otherwise upsert will throw error:

# there is no unique or exclusion constraint matching the ON CONFLICT specification


cur.execute("""
CREATE TABLE IF NOT EXISTS docs (
    id serial PRIMARY KEY,
    doc_id text UNIQUE,
    content text,
    embedding vector(1536),
    metadata jsonb
);
"""
)

conn.commit()


# 2) Upsert Function (works now because doc_id is UNIQUE)

def upsert_pg(doc_id, content, embedding, metadata):
    cur.execute("""
        INSERT INTO docs (doc_id, content, embedding, metadata)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (doc_id) DO UPDATE
            SET content = EXCLUDED.content,
                embedding = EXCLUDED.embedding,
                metadata = EXCLUDED.metadata;
    """, (doc_id, content, embedding, json.dumps(metadata)))
    
conn.commit()


# 3) Query Function 

def pg_query(query_emb, top_k = 5):
    cur.execute("""
        SELECT
            doc_id, 
            content,
            metadata,
            embedding <==> %s AS distance
        FROM docs
        ORDER BY embedding <=> %s
        LIMIT %s;
    """, (query_emb, query_emb, top_k))

    return cur.fetchall()