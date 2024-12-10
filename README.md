# **Project Setup for Django To-Do List Application**

This guide walks you through the steps to set up and run the Django-based to-do list application. The project allows users to add new tasks and view a list of tasks.

---

## **Prerequisites**

Before starting, make sure you have the following installed:

- **Python** 3.10 or later
- **Pip** (Python package installer)
- **Git** (for cloning the repository)
- **Virtual Environment** (optional but recommended for managing dependencies)

---

## **Steps for Setting Up the Project**

### 1. **Clone the Repository**

First, clone the repository to your local machine:

```bash
git clone https://github.com/ridzRUSH/django_todo.git
```

This will create a local copy of the project in the current directory.

### 2. **Create and Activate a Virtual Environment (Optional but Recommended)**

Creating a virtual environment ensures that the project dependencies are isolated and won't conflict with other Python projects on your machine.

#### For **Windows**:

```bash
python -m venv env
env\Scripts\activate
```

#### For **macOS/Linux**:

```bash
python3 -m venv env
source env/bin/activate
```

Once the virtual environment is activated, you'll see `(env)` in your command prompt or terminal.

### 3. **Install Dependencies**

Install the project dependencies using `pip` from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install Django and any other dependencies needed to run the project.

### 4. **Apply Database Migrations**

The project uses SQLite by default, which is the default database in Django. To set up the database, apply the migrations:

```bash
python manage.py migrate
```

This will create the necessary database tables for the project.

### 5. **Run the Development Server**

Start the Django development server by running:

```bash
python manage.py runserver
```

This will start the server on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### 6. **Access the Application**

Open a web browser and visit the following URLs:

- **Task List Page:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Add Task Page:** [http://127.0.0.1:8000/add/](http://127.0.0.1:8000/add/)

On the **Add Task Page**, you can add new tasks, and on the **Task List Page**, you can view the tasks.

---


## **Common Commands**

Here are some useful Django commands that you might need during development:

- **Start the server**:  
  ```bash
  python manage.py runserver
  ```

- **Create migrations for changes in models**:  
  ```bash
  python manage.py makemigrations
  ```

- **Apply migrations**:  
  ```bash
  python manage.py migrate
  ```

