-- Create table_A if it does not exist

CREATE TABLE IF NOT EXISTS joblistings (
    job_id SERIAL PRIMARY KEY,
    website TEXT,
    job_url TEXT NOT NULL,
    job_url_direct TEXT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    date_posted DATE,
    job_description TEXT NOT NULL,
    company_industry TEXT,
    company_url TEXT,
    company_num_employees TEXT,
    company_description TEXT
);