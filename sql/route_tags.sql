CREATE TABLE route_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_id INTEGER NOT NULL,
    "order" INTEGER NOT NULL,
    relative_volume REAL NOT NULL
);

INSERT INTO route_tags (route_id, "order", relative_volume) VALUES
(1, 1, 1), (1, 2, 1), (1, 3, 1),
(2, 1, 3), (2, 2, 1), (2, 3, 1),
(3, 1, 1), (3, 2, 3), (3, 3, 1),
(4, 1, 1), (4, 2, 1), (4, 3, 3),
(5, 1, 1), (5, 2, 3), (5, 3, 3),
(6, 1, 3), (6, 2, 1), (6, 3, 3),
(7, 1, 3), (7, 2, 3), (7, 3, 1);