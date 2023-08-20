-- make_vector_table
CREATE TABLE IF NOT EXISTS VECTOR_TABLE (
    id SERIAL PRIMARY KEY,
    vector CLOB NOT NULL
);
-- get_point_by_id
SELECT vector
FROM VECTOR_TABLE
WHERE id == {0};
-- delete_point_by_id
DELETE FROM VECTOR_TABLE
WHERE id == {0};
-- add_point
INSERT INTO VECTOR_TABLE
VALUES ({0}, {1});
