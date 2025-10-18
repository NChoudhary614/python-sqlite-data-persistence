# 🗄️ Data Persistence Project with Python & SQLite

A beginner-friendly Python project to **store**, **backup** 🗃️, and **restore** ♻️ user and transaction data using SQLite. Perfect for demos, internships, and learning real-world development!

---

## 📦 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- 👤 **Store** user data and transactions with SQLite
- 🛡️ **Prevent duplicates**—unique emails enforced
- ⚡ **One-command** backup and restore
- 🧩 **Modular** folder structure and maintainable code
- ✔️ Runs on any OS with Python installed

---

## 🗂️ Project Structure

data_persistent_project/
├── database/
│ ├── init.py
│ ├── models.py
│ ├── database.py
├── backups/
├── main.py
├── requirements.txt
├── README.md


---

## 🚀 Getting Started

### 1. Clone this Repository
git clone https://github.com/NChoudhary/data_persistent_project.git
cd data_persistent_project


### 2. (Optional) Set up a Virtual Environment
python -m venv venv

On Windows
venv\Scripts\activate

On Linux/macOS
source venv/bin/activate



### 3. Run the Application
python main.py


---

## 🧠 How It Works

- **`database/models.py`** — Table schemas for users & transactions 📑
- **`database/database.py`** — All database functions, backup/restore 🗃️
- **`main.py`** — Main script with sample inserts and backups 🖥️
- **`backups/`** — Automatically saved database backups ⏳

---

## 📝 Example Output

User with email alice@example.com already exists.
User with email bob@example.com already exists.
[(1, 250.5, '2025-10-18'), (2, 99.99, '2025-10-18')]
Backup created: backups/company_data_backup_YYYYMMDD_HHMMSS.db


---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss improvements.

---

## 📜 License

MIT

---

> ⭐ **Star this repository if it helped you or you found it useful!**
