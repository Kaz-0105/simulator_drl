CREATE TABLE inflow_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    inflow_id INTEGER NOT NULL,
    vehicle_input_id INTEGER NOT NULL,
    volume REAL NOT NULL
);

INSERT INTO inflow_tags (inflow_id, vehicle_input_id, volume)
VALUES (1, 4, 700); 