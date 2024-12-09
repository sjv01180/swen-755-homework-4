-- Drop table if it already exists
DROP TABLE IF EXISTS Users CASCADE;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v4();

-- Create table
CREATE TABLE Users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_name varchar(100),
    password char(128),
    is_mod BOOLEAN DEFAULT false, -- key is referenced for user management from admin
    session_id char(256),
    last_login DATE -- REFACTORED BREAKER: SESSION EXPIRATION MANAGEMENT (database-side) 
);