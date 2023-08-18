-- make_vector_table
CREATE TABLE IF NOT EXISTS vector_table (
    id SERIAL PRIMARY KEY,
    vector CLOB NOT NULL
);
-- get_point_by_id
SELECT vector
FROM vector_table
WHERE id == {0};
-- delete_point_by_id
DELETE FROM vector_table
WHERE id == {0};
-- add_point
INSERT INTO vector_table
