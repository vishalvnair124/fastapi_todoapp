# ✅ FastAPI Todo App

A simple and minimal **FastAPI**-based Todo web application that allows you to create, view, and manage tasks.

---

## 🚀 Features

- 📋 Create, read, update, and delete tasks (CRUD)
- 🧠 Built with **FastAPI** – high performance, easy to use
- 🖥️ Templated frontend using Jinja2 and HTML
- 🗃️ SQLite database connection
- 📦 Lightweight and beginner-friendly

---

## 🗂️ Project Structure

```
fastapi_todoapp/
│
├── app.py           # Main FastAPI application
├── conn.py          # Database connection logic
├── templates/       # HTML templates (Jinja2)
├── env/             # Environment/virtualenv folder
├── __pycache__/     # Compiled Python files
└── README.md        # Project documentation
```

---

## ⚙️ How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/vishalvnair124/fastapi_todoapp.git
cd fastapi_todoapp
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv env
source env/bin/activate           # On Windows: env\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install fastapi uvicorn jinja2
```

4. **Run the app:**

```bash
uvicorn app:app --reload
```

5. **Open in browser:**

```
http://127.0.0.1:8000
```

---

## 🧑‍💻 Tech Stack

| Component     | Technology    |
|---------------|---------------|
| Backend       | FastAPI       |
| Frontend      | HTML + Jinja2 |
| Database      | SQLite        |
| Server        | Uvicorn       |
| Language      | Python        |

---

## 🧠 Future Enhancements

- 🔐 User authentication
- 🗓️ Due dates and priorities
- 📱 Responsive design with Tailwind or Bootstrap
- 📊 Task statistics dashboard

---

## 👨‍💻 Made With ❤️ By

**Vishal V Nair**  
🚀 MCA @ TKM | Tech Enthusiast  
🔧 Skilled in FastAPI | Python | Web Dev  
📫 GitHub: [@vishalvnair124](https://github.com/vishalvnair124)
