CREATE TABLE road_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    road_id INTEGER NOT NULL,
    link_id INTEGER NOT NULL,
    link_type INTEGER NOT NULL
);

INSERT INTO road_tags (road_id, link_id, link_type) VALUES 
(1, 1, 1),
(1, 9, 2),
(1, 10000, 3),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(4, 10, 2),
(4, 10001, 3),
(5, 5, 1),
(5, 11, 2),
(5, 10002, 3),
(6, 6, 1),
(7, 7, 1),
(8, 8, 1),
(8, 12, 2),
(8, 10003, 3);