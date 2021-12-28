import sqlite3

try:
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    cursor.execute("""CREATE TABLE IF NOT EXISTS IT_Company(
       ID_company INT PRIMARY KEY,
       Name_company TEXT,
       Foundation_year INT,
       Specialization TEXT);
    """)
    sqlite_connection.commit()

    cursor.execute("""INSERT INTO IT_Company(ID_company, Name_company, Foundation_year, Specialization)
       VALUES(1, 'Dell Technologies', 1984, 'Production of computers');""")
    sqlite_connection.commit()

    cursor.execute("""INSERT INTO IT_Company(ID_company, Name_company, Foundation_year, Specialization)
               VALUES(2, 'IBM', 1911, 'Software');""")
    sqlite_connection.commit()

    cursor.execute("""INSERT INTO IT_Company(ID_company, Name_company, Foundation_year, Specialization)
               VALUES(3, 'Cisco Systems', 1984, 'Network equipment');""")
    sqlite_connection.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Founder(
           ID_founder INT PRIMARY KEY,
           Founder_name TEXT,
           Career INT,
           ID_company INT);
        """)
    sqlite_connection.commit()

    cursor.execute("""INSERT INTO Founder(ID_founder, Founder_name, Career, ID_company)
       VALUES(1, 'Michael Dell', 'Businessman', 1);""")
    sqlite_connection.commit()

    cursor.execute("""INSERT INTO Founder(ID_founder, Founder_name, Career, ID_company)
        VALUES(2, 'Charles Flint', 'Businessman', 2);""")
    sqlite_connection.commit()

    cursor.execute("""INSERT INTO Founder(ID_founder, Founder_name, Career, ID_company)
        VALUES(3, 'Sandra Lerner', 'Businesswoman', 3);""")
    sqlite_connection.commit()

    cursor.execute("""INSERT INTO Founder(ID_founder, Founder_name, Career, ID_company)
        VALUES(4, 'Leonard Bosak', 'Businessman', 3);""")
    sqlite_connection.commit()

    cursor.execute("SELECT * FROM Founder WHERE Founder.id_company = 1;")
    one_result = cursor.fetchone()
    print(one_result)

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")