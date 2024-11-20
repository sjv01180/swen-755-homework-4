-- Inserting sample messages into the Messages table
INSERT INTO Messages (user_id, user_name, msg_body, is_deleted)
VALUES 
  ((SELECT user_id FROM Users WHERE user_name = 'JaneFonda'), 'JaneFonda',  'Hello, how are you?', false),
  ((SELECT user_id FROM Users WHERE user_name = 'JaneDoe'), 'JaneDoe', 'Just wanted to check in.', false),
  ((SELECT user_id FROM Users WHERE user_name = 'JekyllHyde'), 'JekyllHyde', 'Meeting at 3 PM today.', false),
  ((SELECT user_id FROM Users WHERE user_name = 'JohnDoe'), 'JohnDoe', 'Did you complete the report?', false),
  ((SELECT user_id FROM Users WHERE user_name = 'JaneFonda'), 'JaneFonda', 'Reminder: Meeting tomorrow at 9 AM.', false),
  ((SELECT user_id FROM Users WHERE user_name = 'JaneDoe'), 'JaneDoe', 'Happy to help, just let me know!', false),
  ((SELECT user_id FROM Users WHERE user_name = 'JekyllHyde'), 'JekyllHyde', 'Can you send me the presentation slides?', false),
  ((SELECT user_id FROM Users WHERE user_name = 'JohnDoe'), 'JohnDoe', 'Lets grab lunch later.', false);
