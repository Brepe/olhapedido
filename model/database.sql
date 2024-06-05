CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email VARCHAR(255) NOT NULL, phone VARCHAR(20) NOT NULL, password VARCHAR(100) NOT NULL, name VARCHAR(100) NOT NULL);

CREATE TABLE IF NOT EXISTS plan (id SERIAL PRIMARY KEY, price DECIMAL(10, 2) NOT NULL, description TEXT, name VARCHAR(100));

CREATE TABLE IF NOT EXISTS company_admin (id SERIAL PRIMARY KEY, email VARCHAR(255) NOT NULL, password VARCHAR(100) NOT NULL, name VARCHAR(100) NOT NULL, level INT, phone VARCHAR(20), id_plan INT NOT NULL DEFAULT 1);

CREATE TABLE IF NOT EXISTS company (id SERIAL PRIMARY KEY, email VARCHAR(255) NOT NULL, phone VARCHAR(20) NOT NULL, register_name VARCHAR(100) NOT NULL, social_name VARCHAR(100) NOT NULL, type INT NOT NULL, cnpj VARCHAR(20) NOT NULL, cpf VARCHAR(20) NOT NULL, url VARCHAR(255) NOT NULL, id_company_admin INT);

CREATE TABLE IF NOT EXISTS address_user (id SERIAL PRIMARY KEY, cep VARCHAR(10) NOT NULL, lograd VARCHAR(100) NOT NULL, numero VARCHAR(10), complemento VARCHAR(30), bairro VARCHAR(50) NOT NULL, cidade VARCHAR(100) NOT NULL, estado VARCHAR(50) NOT NULL, pais VARCHAR(50) NOT NULL, id_user INT);

CREATE TABLE IF NOT EXISTS address_company (id SERIAL PRIMARY KEY, cep VARCHAR(10) NOT NULL, lograd VARCHAR(100) NOT NULL, numero VARCHAR(10), complemento VARCHAR(30), bairro VARCHAR(100) NOT NULL, cidade VARCHAR(100) NOT NULL, estado VARCHAR(50) NOT NULL, pais VARCHAR(50) NOT NULL, id_company INT);

CREATE TABLE IF NOT EXISTS layout (id SERIAL PRIMARY KEY, color VARCHAR(20) NOT NULL, linkImage VARCHAR(255) NOT NULL, linkTop VARCHAR(255) NOT NULL, bckg VARCHAR(255) NOT NULL, layout VARCHAR(50) NOT NULL, id_company INT);

CREATE TABLE IF NOT EXISTS product (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, description TEXT, stock INT DEFAULT 1, price DECIMAL(10, 2) NOT NULL, priceDisc DECIMAL(10, 2) NOT NULL, brand VARCHAR(50) NOT NULL, type VARCHAR(50) NOT NULL, photo VARCHAR(255) NOT NULL, video VARCHAR(255) NOT NULL, id_company INT);

CREATE TABLE IF NOT EXISTS purchase (id SERIAL PRIMARY KEY, dateCr DATE, message TEXT, price DECIMAL(10, 2) NOT NULL, status VARCHAR(20) NOT NULL, id_user INT, id_company INT);

CREATE TABLE IF NOT EXISTS product_purchase (id SERIAL PRIMARY KEY, image VARCHAR(255) NOT NULL, message TEXT, id_product INT, id_purchase INT);

CREATE TABLE IF NOT EXISTS promo (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, cupom VARCHAR(20) NOT NULL, value DECIMAL(10, 2) NOT NULL, percent DECIMAL(5, 2) NOT NULL, status VARCHAR(20) NOT NULL, dateStart DATE, dateEnd DATE, id_company INT, id_product INT);

CREATE TABLE IF NOT EXISTS subproduct_list (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, photo VARCHAR(255) NOT NULL, id_product INT);

CREATE TABLE IF NOT EXISTS subproduct (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, price DECIMAL(10, 2) NOT NULL, photo VARCHAR(255) NOT NULL, stock INT DEFAULT 1, id_subproduct_list INT);

CREATE TABLE IF NOT EXISTS company_calendar (id SERIAL PRIMARY KEY, type VARCHAR(50) NOT NULL, dateCr DATE, weekday VARCHAR(20) NOT NULL, id_company INT, id_product INT);

CREATE TABLE IF NOT EXISTS album (id SERIAL PRIMARY KEY, link VARCHAR(255) NOT NULL, type VARCHAR(50) NOT NULL, description TEXT, id_company INT);

CREATE TABLE IF NOT EXISTS chat (id SERIAL PRIMARY KEY, message TEXT, dateCr DATE, chatfrom VARCHAR(100) NOT NULL, chatto VARCHAR(100) NOT NULL, id_purchase INT, id_user INT, id_company INT);

ALTER TABLE company_admin ADD CONSTRAINT fk_users_id_plan FOREIGN KEY (id_plan) REFERENCES plan(id);
ALTER TABLE company ADD CONSTRAINT fk_company_id_company_admin FOREIGN KEY (id_company_admin) REFERENCES company_admin(id);
ALTER TABLE address_user ADD CONSTRAINT fk_address_user_id_user FOREIGN KEY (id_user) REFERENCES users(id);
ALTER TABLE address_company ADD CONSTRAINT fk_address_company_id_company FOREIGN KEY (id_company) REFERENCES company(id);
ALTER TABLE layout ADD CONSTRAINT fk_layout_id_company FOREIGN KEY (id_company) REFERENCES company(id);
ALTER TABLE product ADD CONSTRAINT fk_product_id_company FOREIGN KEY (id_company) REFERENCES company(id);
ALTER TABLE purchase ADD CONSTRAINT fk_purchase_id_user FOREIGN KEY (id_user) REFERENCES users(id);
ALTER TABLE purchase ADD CONSTRAINT fk_purchase_id_company FOREIGN KEY (id_company) REFERENCES company(id);
ALTER TABLE product_purchase ADD CONSTRAINT fk_product_purchase_id_product FOREIGN KEY (id_product) REFERENCES product(id);
ALTER TABLE product_purchase ADD CONSTRAINT fk_product_purchase_id_purchase FOREIGN KEY (id_purchase) REFERENCES purchase(id);
ALTER TABLE promo ADD CONSTRAINT fk_promo_id_company FOREIGN KEY (id_company) REFERENCES company(id);
ALTER TABLE promo ADD CONSTRAINT fk_promo_id_product FOREIGN KEY (id_product) REFERENCES product(id);
ALTER TABLE subproduct ADD CONSTRAINT fk_subproduct_id_subproduct_list FOREIGN KEY (id_subproduct_list) REFERENCES subproduct_list(id);
ALTER TABLE subproduct_list ADD CONSTRAINT fk_subproduct_list_id_product FOREIGN KEY (id_product) REFERENCES product(id);
ALTER TABLE company_calendar ADD CONSTRAINT fk_company_calendar_id_company FOREIGN KEY (id_company) REFERENCES company(id);
ALTER TABLE company_calendar ADD CONSTRAINT fk_company_calendar_id_product FOREIGN KEY (id_product) REFERENCES product(id);
ALTER TABLE album ADD CONSTRAINT fk_album_id_company FOREIGN KEY (id_company) REFERENCES company(id);
ALTER TABLE chat ADD CONSTRAINT fk_chat_id_purchase FOREIGN KEY (id_purchase) REFERENCES purchase(id);
ALTER TABLE chat ADD CONSTRAINT fk_chat_id_user FOREIGN KEY (id_user) REFERENCES users(id);
ALTER TABLE chat ADD CONSTRAINT fk_chat_id_company FOREIGN KEY (id_company) REFERENCES company(id);
