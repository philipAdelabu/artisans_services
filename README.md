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
     1. users
     2. providers
     3. sellers
     4. services
     5. bookings
     6. payments
     7. orders
     8. reviews
     9. ratings
     10. cart_items
     11.  sys_logs
     12. feedback
     13. histories
  2. sterializers.py is created to handle all the models serialization
  3. Migration is done: python3 manage.py makemigrations
      - Migration is applied to help creates all the necessary tables in the database by using the class models in the models.py file.
  
  `python3 manage.py makemigratioins`
  `python3 manage.py migrate`


  --- 

  ## The flow of service provision

   1. You must first become a user by have a login account.
   2. You must apply as a service provider with the following
      1. user_account, 
      2. company_name, 
      3. description, 
      4. specialization
   3. Then provide a services. 


  ## The API for the artisans app 

  GET     /api/v1/users/     -> get the list of the users 
  GET     /api/vi/users/1/   -> get a user with id 1
  DELETE  /api/vi/users/1/    -> delete the user with id 1
  


