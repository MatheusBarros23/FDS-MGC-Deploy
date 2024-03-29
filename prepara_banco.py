import MySQLdb

# Defina a função init_database
def prepara_banco():
    print('Conectando...')
    conn = MySQLdb.connect(user='root', passwd='@admin07', host='127.0.0.1', port=3306)

    # Descomente se quiser desfazer o banco...
    conn.cursor().execute("DROP DATABASE IF EXISTS `MyGamingCritics`;")
    conn.commit()

    criar_tabelas = '''SET NAMES utf8;
        CREATE DATABASE `MyGamingCritics` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
        USE `MyGamingCritics`;
        CREATE TABLE `jogo` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `nome` varchar(50) COLLATE utf8_bin NOT NULL,
          `categoria` varchar(40) COLLATE utf8_bin NOT NULL,
          `console` varchar(20) NOT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
        CREATE TABLE `usuario` (
          `id` varchar(8) COLLATE utf8_bin NOT NULL,
          `nome` varchar(20) COLLATE utf8_bin NOT NULL,
          `senha` varchar(8) COLLATE utf8_bin NOT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

    conn.cursor().execute(criar_tabelas)

    # inserindo usuarios
    cursor = conn.cursor()
    cursor.executemany(
          'INSERT INTO MyGamingCritics.usuario (id, nome, senha) VALUES (%s, %s, %s)',
          [
                ('Suares', 'Matheus Soares', '5432'),
                ('arkim', 'Lucas Barros', '1234'),
                ('Dzr', 'Luiz Eduardo', 'sport03'),
                ('Kryno', 'Matheus Barros', '4321'),

          ])

    cursor.execute('select * from MyGamingCritics.usuario')
    print(' -------------  Usuários:  -------------')
    for user in cursor.fetchall():
        print(user[1])

    # inserindo jogos
    cursor.executemany(
          'INSERT INTO MyGamingCritics.jogo (nome, categoria, console) VALUES (%s, %s, %s)',
          [
                ('God of War 4', 'Ação', 'PS4'),
                ('NBA 2k18', 'Esporte', 'Xbox One'),
                ('Rayman Legends', 'Indie', 'PS4'),
                ('Super Mario RPG', 'RPG', 'SNES'),
                ('Super Mario Kart', 'Corrida', 'SNES'),
                ('Fire Emblem Echoes', 'Estratégia', '3DS'),
          ])

    cursor.execute('select * from MyGamingCritics.jogo')
    print(' -------------  Jogos:  -------------')
    for jogo in cursor.fetchall():
        print(jogo[1])

    # commitando senão nada tem efeito
    conn.commit()
    cursor.close()