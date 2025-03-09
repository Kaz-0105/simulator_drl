CREATE TABLE routes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL
);

INSERT INTO routes ("name") VALUES
('1:1:1'),
('3:1:1'),
('1:3:1'),
('1:1:3'),
('1:3:3'),
('3:1:3'),
('3:3:1');