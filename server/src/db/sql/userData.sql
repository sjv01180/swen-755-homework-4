INSERT INTO Users (user_name, password, is_mod, session_id, last_login)
VAlUES 
('JaneFonda', '2cb5b4a611c7616308e2b74c6d8085829427b7098ab8f7e8e15508435fac6d3295a70780c029c414be39feb9270a85e963d76f0efd6bcc96cf0f85e243c7ee21', 'true', 'abcxyz', NOW()),
('JaneDoe', '2cb5b4a611c7616308e2b74c6d8085829427b7098ab8f7e8e15508435fac6d3295a70780c029c414be39feb9270a85e963d76f0efd6bcc96cf0f85e243c7ee21', 'false', 'efgxyz', NOW() - interval '1 day'),
('JekyllHyde', '2cb5b4a611c7616308e2b74c6d8085829427b7098ab8f7e8e15508435fac6d3295a70780c029c414be39feb9270a85e963d76f0efd6bcc96cf0f85e243c7ee21', 'false', 'hij123', NOW()),
('JohnDoe', '2cb5b4a611c7616308e2b74c6d8085829427b7098ab8f7e8e15508435fac6d3295a70780c029c414be39feb9270a85e963d76f0efd6bcc96cf0f85e243c7ee21', 'false', 'abc456', NOW());
-- for testing, the following is a hashed and salted rendition of password "123": '2cb5b4a611c7616308e2b74c6d8085829427b7098ab8f7e8e15508435fac6d3295a70780c029c414be39feb9270a85e963d76f0efd6bcc96cf0f85e243c7ee21'