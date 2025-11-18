# PROJECT
A Django web application for tracking failures, projects, parts, and processes. Built as an internship project.

## Features

- CRUD operations for Projects, Parts, Processes, and Failures
- Search and filter projects by name, description, or date
- Responsive template inheritance using `base.html` for consistent navigation and UI
- Confirmation popups for delete actions
- Dashboard view with summary statistics
- Bulk import/export support (CSV/XLS via Django admin or custom views)
- User permissions (login required for edit/delete operations)
- Neatly organized codebase for easy maintenance and deployment

## Setup Instructions

1. **Install Python 3.**  
   Download and install from [python.org](https://python.org).

2. **Install dependencies:**  
   Open terminal, navigate to your project folder, and run: pip install -r requirements.txt
3. **Apply database migrations:**
      python manage.py makemigrations
      python manage.py migrate
4. **Create a superuser (optional, for admin access):**
    python manage.py createsuperuser
5. **Run the server:**
     python manage.py runserver
 Open your browser and go to:
      http://127.0.0.1:8000/projects/

   
## Usage

- Use the navigation bar to switch between Projects, Parts, Processes, and Failures.
- Add, edit, and delete records for each module.
- Use the search box to find projects.
- Only authenticated users can edit/delete.
- Go to `/admin/` for full database export/import or admin actions.

---

## Deployment

To deploy on a cloud service (Heroku, Render, etc.), see instructions for setting up Postgres and configuring Django settings, or ask the developer for help.

---

## Important Notes

- Do **NOT** upload your local `venv/` or `db.sqlite3` to GitHub.
- A `.gitignore` file is included to prevent unwanted files from being tracked.
- For persistent online use, connect Django to a cloud Postgres database.

---

     
   
