Employee Management System (Django)

📌 Features

- Add Employee
- Edit Employee
- Delete Employee
- Search functionality (by name or ID)
- Employee table view using django_tables2
- Pagination support (auto-enabled when records exceed limit)
- Preloaded data using fixtures

---

🛠️ Tech Stack

- Django
- HTML, CSS (Flexbox)
- Bootstrap
- django-tables2

---

🚀 Setup Instructions

1️⃣ Clone the repository

git clone <your-repo-url>
cd mypro

2️⃣ Create virtual environment

python -m venv env
env\Scripts\activate   # Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Apply migrations

python manage.py migrate

5️⃣ Load fixtures (sample data)

python manage.py loaddata <fixture_file_name>.json

6️⃣ Run the server

python manage.py runserver

---
Fixtures

- Sample employee data is provided using Django fixtures
- This helps quickly populate the database for testing
- Located inside the app’s "fixtures/" folder

---

📊 Notes

- Pagination is implemented using django-tables2
- It becomes visible when records exceed the configured limit (e.g., 20 per page)

---

👩‍💻 Author

Aishwarya P