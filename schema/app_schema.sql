CREATE TABLE IF NOT EXISTS apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    category VARCHAR(255),
    author VARCHAR(255) NOT NULL,
    version VARCHAR(16) NOT NULL,
    icon_path VARCHAR(255),
    path VARCHAR(255),
    installed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS executable_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    app_id INTEGER,
    option_name VARCHAR(512),
    path VARCHAR(1024),
    execution_type VARCHAR(32),
    instructions TEXT,
    FOREIGN KEY (app_id) REFERENCES apps(id)
);