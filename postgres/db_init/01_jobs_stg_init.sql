-- Create table_A if it does not exist

CREATE TABLE IF NOT EXISTS table_A (
    job_id SERIAL PRIMARY KEY,
    website TEXT,
    job_url	TEXT,
    job_url_direct TEXT,
    title TEXT,
    company TEXT,
    date_posted DATE,
    
);