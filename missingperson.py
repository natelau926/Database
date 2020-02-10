from tkinter import *
import mysql.connector

root = Tk()
root.geometry("1000x1000")
root.title("CSS 475 Missing_Person Database")


def Missingperson_Table():
    mydb = mysql.connector.connect(
        host="database-2.c3skravfuzit.us-west-2.rds.amazonaws.com", user="admin", password="css475missingpersondb",
        database="missingpersonsdb")
    mycursor.execute("Select * from MISSING_PERSON")
    myresult = mycursor.fetchall()
    table_name = "                                       ----------------Missing Person----------------"
    frame.insert(frame.size(), table_name)
    space_print1 = "------------------------------------------" \
                   "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print1)
    complaint_att = "| Person_ID  |First_Name| Last_Name|   DOB   | Sex | Race | Last_Seen | Height | Weight"
    frame.insert(frame.size() + 1, complaint_att)
    space_print = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    for row in myresult:
        result1 = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
        frame.insert(frame.size(), result1)
        result = "| " + str(row[0]) + ' | ' + row[1] + ' | ' + row[2] + ' | ' + str(row[3]) + ' | ' + row[4] + ' | ' + \
                 row[5] + ' | ' \
                 + str(row[6]) + ' | ' + row[7] + ' | ' + row[8] + ' | '
        frame.insert(frame.size() + 1, result)
        space_print = "------------------------------------------" \
                      "----------------------------------------------------------------------------------------"
        frame.insert(frame.size(), space_print)
    space_print = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    mydb.close()


def Complaint_Report_Table():
    mydb = mysql.connector.connect(
        host="database-2.c3skravfuzit.us-west-2.rds.amazonaws.com", user="admin", password="css475missingpersondb",
        database="missingpersonsdb")
    mycursor.execute("Select * from COMPLAINT_REPORT")
    myresult = mycursor.fetchall()
    table_name = "                        ----------------Complaint Report----------------"
    frame.insert(frame.size(), table_name)
    space_print1 = "------------------------------------------" \
                   "------------------------------------------------------------"
    frame.insert(frame.size(), space_print1)
    complaint_att = "| Complaint_ID | loc_ID | Sus_ID | Missing_ID | File_Fname | Filer_Lname |"
    frame.insert(frame.size() + 1, complaint_att)
    space_print = "------------------------------------------" \
                  "------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    for row in myresult:
        result1 = "------------------------------------------" \
                  "------------------------------------------------------------"
        frame.insert(frame.size(), result1)
        result = ("|   " + str(row[0]) + ' | ' + str(row[1]) + ' | ' + str(row[2]) + ' | ' + str(row[3]) + ' | ' + row[
            4] + ' | ' + row[5] + ' |')
        frame.insert(frame.size() + 1, result)
        space_print3 = "------------------------------------------" \
                       "------------------------------------------------------------"
        frame.insert(frame.size(), space_print3)

    mydb.close()


def Family_Table():
    mydb = mysql.connector.connect(
        host="database-2.c3skravfuzit.us-west-2.rds.amazonaws.com", user="admin", password="css475missingpersondb",
        database="missingpersonsdb")
    mycursor.execute("Select * from FAMILY")
    myresult = mycursor.fetchall()
    table_name = "                                           ----------------Family----------------"
    frame.insert(frame.size(), table_name)
    space_print1 = "------------------------------------------" \
                   "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print1)
    complaint_att = "| Family_ID |  Missing_ID |  First_Name  | Last_Name  | Relationship  | Phone_Number |"
    frame.insert(frame.size() + 1, complaint_att)
    space_print = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    for row in myresult:
        result1 = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
        frame.insert(frame.size(), result1)
        result = ("| " + str(row[0]) + ' | ' + str(row[1]) + ' | ' + row[2] + ' | ' + row[3] + ' | ' + row[4] + ' | ' +
                  row[5] + ' | ')
        frame.insert(frame.size() + 1, result)
        space_print = "------------------------------------------" \
                      "----------------------------------------------------------------------------------------"
        frame.insert(frame.size(), space_print)
    space_print = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    mydb.close()


def Location_Table():
    mydb = mysql.connector.connect(
        host="database-2.c3skravfuzit.us-west-2.rds.amazonaws.com", user="admin", password="css475missingpersondb",
        database="missingpersonsdb")
    mycursor.execute("Select * from LOCATION")
    myresult = mycursor.fetchall()
    table_name = "                                           ----------------Location----------------"
    frame.insert(frame.size(), table_name)
    space_print1 = "------------------------------------------" \
                   "---------------"
    frame.insert(frame.size(), space_print1)
    attribute_name = " |   Location ID   |    CITY   |   State   | "
    frame.insert(frame.size() + 1, attribute_name)
    space_print = "------------------------------------------" \
                  "---------------"
    frame.insert(frame.size(), space_print)
    for row in myresult:
        result1 = "------------------------------------------" \
                  "---------------"
        frame.insert(frame.size(), result1)
        result = "|  " + (str(row[0]) + "  | " + row[1] + '  | ' + row[2]) + '  | '
        frame.insert(frame.size() + 1, result)
        space_print3 = "------------------------------------------" \
                       "---------------"
        frame.insert(frame.size(), space_print3)
    mydb.close()


def Medical_Records_Table():
    mydb = mysql.connector.connect(
        host="database-2.c3skravfuzit.us-west-2.rds.amazonaws.com", user="admin", password="css475missingpersondb",
        database="missingpersonsdb")
    mycursor.execute("Select * from MEDICAL_RECORDS")
    myresult = mycursor.fetchall()
    table_name = "                                           ----------------Medical Records----------------"
    frame.insert(frame.size(), table_name)
    space_print1 = "------------------------------------------" \
                   "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print1)
    complaint_att = " |  Record_ID  |  Missing_ID  |  Know_Illnesses |  Medication |"
    frame.insert(frame.size() + 1, complaint_att)
    space_print = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    for row in myresult:
        result1 = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
        frame.insert(frame.size(), result1)
        result = ("| " + str(row[0]) + ' |' + str(row[1]) + ' |' + row[2] + ' | ' + row[3] + ' | ')
        frame.insert(frame.size() + 1, result)
    space_print = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    mydb.close()


def Police_Department_Table():
    mydb = mysql.connector.connect(
        host="database-2.c3skravfuzit.us-west-2.rds.amazonaws.com", user="admin", password="css475missingpersondb",
        database="missingpersonsdb")
    mycursor.execute("Select * from POLICE_DEPARTMENT")
    myresult = mycursor.fetchall()
    table_name = "                                           ----------------Police Department----------------"
    frame.insert(frame.size(), table_name)
    space_print1 = "------------------------------------------" \
                   "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print1)
    attribute_name = "| Department ID |      Com ID       |        City        |   State   |"
    frame.insert(frame.size() + 1, attribute_name)
    space_print = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    for row in myresult:
        result1 = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
        frame.insert(frame.size(), result1)
        result = "|" + (str(row[0]) + " " * (16 - len(str(row[0]))) + '|' + str(row[1]) + ' ' * (
                    15 - len(str(row[1]))) + '|' + row[2] + ' ' * (15 - len(str(row[2]))) + '|' + row[3] + ' ' * (
                                    15 - len(str(row[3]))) + '|')
        frame.insert(frame.size() + 1, result)
        space_print3 = "------------------------------------------" \
                       "----------------------------------------------------------------------------------------"
        frame.insert(frame.size(), space_print3)
    mydb.close()


def Suspicious_Persons_Table():
    mydb = mysql.connector.connect(
        host="database-2.c3skravfuzit.us-west-2.rds.amazonaws.com", user="admin", password="css475missingpersondb",
        database="missingpersonsdb")
    mycursor.execute("Select * from SUSPICIOUS_PERSONS")
    myresult = mycursor.fetchall()
    table_name = "                                           ----------------Suspicious Persons----------------"
    frame.insert(frame.size(), table_name)
    space_print1 = "------------------------------------------" \
                   "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print1)
    complaint_att = " | Suspect_ID |  First_Name  | Last_Name |  DOB  |  Sex  | Race | "
    frame.insert(frame.size() + 1, complaint_att)
    space_print = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    for row in myresult:
        result1 = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
        frame.insert(frame.size(), result1)
        result = ('| ' + str(row[0]) + ' | ' + row[1] + ' | ' + row[2] + ' | ' + str(row[3]) + ' | ' + row[4] + ' | ' + row[5] + ' | ')
        frame.insert(frame.size() + 1, result)
    space_print = "------------------------------------------" \
                  "----------------------------------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    mydb.close()


def q1():
    mydb = mysql.connector.connect(
        host="database-2.c3skravfuzit.us-west-2.rds.amazonaws.com", user="admin", password="css475missingpersondb",
        database="missingpersonsdb")
    mycursor.execute("SELECT MISSING_PERSON.First_Name AS MISSING_PERSON_FNAME, "
                     "MISSING_PERSON.Last_Name AS MISSING_PERSON_LNAME, "
                     "FAMILY.First_Name AS FAMILY_FNAME, FAMILY.Last_Name AS FAMILY_LNAME, "
                     "FAMILY.Relationship, FAMILY.Phone_Number "
                     "FROM MISSING_PERSON INNER JOIN FAMILY ON MISSING_PERSON.Person_ID = FAMILY.Missing_ID "
                     "ORDER BY MISSING_PERSON_FNAME;")

    myresult = mycursor.fetchall()
    table_name = "                        ----------------Missing Person's family name, Relationship and Phone Number----------------"
    frame.insert(frame.size(), table_name)
    space_print1 = "------------------------------------------" \
                   "------------------------------------------------------------"
    frame.insert(frame.size(), space_print1)
    complaint_att = "| MISSING_PERSON_FNAME | MISSING_PERSON_LNAME | FAMILY_FNAME | FAMILY_LNAME | Relationship | Phone_Number |"
    frame.insert(frame.size() + 1, complaint_att)
    space_print = "------------------------------------------" \
                  "------------------------------------------------------------"
    frame.insert(frame.size(), space_print)
    for row in myresult:
        result1 = "------------------------------------------" \
                  "------------------------------------------------------------"
        frame.insert(frame.size(), result1)
        result = ("|   " + row[0] + ' | ' + row[1]+ ' | ' + row[2]+ ' | ' + row[3] + ' | ' + row[
            4] + ' | ' + str(row[5]) + ' |')
        #myresult = row
        frame.insert(frame.size() + 1, result)
        space_print3 = "------------------------------------------" \
                       "------------------------------------------------------------"
        frame.insert(frame.size(), space_print3)

    mydb.close()


button = Button(root, text="Missing Person", font=40, bg="White", command=Missingperson_Table)
button.place(x=20, y=30)

button1 = Button(root, text="Complaint Report", font=40, bg="White", command=Complaint_Report_Table)
button1.place(x=160, y=30)

button2 = Button(root, text="Family", font=40, bg="White", command=Family_Table)
button2.place(x=315, y=30)

button3 = Button(root, text="Location", font=40, bg="White", command=Location_Table)
button3.place(x=395, y=30)

button4 = Button(root, text="Medical_Records", font=40, bg="White", command=Medical_Records_Table)
button4.place(x=485, y=30)

button5 = Button(root, text="Police_Department", font=40, bg="White", command=Police_Department_Table)
button5.place(x=635, y=30)

button6 = Button(root, text="Suspicious_Persons", font=40, bg="White", command=Suspicious_Persons_Table)
button6.place(x=801, y=30)

q1 = Button(root, text="Missing Person's name, family's name, Relationship and Phonenumber", font=40, bg="White", command=q1)
q1.place(x=20, y=90)

frame = Listbox(root, font=20)
frame.place(relx=0.5, rely=0.30, relwidth=0.9, relheight=0.8, anchor='n')
mydb = mysql.connector.connect(host="database-2.c3skravfuzit.us-west-2.rds.amazonaws.com", user="admin",
                               password="css475missingpersondb", database="missingpersonsdb")

mycursor = mydb.cursor()

root.mainloop()

# mycursor.execute('CREATE TABLE MISSING_PERSON (Person_ID INTEGER(30), First_Name VARCHAR(15), Last_Name VARCHAR(15), DOB DATE, Sex VARCHAR(7), Race VARCHAR(20),
# Last_Seen VARCHAR(20), Height VARCHAR(10), Weight VARCHAR(10))')


# sqlFormula = "INSERT INTO MISSING_PERSON (Person_ID, First_Name, Last_Name, " \
#             "DOB, Sex, Race, Last_Seen, Height, Weight) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
# person =  [(334745446, 'Rozelle', 'Dominguez', '2004-11-24', 'Female', 'Hispanic', '2018-02-26', 64, 115),
#          (864541919, 'Petr', 'Landon', '2012-01-30', 'Male', 'White', '2019-06-04', 50, 100),
#          (285373785, 'Goldia', 'Dibnah', '2000-06-30', 'Female', 'African American', '2019-05-05', 64, 98)]

# mycursor.executemany(sqlFormula, person)
# mydb.commit()


# ----- Get the data from table using query ---------
# mycursor.execute("SELECT * FROM students")
# myresult = mycursor.fetchall()
# for row in myresult:
#    print(row)


# -------- Show the databases ---------
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)


# ------ Create table -------------
# mycursor.execute("CREATE TABLE (table_name) (attribute) (data_type) , (attribute) (date_type)
# Example for student table
# mycursor.execute("CREATE TABLE students name VARCHAR(255), AGE INTEGER(10))")


# ------ INSERT INTO VALUES -------
# Example for student table by adding student name and age

# sqlFormula = "INSERT INTO students (name,age) VALUES (%s, %s)"
# students = [("Bob", 12),
#            ("Amanda", 32),
#            ("Jacob", 21),
#            ("Michelle", 28)]
# mycursor.executemany(sqlFormula, students)
# mydb.commit()
