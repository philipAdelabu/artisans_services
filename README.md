# Skills Artisan Service Provider Backend
This a backend to produce api consumption to the frontend. The project is writting in python and django backend. I made use of the ruling king of django api provider "Djangorestframework". It is an expressive framewrok that simplifies API sterilization and desterilization. 

## The necessary tools to dowload are: 
 1. python
 2. django : this should be installed within a virtual environment
 3. djangorestframework: this as well should be installed within a virtual environment.
 4. Pillow is install to manage image files
 5. Sqlite3 is install to help manage db store in the db.sqlite3 database

 ## Creating some necessary apps
  python3 manage.py startapp artisanapi 

  1. These models are created:
     - users
     - providers
     - sellers
     - services
     - bookings
     - payments
     - orders
     - reviews
     - ratings
     - cart_items
     - sys_logs
     - feedback
     - histories
  2. sterializers.py is created to handle all the models serialization
  3. Migration is done: python3 manage.py makemigrations
      - Migration is applied to help creates all the necessary tables in the database by using the class models in the models.py file.
  
  `python3 manage.py makemigratioins`
  `python3 manage.py migrate`
  


