CREATE TABLE roads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vissim_file_id INTEGER NOT NULL,
    main_link_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL
);

INSERT INTO roads (vissim_file_id, main_link_id, order_id)
VALUES (1, 7, 0);