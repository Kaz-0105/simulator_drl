CREATE TABLE roads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vissim_file_id INTEGER NOT NULL,
);

INSERT INTO roads (vissim_file_id, order_id)
VALUES (1, 0);