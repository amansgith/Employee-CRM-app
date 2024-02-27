# Ecommerce-CRM-app
A Web App made with Python, Django and MySQL to manage Customer Details

The web app allows you to Perform all the CRUD Operations through the website directly.
It also uses Django's inbuilt authentication system for SignUp and Login.
It uses MySQL Database to Store and manage all the Customer Details.

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Python**: Make sure you have Python 3.x installed on your system.
2. **MySQL**: Install MySQL and set up a database for your app.

## Installation Steps

1. **Clone the Repository**:
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to clone the repository.
   - Run the following command to clone the repository:
     ```
     git clone https://github.com/your-username/your-repo.git
     ```

2. **Create a Virtual Environment** (optional but recommended):
   - Change into the project directory:
     ```
     cd your-repo
     ```
   - Create a virtual environment (if you haven't already):
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```
       source venv/bin/activate
       ```

3. **Install Dependencies**:
   - Install the required packages using pip:
     ```
     pip install -r requirements.txt
     ```

4. **Database Configuration**:
   - Create `.env` file using `.env.template` in your root folder.
   - Update the database details of your Local MySQL DB in the .env file

5. **Apply Migrations**:
   - Run the following commands to create database tables:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

6. **Run the Development Server**:
   - Start the development server:
     ```
     python manage.py runserver
     ```
   - Access the app in your browser at `http://127.0.0.1:8000/`.

And Voila!! you can see the app running

Feel free to customize the app further based on your requirements. Happy coding! 🚀
