-- make_vector_table
CREATE TABLE IF NOT EXISTS vector_table (
    id SERIAL PRIMARY KEY,
    vector DOUBLE[]
);
