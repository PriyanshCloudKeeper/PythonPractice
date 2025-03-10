# export DB_USER=my_db_user
# echo =$DB_USER
# But this is temp and only valid for the session


import os

db_user = os.getenv("DB_USER")
print(db_user)

# We can use a .env file to get secrets


