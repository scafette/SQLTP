import sqlite3

conn = sqlite3.connect('database.sql')
cursor = conn.cursor()

# Création des tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS CLIENT (
    ID_CLIENT INTEGER PRIMARY KEY,
    NOM TEXT,
    PRENOM TEXT,
    TELEPHONE TEXT,
    EMAIL TEXT,
    DATE_NAISSANCE DATE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ADRESS (
    ID_ADRESS INTEGER PRIMARY KEY,
    ID_CLIENT INTEGER,
    ADRESSE TEXT,
    VILLE TEXT,
    CODE_POSTAL TEXT,
    PAYS TEXT,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS PRODUCT (
    ID_PRODUCT INTEGER PRIMARY KEY,
    NOM TEXT,
    DESCRIPTION TEXT,
    PRIX REAL,
    STOCK INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS CART (
    ID_CART INTEGER PRIMARY KEY,
    ID_CLIENT INTEGER,
    DATE_ACHAT DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS COMMANDE (
    ID_COMMANDE INTEGER PRIMARY KEY,
    ID_CLIENT INTEGER,
    DATE_COMMANDE DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS commerce_product (
    ID_COMMERCE_PRODUCT INTEGER PRIMARY KEY,
    ID_CART INTEGER,
    ID_PRODUCT INTEGER,
    ID_COMMANDE INTEGER,
    QUANTITY INTEGER,
    FOREIGN KEY (ID_CART) REFERENCES CART(ID_CART),
    FOREIGN KEY (ID_COMMANDE) REFERENCES COMMANDE(ID_COMMANDE),
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS INVOICE (
    ID_INVOICE INTEGER PRIMARY KEY,
    ID_COMMANDE INTEGER,
    DATE_FACTURE DATE,
    FOREIGN KEY (ID_COMMANDE) REFERENCES COMMANDE(ID_COMMANDE)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS PHOTO (
    ID_PHOTO INTEGER PRIMARY KEY,
    ID_PRODUCT INTEGER,
    URL TEXT,
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS PAIMENT (
    ID_PAIMENT INTEGER PRIMARY KEY,
    ID_CLIENT INTEGER,
    ID_INVOICE INTEGER,
    DATE_PAIMENT DATE,
    ID_MODE_PAIMENT INTEGER,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT),
    FOREIGN KEY (ID_INVOICE) REFERENCES INVOICE(ID_INVOICE),
    FOREIGN KEY (ID_MODE_PAIMENT) REFERENCES MODE_PAIMENT(ID_MODE_PAIMENT)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS MODE_PAIMENT (
    ID_MODE_PAIMENT INTEGER PRIMARY KEY,
    NOM TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS RATE (
    ID_RATE INTEGER PRIMARY KEY,
    ID_PRODUCT INTEGER,
    RATE INTEGER,
    ID_CLIENT INTEGER,
    COMMENT TEXT,
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT),
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
);
''')


clients = [
    (1, 'Martin', 'Paul', '0612345678', 'paul.martin@example.com', '1980-01-01'),
    (2, 'Dupont', 'Marie', '0623456789', 'marie.dupont@example.com', '1985-05-12'),
    (3, 'Durand', 'Clara', '0634567890', 'clara.durand@example.com', '1990-08-22'),
    (4, 'Petit', 'Henri', '0645678901', 'henri.petit@example.com', '1978-09-14'),
    (5, 'Moreau', 'Sophie', '0656789012', 'sophie.moreau@example.com', '1995-11-30')
]

cursor.executemany('''
INSERT INTO CLIENT (ID_CLIENT, NOM, PRENOM, TELEPHONE, EMAIL, DATE_NAISSANCE)
VALUES (?, ?, ?, ?, ?, ?);
''', clients)

adresses = [
    (1, 1, '1 rue de l\'église', 'Paris', '75001', 'France'),
    (2, 2, '2 rue de la mairie', 'Lyon', '69000', 'France'),
    (3, 3, '3 avenue de la République', 'Marseille', '13000', 'France'),
    (4, 4, '4 boulevard des Capucines', 'Toulouse', '31000', 'France'),
    (5, 5, '5 impasse des Lilas', 'Bordeaux', '33000', 'France')
]

cursor.executemany('''
INSERT INTO ADRESS (ID_ADRESS, ID_CLIENT, ADRESSE, VILLE, CODE_POSTAL, PAYS)
VALUES (?, ?, ?, ?, ?, ?);
''', adresses)

products = [
    (1, 'MacBook Air', 'Ordinateur portable', 1200.0, 15),
    (2, 'Dell XPS 13', 'Ordinateur portable', 1100.0, 8),
    (3, 'Lenovo ThinkPad', 'Ordinateur portable', 950.0, 5),
    (4, 'HP Spectre', 'Ordinateur portable', 1400.0, 12),
    (5, 'Asus ZenBook', 'Ordinateur portable', 1000.0, 10)
]

cursor.executemany('''
INSERT INTO PRODUCT (ID_PRODUCT, NOM, DESCRIPTION, PRIX, STOCK)
VALUES (?, ?, ?, ?, ?);
''', products)

photos = [
    (1, 1, 'https://example.com/macbook.jpg'),
    (2, 2, 'https://example.com/dellxps.jpg'),
    (3, 3, 'https://example.com/thinkpad.jpg'),
    (4, 4, 'https://example.com/hpspectre.jpg'),
    (5, 5, 'https://example.com/zenbook.jpg')
]

cursor.executemany('''
INSERT INTO PHOTO (ID_PHOTO, ID_PRODUCT, URL)
VALUES (?, ?, ?);
''', photos)

carts = [
    (1, 1, '2024-11-01'),
    (2, 2, '2024-11-02'),
    (3, 3, '2024-11-03'),
    (4, 4, '2024-11-04'),
    (5, 5, '2024-11-05')
]

cursor.executemany('''
INSERT INTO CART (ID_CART, ID_CLIENT, DATE_ACHAT)
VALUES (?, ?, ?);
''', carts)

commandes = [
    (1, 1, '2024-11-10'),
    (2, 2, '2024-11-12'),
    (3, 3, '2024-11-14'),
    (4, 4, '2024-11-16'),
    (5, 5, '2024-11-18')
]

cursor.executemany('''
INSERT INTO COMMANDE (ID_COMMANDE, ID_CLIENT, DATE_COMMANDE)
VALUES (?, ?, ?);
''', commandes)

commerce_products = [
    (1, 1, 1, 1, 2),
    (2, 2, 2, 2, 1),
    (3, 3, 3, 3, 3),
    (4, 4, 4, 4, 1),
    (5, 5, 5, 5, 2)
]

cursor.executemany('''
INSERT INTO commerce_product (ID_COMMERCE_PRODUCT, ID_CART, ID_PRODUCT, ID_COMMANDE, QUANTITY)
VALUES (?, ?, ?, ?, ?);
''', commerce_products)

invoices = [
    (1, 1, '2024-11-11'),
    (2, 2, '2024-11-13'),
    (3, 3, '2024-11-15'),
    (4, 4, '2024-11-17'),
    (5, 5, '2024-11-19')
]

cursor.executemany('''
INSERT INTO INVOICE (ID_INVOICE, ID_COMMANDE, DATE_FACTURE)
VALUES (?, ?, ?);
''', invoices)

modes_paiement = [
    (1, 'Carte Bancaire'),
    (2, 'Paypal'),
    (3, 'Chèque'),
    (4, 'Espèces')
]

cursor.executemany('''
INSERT INTO MODE_PAIMENT (ID_MODE_PAIMENT, NOM)
VALUES (?, ?);
''', modes_paiement)

paiements = [
    (1, 1, 1, '2024-11-12', 1),
    (2, 2, 2, '2024-11-14', 2),
    (3, 3, 3, '2024-11-16', 3),
    (4, 4, 4, '2024-11-18', 4),
    (5, 5, 5, '2024-11-20', 1)
]

cursor.executemany('''
INSERT INTO PAIMENT (ID_PAIMENT, ID_CLIENT, ID_INVOICE, DATE_PAIMENT, ID_MODE_PAIMENT)
VALUES (?, ?, ?, ?, ?);
''', paiements)

rates = [
    (1, 1, 5, 1, 'Excellent produit, très satisfait.'),
    (2, 2, 4, 2, 'Bon produit, mais quelques défauts.'),
    (3, 3, 3, 3, 'Produit moyen, peut mieux faire.'),
    (4, 4, 5, 4, 'Très bon produit, je recommande.'),
    (5, 5, 2, 5, 'Déçu par la qualité.')
]

cursor.executemany('''
INSERT INTO RATE (ID_RATE, ID_PRODUCT, RATE, ID_CLIENT, COMMENT)
VALUES (?, ?, ?, ?, ?);
''', rates)

conn.commit()
conn.close()
