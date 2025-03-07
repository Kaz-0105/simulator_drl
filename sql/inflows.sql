CREATE TABLE inflows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    vissim_file_id INTEGER NOT NULL,
    description TEXT
);

INSERT INTO inflows (name, vissim_file_id, description) 
VALUES ('均衡型', 1, '全ての道路が等しい流入量を持つ');
