
# 🛠️ Django Project Setup + Knowledge Transfer Notes

## 📚 KT (Knowledge Transfer)

### 1) Django Basics
- Understanding Django flow and integrations
- Introduction to ORM
- Watch from 34 min to 1hr:46min:  
  https://youtu.be/OTmQOjsl0eg?si=QUQl0hUi7RVnYqwE

### 2) ORM Integration and Data Retrieval
- ORM Integration & Data Retrieval – Video A:  
  https://www.youtube.com/watch?v=5g_xIwxLSJk&t=744s
- ORM Series – Playlist (Watch first 5 videos):  
  https://youtube.com/playlist?list=PL-2EBeDYMIbTT7ri4pNEBu9VoVSAkOvd2&si=FqY9vimq0pG0N2J0

#### Free Online DB Services
- Aiven Console:  
  https://console.aiven.io/account/a4f8c27028ac/project/sathvikt23-58ab/services

### 3) REST API Invocation & Local Deployment (till Docker)
- API & Deployment – Part 1:  
  https://youtu.be/cJveiktaOSQ?si=tt64fh43rytuKSuz
- API & Deployment – Part 2:  
  https://youtu.be/t-uAgI-AUxc?si=aLgdTg7gnz0wk6OH

---

## ⚙️ Django Project Setup Using `uv`

### 1. Create and Activate Virtual Environment

Create `.venv` using `uv`:

```bash
uv venv
```

Activate it:

- On Linux/macOS:
  ```bash
  source .venv/bin/activate
  ```

- On Windows:
  ```cmd
  .venv\Scripts\activate
  ```

### 2. Sync Dependencies from `uv.lock`

```bash
uv sync
```

This will install all dependencies from `uv.lock`.

---

## 🚀 Run Django Project

Navigate to the Django project directory (where `manage.py` exists).

### Apply Migrations

```bash
python manage.py migrate
```

### Start the Development Server

```bash
python manage.py runserver
```

---

## 👤 Optional Commands

### Create Superuser (for Django Admin)

```bash
python manage.py createsuperuser
```

### Collect Static Files (for Production)

```bash
python manage.py collectstatic
```

---

## 🔄 Update Lock File (if you modify dependencies)

If you modify `pyproject.toml` and want to regenerate the lock file:

```bash
uv pip compile
```

---

📌 Make sure the following files exist in your project root:
- `.venv/`
- `uv.lock`
- `pyproject.toml`
