CREATE TABLE route_sets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    num_roads INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT
);

INSERT INTO route_sets (num_roads, "name", "description") VALUES
(4, 'all_111', '全ての流入道路の経路選択が1:1:1'),
(4, 'all_311', '全ての流入道路の経路選択が3:1:1'),
(4, 'all_131', '全ての流入道路の経路選択が1:3:1'),
(4, 'all_113', '全ての流入道路の経路選択が1:1:3'),
(4, 'all_133', '全ての流入道路の経路選択が1:3:3'),
(4, 'all_313', '全ての流入道路の経路選択が3:1:3'),
(4, 'all_331', '全ての流入道路の経路選択が3:3:1');