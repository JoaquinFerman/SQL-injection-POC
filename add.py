import sqlite3

# Por si acaso aca te dejo la creacion de las tablas

con = sqlite3.connect("news.db")
cur = con.cursor()

cur.execute("CREATE TABLE noticias(id, titulo, cuerpo)")

cur.execute("""
    INSERT INTO noticias VALUES
        ('1', 'A Vicky Xipolitakis se le escapa una...', 'Por que seguis leyendo viejo verde?'),
        ('2', 'Valeria Lynch pierde la voz momentos antes de su concierto', 'Señora de Don Bosco decepcionada, prende fuego el movistar arena'),
        ('3', 'Joita aprende a hacer inyecciones sql', 'Agradecimientos especiales a chat gpt por hacerle el html')
""")

cur.execute("CREATE TABLE users(username, password)")

cur.execute("""
    INSERT INTO users VALUES
        ('moebius', 'linuxis4nerds'),
        ('lockdown', 'machaterN1')
""")

con.commit()
con.close()