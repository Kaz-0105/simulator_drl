CREATE TABLE intersection_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    intersection_id INTEGER NOT NULL,
    road_id INTEGER NOT NULL,
    "order" INTEGER NOT NULL,
    "type" INTEGER NOT NULL
);

INSERT INTO intersection_tags (intersection_id, road_id, "order", "type") VALUES 
(1, 1, 4, 1),
(1, 2, 2, 2),
(1, 3, 4, 2),
(1, 4, 2, 1),
(1, 5, 1, 1),
(1, 6, 3, 2),
(1, 7, 1, 2),
(1, 8, 3, 1);
