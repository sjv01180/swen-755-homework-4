DROP TABLE IF EXISTS Messages CASCADE;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v4();

CREATE TABLE Messages (
    message_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID,
    user_name varchar(100), 
    msg_body varchar(100),
    is_deleted BOOLEAN DEFAULT false,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES Users(user_id) 
        ON DELETE CASCADE
);