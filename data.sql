DELETE FROM oas_api_app_item_tags;
DELETE FROM oas_api_app_tag_related_tags;
DELETE FROM oas_api_app_item;
DELETE FROM oas_api_app_tag;
DELETE FROM oas_api_app_user;
DELETE FROM oas_api_app_admin;

INSERT INTO oas_api_app_tag (name, created_date, updated_date, prime_color) VALUES
('Yu-Gi-Oh', '2024-12-26', '2024-12-26', '#ff4081'),
('Common', '2024-12-26', '2024-12-26', '#607d8b'),
('Rare', '2024-12-26', '2024-12-26', '#ff9800'),
('Super Rare', '2024-12-26', '2024-12-26', '#9c27b0'),
('Ultra Rare', '2024-12-26', '2024-12-26', '#3f51b5'),
('Secret Rare', '2024-12-26', '2024-12-26', '#c2185b'),
('Starlight Rare', '2024-12-26', '2024-12-26', '#8e24aa'),
('Ghost Rare', '2024-12-26', '2024-12-26', '#00bcd4'),
('Prismatic Secret Rare', '2024-12-26', '2024-12-26', '#ff5722'),
('Ultimate Rare', '2024-12-26', '2024-12-26', '#9e9e9e'),
('Monster', '2024-12-26', '2024-12-26', '#4caf50'),
('Spell', '2024-12-26', '2024-12-26', '#f44336'),
('Trap', '2024-12-26', '2024-12-26', '#ffeb3b');

INSERT INTO oas_api_app_tag_related_tags (from_tag_id, to_tag_id) VALUES
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Common')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Rare')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Super Rare')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Ultra Rare')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Secret Rare')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Starlight Rare')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Ghost Rare')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Prismatic Secret Rare')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Ultimate Rare')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Monster')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Spell')),
((SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh'), (SELECT id FROM oas_api_app_tag WHERE name = 'Trap'));

INSERT INTO oas_api_app_user (id, username, email, password, address, phone, avatar_url, created_date, updated_date, payment_info) VALUES
('d9e779353fc64ac48e8c3eae1c4725a5', 'johndoe', 'johndoe@example.com', '$2b$12$8WjZFF7U8DHS.PhjCtBXDuIbGOkVA2fHHjtAi6UF/KSf9OhknyjMW', '123 Main St', '123-456-7890', '', '2024-12-26', '2024-12-26', '4003830171874018 727'),
('ad6b3f9cd3bb4686bfae40e33b33c6c9', 'eliza', 'eliza@example.com', '$2b$12$8WjZFF7U8DHS.PhjCtBXDuIbGOkVA2fHHjtAi6UF/KSf9OhknyjMW', '101 Elm St', '555-123-4567', 'https://www.guiltygear.com/ggst/en/wordpress/wp-content/uploads/2020/09/archive_ram-1.jpg', '2024-12-26', '2024-12-26', '5496198584584769 130'),
('9e1f76a05e204a6b9a8321b3030b824d', 'galaxy', 'galaxy@example.com', '$2b$12$8WjZFF7U8DHS.PhjCtBXDuIbGOkVA2fHHjtAi6UF/KSf9OhknyjMW', '789 Galaxy Rd', '555-555-5555', 'https://toquoc.mediacdn.vn/280518851207290880/2021/9/3/base64-1630595438805599368242-1630639676186-1630639676357733744119.png', '2024-12-26', '2024-12-26', '4111111111111111 230');

INSERT INTO oas_api_app_item (id, name, image_url, description, start_price, step, end_date, user_id, status, created_date, updated_date) VALUES
('30f9c9d4413747cd9e961b6db6d8ac98', 'Blue-Eyes White Dragon', 'https://images.ygoprodeck.com/images/cards/89631139.jpg', 'A legendary dragon that is a powerful symbol of strength.', 115000000, 2000000, '2024-12-31', '9e1f76a05e204a6b9a8321b3030b824d', 0, '2024-12-26', '2024-12-26'),
('bafbd7d7c65f45c0bb2c63ad877249b7', 'Dark Magician', 'https://images.ygoprodeck.com/images/cards/46986414.jpg', 'The ultimate wizard in terms of attack and defense.', 80000000, 1500000, '2024-12-31', '9e1f76a05e204a6b9a8321b3030b824d', 0, '2024-12-26', '2024-12-26'),
('e86d75e307fa4e8f9f56c01a4ef6f5cc', 'Exodia the Forbidden One', 'https://images.ygoprodeck.com/images/cards/33396948.jpg', 'When all five pieces of Exodia are assembled, victory is assured.', 200000000, 5000000, '2024-12-31', '9e1f76a05e204a6b9a8321b3030b824d', 0, '2024-12-26', '2024-12-26'),
('a1d3843d80d9415b85c73b88d8b0c7ad', 'Summoned Skull', 'https://images.ygoprodeck.com/images/cards/70781052.jpg', 'A fearsome monster with high attack points.', 70000000, 1000000, '2024-12-31', '9e1f76a05e204a6b9a8321b3030b824d', 0, '2024-12-26', '2024-12-26'),
('4fcb9b99ae4d47d1888f933efaddffde', 'Blue-Eyes Ultimate Dragon', 'https://images.ygoprodeck.com/images/cards/23995346.jpg', 'A fusion of three Blue-Eyes White Dragons, extremely powerful.', 350000000, 7000000, '2024-12-31', 'ad6b3f9cd3bb4686bfae40e33b33c6c9', 0, '2024-12-26', '2024-12-26'),
('592634a67c144a3a922c40a2859a42de', 'Red-Eyes Black Dragon', 'https://images.ygoprodeck.com/images/cards/74677422.jpg', 'A powerful dragon known for its fiery breath.', 90000000, 2000000, '2024-12-31', 'ad6b3f9cd3bb4686bfae40e33b33c6c9', 0, '2024-12-26', '2024-12-26'),
('d3f7b169b9be48b993b47db0ec2b9c98', 'Dark Paladin', 'https://images.ygoprodeck.com/images/cards/98502113.jpg', 'A fusion monster with high attack and the ability to negate spell cards.', 120000000, 2500000, '2024-12-31', 'ad6b3f9cd3bb4686bfae40e33b33c6c9', 0, '2024-12-26', '2024-12-26');

INSERT INTO oas_api_app_item_tags (item_id, tag_id) VALUES
('30f9c9d4413747cd9e961b6db6d8ac98', (SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh')),
('30f9c9d4413747cd9e961b6db6d8ac98', (SELECT id FROM oas_api_app_tag WHERE name = 'Ultra Rare')),
('bafbd7d7c65f45c0bb2c63ad877249b7', (SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh')),
('bafbd7d7c65f45c0bb2c63ad877249b7', (SELECT id FROM oas_api_app_tag WHERE name = 'Ultra Rare')),
('e86d75e307fa4e8f9f56c01a4ef6f5cc', (SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh')),
('e86d75e307fa4e8f9f56c01a4ef6f5cc', (SELECT id FROM oas_api_app_tag WHERE name = 'Secret Rare')),
('a1d3843d80d9415b85c73b88d8b0c7ad', (SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh')),
('a1d3843d80d9415b85c73b88d8b0c7ad', (SELECT id FROM oas_api_app_tag WHERE name = 'Common')),
('4fcb9b99ae4d47d1888f933efaddffde', (SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh')),
('4fcb9b99ae4d47d1888f933efaddffde', (SELECT id FROM oas_api_app_tag WHERE name = 'Ultra Rare')),
('592634a67c144a3a922c40a2859a42de', (SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh')),
('592634a67c144a3a922c40a2859a42de', (SELECT id FROM oas_api_app_tag WHERE name = 'Rare')),
('d3f7b169b9be48b993b47db0ec2b9c98', (SELECT id FROM oas_api_app_tag WHERE name = 'Yu-Gi-Oh')),
('d3f7b169b9be48b993b47db0ec2b9c98', (SELECT id FROM oas_api_app_tag WHERE name = 'Ultra Rare')),
('d3f7b169b9be48b993b47db0ec2b9c98', (SELECT id FROM oas_api_app_tag WHERE name = 'Monster'));

INSERT INTO oas_api_app_admin (username, password) VALUES
('admin727', '$2b$12$8WjZFF7U8DHS.PhjCtBXDuIbGOkVA2fHHjtAi6UF/KSf9OhknyjMW');
