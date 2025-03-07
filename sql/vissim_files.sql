/* テーブルの作成 */
CREATE TABLE vissim_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    inpx_file_name TEXT NOT NULL,
    layx_file_name TEXT NOT NULL,
    path TEXT NOT NULL,
    description TEXT
);

/* データの追加のひな型 */
INSERT INTO vissim_files (name, inpx_file_name, layx_file_name, path, description) 
VALUES ('二車線一交差点', 'network.inpx', 'network.layx', '/layout/two_lane', '2車線道路で構成される1交差点のネットワーク');