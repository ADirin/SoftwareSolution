import mysql.connector as mariadb
#connect to datbase server
mariadb_connection = mariadb.connect(user='root', password ='Test1234', database ='test_database',  host = '127.0.0.1', port = '3308' )
# create an instance of connecter
create_cursor = mariadb_connection.cursor() #dictionary = True
#create new db
#create_cursor.execute("CREATE DATABASE test_database")
#then just make querry about the exisitin database and print it
#create_cursor.execute("show databases")
    #for x in create_cursor:
        #print(x)
 # as we have already created the data base we just comments the other comment and add the newely created db in the list
 #........password ='Test1234', database ='test_database',  host = '127.0.0.1...........
 #Create  a table
#create_cursor.execute("CREATE TABLE python_creation_table (column1 VARCHAR(2), column2 INT)")
 #show tables
#create_cursor.execute("SHOW TABLES")
#for x in create_cursor:
#    print(x)
#Add items to the table which there are two ways
# Hard coded (1 WAY)
# sql_statement = 'INSERT INTO python_creation_table (column1,column2) VALUES ("hi", 1), ("hi", 2)';
# create_cursor.execute(sql_statement)
# #MYSQL is not auto commit so we have to do it...
# mariadb_connection.commit();
# The second OPTIONS (2 WAY) subsitute value with %s based on the number of field we add the %s
# sql_statement = 'INSERT INTO python_creation_table (column1,column2) VALUES (%s, %s)';
# items_to_insert = ('hi', 4)
# create_cursor.execute(sql_statement, items_to_insert)
# mariadb_connection.commit();
# We check if the data is already in the database
# sql_statment = 'SELECT * from python_creation_table'
# create_cursor.execute(sql_statment)
#fecthall download all but it is also possible to fecthon
# myresult = create_cursor.fetchall() # fetchone()
# print(myresult)

###USer Where  thwew is not any three so nothing wikk be there
# sql_statement= 'SELECT * from python_creation_table where column2 = 4'
# create_cursor.execute(sql_statement)
# myresult = create_cursor.fetchall()
# print(myresult)


## More complicated querru like sum of the items
# sql_statement= 'SELECT sum(column2) as sum_col_2 from python_creation_table where column2 < 4 group by column2 order by 1'
# create_cursor.execute(sql_statement)
# myresult = create_cursor.fetchall()
# print(myresult)
mariadb_connection.close()