KT :
1)
-Understanding Django flow and integrations 
-Introduction to ORM 
Starting 34 min and resume again at 1hr :46 min
https://youtu.be/OTmQOjsl0eg?si=QUQl0hUi7RVnYqwE

2) 
- ORM integration and data retrieval 
a ) https://www.youtube.com/watch?v=5g_xIwxLSJk&t=744s
b ) https://youtube.com/playlist?list=PL-2EBeDYMIbTT7ri4pNEBu9VoVSAkOvd2&si=FqY9vimq0pG0N2J0 (first 5 video s) 

Online DB services (free) 
https://console.aiven.io/account/a4f8c27028ac/project/sathvikt23-58ab/services

3) 
Invoking REST APIs and local Deployment (till docker ) 
https://youtu.be/cJveiktaOSQ?si=tt64fh43rytuKSuz

https://youtu.be/t-uAgI-AUxc?si=aLgdTg7gnz0wk6OH

--------------------------------------------
SET UP : 
Create venv + Sync in One Step with uv
bash
uv venv
This creates a .venv folder (just like python -m venv .venv).

Activate the virtual environment
On Linux/macOS:
bash
source .venv/bin/activate
On Windows:
cmd
.venv\Scripts\activate
Then sync dependencies from uv.lock
uv sync
uv will auto-detect .venv/bin/python or .venv\Scripts\python.exe — no need to pass --python if .venv is activated or exists

----------------------------------------
Run Django project :
Navigate to the Django project folder (where manage.py exists), then:

a. Apply migrations:
bash
python manage.py migrate
b. Run the development server:
python manage.py runserver

Create a superuser (optional, for admin panel)
python manage.py createsuperuser

Collect static files (for production, optional)
python manage.py collectstatic

Optional: Regenerate uv.lock after editing pyproject.toml
uv pip compile
