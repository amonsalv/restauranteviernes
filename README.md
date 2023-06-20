# Restaurante Viernes

This is the official repository for Restaurante Viernes, a web application developed with Django.

## Description

Restaurante Viernes is an online platform for reserving tables at a restaurant. Users can explore the available schedules, select a convenient date and time, and make a reservation. The application also allows administrators to manage the reservations as well as the restaurant's menu and options.

## Features

- User registration: Users can create an account in the application to access reservation functionalities.
- Table reservation: Users can explore available schedules and select a date and time to make a reservation.
- Reservation management: Administrators can view and manage the made reservations, such as confirming, canceling, or modifying existing reservations.
- Menu administration: Administrators can add, edit, and delete items from the restaurant's menu.
- Restaurant options: Administrators can configure additional options for the restaurant, such as opening hours, maximum table capacity, etc.
- Payment integration: Users can make secure online payments to confirm their reservations.

## Technologies Used

- Django: A high-level web framework written in Python.
- Django Rest Framework: A third-party library for building RESTful APIs in Django.
- PostgreSQL: A relational database used to store the application's data.
- HTML/CSS: Markup languages used for the structure and styling of web pages.
- JavaScript: A programming language used for client-side interactivity.

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/amonsalv/restauranteviernes.git
   ```

2. Navigate to the project directory:

   ```shell
   cd restauranteviernes
   ```

3. Create and activate a virtual environment:

   ```shell
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Configure the database in the `settings.py` file. Make sure you have PostgreSQL installed and create a new database.

6. Perform the database migrations:

   ```shell
   python manage.py migrate
   ```

7. Start the development server:

   ```shell
   python manage.py runserver
   ```

8. Open your web browser and access `http://localhost:8000` to see the application in action.

## Contribution

If you would like to contribute to Restaurante Viernes, you can follow the steps below:

1. Fork this repository.
2. Create a new branch for your feature: `git checkout -b my-new-feature`.
3. Make the changes and commit descriptive commits.
4. Push your changes to your forked repository: `git push origin my-new-feature`.
5. Submit a Pull Request to this repository.

We appreciate your contributions and will ensure timely review.

## Contact

If you have any questions or suggestions, feel free to contact the Friday Restaurant development team at amonsalv7@gmail.com.

Thank you for using Restaurante Viernes! We hope you enjoy the application.
