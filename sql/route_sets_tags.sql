CREATE TABLE route_sets_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_set_id INTEGER NOT NULL,
    "order" INTEGER NOT NULL,
    route_id INTEGER NOT NULL
);

INSERT INTO route_sets_tags (route_set_id, "order", route_id) VALUES
(1, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1),
(2, 1, 2), (2, 2, 2), (2, 3, 2), (2, 4, 2),
(3, 1, 3), (3, 2, 3), (3, 3, 3), (3, 4, 3),
(4, 1, 4), (4, 2, 4), (4, 3, 4), (4, 4, 4),
(5, 1, 5), (5, 2, 5), (5, 3, 5), (5, 4, 5),
(6, 1, 6), (6, 2, 6), (6, 3, 6), (6, 4, 6),
(7, 1, 7), (7, 2, 7), (7, 3, 7), (7, 4, 7);