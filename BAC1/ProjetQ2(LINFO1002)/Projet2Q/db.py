import sqlite3


def data(file_path):
    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()
    result = cursor.execute("SELECT username, grade FROM submissions WHERE task= 'Fibonacci' and course = 'LSINF1101-PYTHON' ")
    tache = []
    grades = []
    i = 0
    for row in result:
        tache.append(row[0])
        grades.append(row[1])
        i += 1
        if i == 100:
            break


    connection.close()
    return [tache, grades]
