import psycopg2
from psycopg2 import sql


def create_database():
    conn = psycopg2.connect(
        host="localhost",
        database="fee_porject",
        user="postgres",
        password="bavya2007",
        port="5432"
    )

    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'fee_project'")
    exists = cursor.fetchone()

    if not exists:
        cursor.execute("CREATE DATABASE fee_project")
        print("Database created successfully")
    else:
        print("Database already exists")

    cursor.close()
    conn.close()


class FeeManagement:

    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="fee_project",
            user="postgres",
            password="bavya2007",
            port="5432"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                course VARCHAR(100) NOT NULL,
                total_fee INTEGER NOT NULL,
                paid_fee INTEGER NOT NULL
            )
        """)
        self.conn.commit()
        print("Table ready")

    def add_student(self):
        name = input("Enter student name: ")
        course = input("Enter course name: ")
        total_fee = int(input("Enter total fee: "))
        paid_fee = int(input("Enter paid fee: "))

        if paid_fee > total_fee:
            print("Paid fee cannot be greater than total fee")
            return

        query = """
            INSERT INTO students (name, course, total_fee, paid_fee)
            VALUES (%s, %s, %s, %s)
        """

        self.cursor.execute(query, (name, course, total_fee, paid_fee))
        self.conn.commit()

        print("Student added successfully")

    def view_students(self):
        self.cursor.execute("SELECT * FROM students ORDER BY id")
        students = self.cursor.fetchall()

        if not students:
            print("No students found")
            return

        print("\n--- Student List ---")

        for student in students:
            pending_fee = student[3] - student[4]

            print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} | "
                f"Course: {student[2]} | "
                f"Total Fee: {student[3]} | "
                f"Paid Fee: {student[4]} | "
                f"Pending Fee: {pending_fee}"
            )

    def pay_fee(self):
        student_id = int(input("Enter student ID: "))
        amount = int(input("Enter paying amount: "))

        self.cursor.execute(
            "SELECT paid_fee, total_fee FROM students WHERE id = %s",
            (student_id,)
        )

        student = self.cursor.fetchone()

        if student is None:
            print("Student not found")
            return

        paid_fee = student[0]
        total_fee = student[1]

        new_paid_fee = paid_fee + amount

        if new_paid_fee > total_fee:
            print("Amount is greater than pending fee")
            return

        self.cursor.execute(
            "UPDATE students SET paid_fee = %s WHERE id = %s",
            (new_paid_fee, student_id)
        )

        self.conn.commit()

        print("Fee paid successfully")

    def pending_students(self):
        self.cursor.execute("""
            SELECT * FROM students
            WHERE paid_fee < total_fee
            ORDER BY id
        """)

        students = self.cursor.fetchall()

        if not students:
            print("No pending fee students")
            return

        print("\n--- Pending Fee Students ---")

        for student in students:
            pending_fee = student[3] - student[4]

            print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} | "
                f"Course: {student[2]} | "
                f"Pending Fee: {pending_fee}"
            )

    def delete_student(self):
        student_id = int(input("Enter student ID to delete: "))

        self.cursor.execute(
            "DELETE FROM students WHERE id = %s",
            (student_id,)
        )

        self.conn.commit()

        if self.cursor.rowcount == 0:
            print("Student not found")
        else:
            print("Student deleted successfully")

    def close(self):
        self.cursor.close()
        self.conn.close()


def main():
    create_database()

    app = FeeManagement()

    while True:
        print("\n====== Student Fee Management ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Pay Fee")
        print("4. Pending Fee Students")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            app.add_student()

        elif choice == "2":
            app.view_students()

        elif choice == "3":
            app.pay_fee()

        elif choice == "4":
            app.pending_students()

        elif choice == "5":
            app.delete_student()

        elif choice == "6":
            app.close()
            print("Thank you")
            break

        else:
            print("Invalid choice")


main()