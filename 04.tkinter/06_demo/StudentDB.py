import sqlite3

def create_student(student):
    conn = sqlite3.connect('dbuniversidad.db')
    c = conn.cursor()
    c.execute("INSERT INTO estudiantes VALUES (?,?,?, ?)",
              (student.matricula, student.nombres, student.apellidos,student.promedio))
    conn.commit()
    conn.close()

def select_student(matricula):
    conn = sqlite3.connect("dbuniversidad.db")
    c = conn.cursor()
    c.execute('SELECT * FROM estudiantes WHERE matricula = ?', (matricula,))
    student = c.fetchone()
    conn.close()
    return student

def update_promed(matricula, promedio):
    conn = sqlite3.connect("dbuniversidad.db")
    c = conn.cursor()
    c.execute("UPDATE estudiantes SET promedio = ? WHERE matricula = ?", (promedio, matricula))
    conn.commit()
    conn.close()

def delete_student(matricula):
    conn = sqlite3.connect("dbuniversidad.db")
    c = conn.cursor()
    c.execute("DELETE FROM estudiantes WHERE matricula = ?", (matricula,))
    conn.commit()
    conn.close()

def select_all():
    conn = sqlite3.connect("dbuniversidad.db")
    c = conn.cursor()
    c.execute("SELECT * FROM estudiantes")
    estudiantes = c.fetchall()
    conn.close()
    return estudiantes