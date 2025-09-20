CREATE DATABASE IF NOT EXISTS atm_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE atm_demo;

CREATE TABLE accounts(
  account_id INT PRIMARY KEY AUTO_INCREMENT,
  account_no VARCHAR(32) UNIQUE NOT NULL,
  balance DECIMAL(12,2) NOT NULL DEFAULT 0
);

CREATE TABLE cards(
  card_no VARCHAR(32) PRIMARY KEY,
  account_id INT NOT NULL,
  pin_hash CHAR(64) NOT NULL,
  status ENUM('ACTIVE','BLOCKED') NOT NULL DEFAULT 'ACTIVE',
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE transactions(
  tx_id BIGINT PRIMARY KEY AUTO_INCREMENT,
  account_id INT NOT NULL,
  card_no VARCHAR(32) NOT NULL,
  atm_id INT NOT NULL,
  tx_type ENUM('WITHDRAW','DEPOSIT','TRANSFER') NOT NULL,
  amount DECIMAL(12,2) NOT NULL,
  balance_after DECIMAL(12,2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('SUCCESS','FAILED') NOT NULL,
  INDEX(account_id), INDEX(card_no),
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

INSERT INTO accounts(account_no,balance) VALUES ('ACCT-0001', 1000000.00);
-- pin demo: 1234 -> sha256
INSERT INTO cards(card_no,account_id,pin_hash,status)
VALUES ('CARD-0001', 1, '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'ACTIVE');

