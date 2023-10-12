import pandas as pd
import pyodbc
import mysql.connector
from mysql.connector import Error

# https://www.projectpro.io/recipes/connect-mysql-python-and-import-csv-file-into-mysql-and-create-table
data_1 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Address.csv')
data_2 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Buyers.csv')
data_3 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Categories.csv')
data_4 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Credit_Cards.csv')
data_5 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Local_Vendors.csv')
data_6 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Orders.csv')
data_7 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Product_Listing.csv')
data_8 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Ratings.csv')
data_9 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Reviews.csv')
data_10 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Sellers.csv')
data_11 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Users.csv')
data_12 = pd.read_csv('NittanyMarketDataset-v8/NittanyMarketDataset-v8/Zipcode_info.csv')

df1 = pd.DataFrame(data_1)
print(df1)
df2 = pd.DataFrame(data_2)
print(df2)
df3 = pd.DataFrame(data_3)
print(df3)
df4 = pd.DataFrame(data_4)
print(df4)
df5 = pd.DataFrame(data_5)
print(df5)
df6 = pd.DataFrame(data_6)
print(df6)
df7 = pd.DataFrame(data_7)
print(df7)
df8 = pd.DataFrame(data_8)
print(df8)
df9 = pd.DataFrame(data_9)
print(df9)
df10 = pd.DataFrame(data_10)
print(df10)
df11 = pd.DataFrame(data_11)
print(df11)
df12 = pd.DataFrame(data_12)
print(df12)

# try:
connection = mysql.connector.connect(host='localhost',
                                     database='kexi',
                                     user='root',
                                     password='336336xx')
if connection.is_connected():
    cursor = connection.cursor()
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)

    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

    # print("1Address table")
    # # address_id, zipcode, street_num, street_name
    # cursor.execute("CREATE TABLE address_data(address_id varchar(255),primary key(address_id),zipcode int,street_num int,street_name varchar(255))")
    # for i, row in df1[50:].iterrows():
    #     # here %S means string values
    #     sql = "INSERT INTO kexi.address_data VALUES (%s,%s,%s,%s)"
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()
    #
    # print("2buyers table")
    # # email,first_name,last_name,gender,age,home_address_id,billing_address_id
    # cursor.execute("CREATE TABLE buyers_data(email varchar(255),primary key(email),first_name varchar(255),last_name varchar(255),gender varchar(25),age int, home_address_id varchar(255),billing_address_id varchar(255))")
    # for i, row in df2[0:30].iterrows():
    #     # here %S means string values
    #     sql = "INSERT INTO kexi.buyers_data VALUES (%s,%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()
    #
    # print("3categories table")
    # # parent_category, category_name
    # cursor.execute("CREATE TABLE categories_data(primary key(category_name),parent_category varchar(255),category_name varchar(255))")
    # for i, row in df3[100:].iterrows():
    #     sql = "INSERT INTO kexi.categories_data VALUES (%s,%s)"
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()
    #
    # print("4credit_cards table")
    # # credit_card_num,card_code,expire_month,expire_year,card_type,Owner_email
    # cursor.execute("CREATE TABLE credit_cards_data(primary key(credit_card_num), credit_card_num varchar(255),card_code int,expire_month int,expire_year int, card_type varchar(100),Owner_email varchar(255))")
    # for i, row in df4[30:].iterrows():
    #     sql = "INSERT INTO kexi.credit_cards_data VALUES (%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()
    #
    # print("5local_vendors table")
    # # Email,Business Name,Business Address ID,Customer Service Number
    # cursor.execute("CREATE TABLE local_vendors_data(primary key(email), email varchar(255),Business_Name varchar(250),Business_Address_ID varchar(255),Customer_Service_Number varchar(255))")
    # for i, row in df5[0:10].iterrows():
    #     sql = "INSERT INTO kexi.local_vendors_data VALUES (%s,%s,%s,%s)"
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()
    #
    # print("6orders table")
    # # Transaction_ID,Seller_Email,Listing_ID,Buyer_Email,Date,Quantity,Payment
    # cursor.execute("CREATE TABLE orders_data(primary key(Transaction_ID), Transaction_ID int,Seller_Email varchar(255),Listing_ID varchar(255),Buyer_Email varchar(255),Order_Date varchar(255),Quantity int, Payment int )")
    # for i, row in df6[0:45].iterrows():
    #     sql = "INSERT INTO kexi.orders_data VALUES (%s,%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()
    #
    # print("7product_listing table")
    # # Seller_Email,Listing_ID,Category,Title,Product_Name,Product_Description,Price,Quantity
    # cursor.execute("CREATE TABLE product_listing_data(primary key(Seller_Email, Listing_ID),Seller_Email varchar(255),Listing_ID varchar(255),Category varchar(255),Title varchar(255),Product_Name varchar(255),Product_Description varchar(255), Price varchar(255), Quantity varchar(255))")
    for i, row in df7[70:].iterrows():
        sql = "INSERT INTO kexi.product_listing_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        connection.commit()
    #
    # print("8rating table")
    # # Buyer_Email,Seller_Email,Date,Rating,Rating_Desc
    # cursor.execute("CREATE TABLE rating_data(primary key(Buyer_Email,Seller_Email,Order_Date),Buyer_Email varchar(255),Seller_Email varchar(255),Order_Date varchar(25),Rating int, Rating_Desc varchar(25))")
    # for i, row in df8[0:35].iterrows():
    #     sql = "INSERT INTO kexi.rating_data VALUES (%s,%s,%s,%s,%s)"
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()
    #
    # print("9reviews table")
    # # Buyer_Email,Seller_Email,Listing_ID,Review_Desc
    # cursor.execute(
    #     "CREATE TABLE reviews_data(primary key(Buyer_Email,Seller_Email,Listing_ID),Buyer_Email varchar(255),Seller_Email varchar(255),Listing_ID varchar(255),Review_Desc varchar(253))")
    # for i, row in df9[0:30].iterrows():
    #     sql = "INSERT INTO kexi.reviews_data VALUES (%s,%s,%s,%s)"
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()
    #
    # print("10sellers table")
    # # email,routing_number,account_number,balance
    # cursor.execute(
    #     "CREATE TABLE sellers_data(primary key (Email),Email varchar(255),routing_number varchar(255),account_number varchar(255),balance varchar(255))")
    # for i, row in df10[0:10].iterrows():
    #     sql = "INSERT INTO kexi.sellers_data VALUES (%s,%s,%s,%s)"
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()
    #
    # print("11users table")
    # # email,password
    # cursor.execute(
    #     "CREATE TABLE users_data(email varchar(255),password varchar(255),primary key(email))")
    # for i, row in df11[0:60].iterrows():
    #     sql = "INSERT INTO kexi.users_data VALUES (%s,%s)"
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()
    #
    # print("12zipcode_info table")
    # # zipcode,city,state_id,population,density,county_name,timezone
    # cursor.execute(
    #     "CREATE TABLE zipcode_info_data(primary key(zipcode), zipcode int,city varchar(255),state_id varchar(255),population int,density varchar(255),county_name varchar(255),timezone varchar(255) )")
    # for i, row in df12[58:].iterrows():
    #     sql = "INSERT INTO kexi.zipcode_info_data VALUES (%s,%s,%s,%s,%s,%s,%s)"
    #     print(sql)
    #     cursor.execute(sql, tuple(row))
    #     connection.commit()


# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
#
#
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=RON\SQLEXPRESS;'
#                       'Database=test_database;'
#                       'Trusted_Connection=yes;')
# print("ok2")
# cursor = conn.cursor()
#
#  cursor.execute('''
#  		CREATE TABLE address (
#  			address_ID int primary key,
#  			zipcode int ,
#  			street_num int
#  			street_name nvarchar(30)
#  			)
#                 ''')

#
# for row in df1.itertuples():
#     cursor.execute('''
#                 INSERT INTO address (address_ID, zipcode, street_num, street_name)
#                 VALUES (?,?,?,?)
#                 ''',
#                 row.address_ID,
#                 row.zipcode,
#                 row.street_num,
#                 row.street_name
#                 )
# conn.commit()

