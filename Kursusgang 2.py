import sqlite3

conn = sqlite3.connect('school.db')
c = conn.cursor()
c.execute('''CREATE TABLE Students
             (student_id INTEGER PRIMARY KEY,
              name TEXT,
              major TEXT)''')
c.execute('''CREATE TABLE Courses
             (course_id INTEGER PRIMARY KEY,
              course_name TEXT,
              instructor TEXT)''')
students_data = [(1, 'Emma Nielsen', 'AI'),
                 (2, 'Liam Jensen', 'Matematik'),
                 (3, 'Freja Larsen', 'Dansk'),
                 (4, 'Noah Pedersen', 'Informatik'),
                 (5, 'Ida Mikkelsen', 'Kemi')]
c.executemany('INSERT INTO Students VALUES (?, ?, ?)', students_data)
courses_data = [(1, 'PBL', 'Dr. Hansen'),
                (2, 'Kalkulus', 'Prof. Jensen'),
                (3, 'Kvantemekanik', 'Dr. Nielsen'),
                (4, 'Dansk', 'Prof. Mikkelsen'),
                (5, 'AI', 'Dr. Larsen')]
c.executemany('INSERT INTO Courses VALUES (?, ?, ?)', courses_data)
c.execute('''CREATE TABLE Enrollments
                (enrollment_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES Students(student_id),
                FOREIGN KEY(course_id) REFERENCES Courses(course_id))''')
enrollments_data = [(1, 1, 1),
                    (2, 2, 3),
                    (3, 3, 4),
                    (4, 4, 2),
                    (5, 5, 5)]
c.executemany('INSERT INTO Enrollments VALUES (?, ?, ?)', enrollments_data)
conn.commit()
conn.close()
