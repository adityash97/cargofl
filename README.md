# cargofl
# Instruction is being updated.


For User:

Step 1:
To run server
python manage.py runserver

Step 2:
Visit link in browser : http://localhost:8000/ or The link came in terminal after running the server.

Step 3:
By default home page will be served ,
To add new employee click in "Add Employee"
To view a employee click on "eye" icon on left side in table.
Use 'Back To Manage Employee' to come to home screen after visiting any other page other than home.

For Admin:

Use endpoint '/admin' of the base url.
Example : 
If this is the url for home page http://localhost:8000/,
then to go to admin saction visit : http://localhost:8000/admin

Creditionals 
id : root
pass: 123


Note :
This app has 4 endpoints
1. '/' (home)
2. 'add/' (to add employee)
3. '1' (to view a employee details , 1 denotes the employee id of employee)
4. 'admin/'(for admin usage)
