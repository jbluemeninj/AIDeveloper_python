import sqlite3
from Student import Student

conn = sqlite3.connect('dbuniversidad.db')
c = conn.cursor()
# c.execute("""CREATE TABLE IF NOT EXISTS estudiantes(
#   matricula TEXT PRIMARY KEY,
#   nombres TEXT NOT NULL,
#   apellidos TEXT NOT NULL, 
#  promedio REAL)""")

# c.execute("INSERT INTO estudiantes VALUES('112','ROBERTO','CRUZ', 9.5)")
# c.execute("INSERT INTO estudiantes VALUES('113','JUAN','CRUZ', 19.5)")
# c.execute("INSERT INTO estudiantes VALUES('114','VICTOR','CRUZ', 18.5)")
# st1 =  Student('114', 'EDISON','FLORES','8.9')
# st2 =  Student('115', 'PAOLO','GUERRERO','10.9')

# c.execute("INSERT INTO estudiantes VALUES(?,?,?,?)", 
#           (st1.matricula,st1.nombres,st1.apellidos,st1.promedio))
# c.execute("INSERT INTO estudiantes VALUES(:matricula, :nombres, :apellidos, :promedio)", {
#     'matricula':st2.matricula,'nombres':st2.nombres, 'apellidos':st2.apellidos,'promedio':st2.matricula
# })

# students = [
# ('117', 'ANDY','POLO','10.9'),
# ('118', 'PAOLO','HURTADO','11.9')
# ]
# c.executemany("INSERT INTO estudiantes VALUES (?,?,?,?)", students)
conn.commit()

st3 =  Student('119', 'ROBERTO','PALACIOS','12.9')

def create(student):
    c.execute("INSERT INTO estudiantes VALUES (?,?,?, ?)",
              (student.matricula, student.nombres, student.apellidos,student.promedio))
    conn.commit()

create(st3)

c.execute('SELECT * FROM estudiantes')
estudiantes = c.fetchall()
print(estudiantes)

conn.close()


