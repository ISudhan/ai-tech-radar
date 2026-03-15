CREATE TABLE papers (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT UNIQUE NOT NULL,
    published_date TIMESTAMP,
    category TEXT,
    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT UNIQUE NOT NULL,
    source TEXT,
    published_date TIMESTAMP,
    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE repositories (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    url TEXT NOT NULL,
    description TEXT,
    language TEXT,
    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE repo_stats (
    id SERIAL PRIMARY KEY,
    repo_id INTEGER REFERENCES repositories(id),
    stars INTEGER,
    forks INTEGER,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE digests (
    id SERIAL PRIMARY KEY,
    digest_date DATE UNIQUE,
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);