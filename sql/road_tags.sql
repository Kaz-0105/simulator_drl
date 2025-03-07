CREATE TABLE road_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    road_id INTEGER NOT NULL,
    link_id INTEGER NOT NULL
);

INSERT INTO road_tags (road_id, link_id) VALUES 
(1, 1),
(1, 9),
(2, 2),
(3, 3),
(4, 4),
(4, 10),
(5, 5),
(5, 11),
(6, 6),
(7, 7),
(8, 8),
(8, 12);