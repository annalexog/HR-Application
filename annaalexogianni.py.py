# Import MySql Connector
import mysql.connector

# making MySQL connection object
mycon = mysql.connector.connect(
    host='localhost', user='root',
    password='', database='hr-g6')
# making MySQL cursor object
mycur = mycon.cursor()


# για να υπάρχουν κενά
def space():
    for i in range(1):
        print()


def check():
    # query για να επιλέξουμε όλους τους employees
    qry = 'select ID_EMPLOYEE from employee;'  # το spelling πρέπει να είναι ίδιο με αυτό στην sql
    mycur.execute(qry)

    d = mycur.fetchall()

    # δημιουργούμε μια λίστα με employees στο table
    employees = []
    for ids in d:
        # μια λίστα με όλους τους employees στο table
        employees.append(ids[0])
    return employees


# function to add a new employee to the table
def add_emp():
    ask = 'Y'
    employees = check() #ελέγχει αν υπάρχει το ID
    while ask in 'yY':
        ID_EMPLOYEE = int(input('Enter employee ID')) #δηλώνεις το id του employee που θέλεις να επεξεργαστείς

        if ID_EMPLOYEE in employees:
            print('ID already exists \nCreate a new ID') # Αν υπάρχει ήδη του ζητάμε να φτιάξει καινούργιο
        else:
            # Tuple με όλες τις πληροφορίες του employee
            data_emp = ()
            NAME = input('First and Last Name : ')
            EMAIL = input('E-mail : ')
            TEL = input('Phone Number : ')
            ADDRESS = input('Address : ')
            SALARY = input('Salary: ')
            data_emp = (ID_EMPLOYEE, NAME, EMAIL, TEL, ADDRESS, SALARY)

            qry = 'insert into employee values(%s,%s,%s,%s,%s,%s);'

            # τα values θα "μπουν" με αυτο το qry
            val = data_emp

            mycur.execute(qry, val)
            mycon.commit()
            print("Employee's data has been added")
            ask = input('Do you wish to add employees? (Y/N) ') # Κάνουμε την ερώτηση αν θέλει να κανει perform το συγκεκριμενο action
            if ask not in ('Yy'):
                space()
                break


# function για να μπορουμε να δουμε τις πληροφοριες καθε employee
def view_emp_data():
    emp = int(input('Enter employee ID: ')) #δηλώνεις το id του employee που θέλεις να επεξεργαστείς
    ID = (emp,) #μετατρέπεις το ID(μεταβλητή) σε tuple
    employees = check() #ελέγχει αν υπάρχει το ID
    if emp in employees:
        validation = input("Are you sure you wish to proceed?: Y/N") # επιβεβαιώνουμε αν όντως θελει να κανει την συγκεκριμένη κίνηση ή αν έκανε καποιο λάθος
        if validation in ("Yy"):
            qry = 'select * from employee where ID_EMPLOYEE = %s;' # qry για να επιλεξουμε τους employees απο την sql
            mycur.execute(qry)
            d = mycur.fetchall() # τους "φέρνει" όλους
            print("Employee's data are: ", d)
        else:
            print("Action canceled") # αν έχει επιλέξει λάθος η διαδικασία ακυρώνεται
    else:
        print("Employee ID does not exist!")

# function για να μπορείς να επεξεργαστείς τα στοιχεία των employees
def edit_emp():
    emp = int(input('Enter employee ID: ')) #δηλώνεις το id του employee που θέλεις να επεξεργαστείς
    ID = (emp,) #μετατρέπεις το ID(μεταβλητή) σε tuple
    employees = check() #ελέγχει αν υπάρχει το ID
    if emp in employees:
        qry = 'select * from employee where ID_EMPLOYEE =%s;' # qry για να επιλέξουμε τους employees απο την sql
        mycur.execute(qry, ID)
        d = mycur.fetchall() # τους "φέρνει" όλους
        print("Employee's data are: ", d)
        validation = input("Are you sure you wish to proceed?: Y/N") # επιβεβαιώνουμε αν όντως θέλει να κάνει την συγκεκριμένη κίνηση ή αν έκανε καποιο λάθος
        if validation in ("Yy"):
            qry = 'update employee set NAME=%s, EMAIL=%s, TEL=%s, ADDRESS=%s, SALARY=%s where ID_EMPLOYEE=%s;' #δίνει την δυνατότητα να επεξεργαστείς τα στοιχεία του employee που διάλεξες
            data_emp = ()
            NAME = input('First and Last Name : ') #το κάθε στοιχείο ξεχωριστά
            EMAIL = input('E-mail : ')
            TEL = input('Phone Number : ')
            ADDRESS = input('Address : ')
            SALARY = input('Salary: ')
            data_emp = (NAME, EMAIL, TEL, ADDRESS, SALARY, emp)
            mycur.execute(qry, data_emp)
            mycon.commit()
        else:
            print("Action canceled")
    else:
        print("Employee ID does not exist!")

# function για να μπορείς να προάγεις έναν employee
def promo_emp():
    emp = int(input('Enter employee ID: ')) #δηλώνεις το id του employee που θέλεις να επεξεργαστείς
    ID = (emp,) #μετατρέπεις το ID(μεταβλητή) σε tuple
    employees = check() #ελέγχει αν υπάρχει το ID
    if emp in employees: #εάν το ID ίναι στη λίστα
        qry = 'select * from employee where ID_EMPLOYEE =%s;' # qry για να επιλέξουμε τους employees απο την sql
        mycur.execute(qry, ID) # εκτελεί την εντολή
        d = mycur.fetchall()  # τους "φέρνει" όλους απο τη βάση
        print("Employee's data are: ", d)
        validation = input("Are you sure you wish to proceed?: Y/N") # επιβεβαιώνουμε αν όντως θέλει να κάνει την συγκεκριμένη κίνηση ή αν έκανε καποιο λάθος
        if validation in ("Yy"):
            qry = 'update employee set SALARY=%s where ID_EMPLOYEE=%s;'
            data_emp = ()
            SALARY = input('Updated SALARY: ')
            data_emp = (SALARY, emp)
            mycur.execute(qry, data_emp)
            mycon.commit()
        else:
            print("Action canceled")
    else:
        print("Employee ID does not exist!")


def del_emp():
    emp = int(input('Enter employee ID: ')) #δηλώνεις το id του employee που θέλεις να επεξεργαστείς
    ID = (emp,) #μετατρέπεις το ID(μεταβλητή) σε tuple
    employees = check() #ελέγχει αν υπάρχει το ID
    if emp in employees: #εάν το ID ίναι στη λίστα
        qry = 'select * from employee where ID_EMPLOYEE =%s;' # qry για να επιλέξουμε τους employees απο την sql
        mycur.execute(qry, ID) # εκτελεί την εντολή
        d = mycur.fetchall() # τους "φέρνει" όλους απο τη βάση
        print("Employee's data are: ", d)
        validation = input("Are you sure you wish to delete this employee?: Y/N") #επιβεβαιώνουμε αν θέλει να διαγραφεί ο employee
        if validation in ("Yy"):
            qry = 'delete from employee where ID_EMPLOYEES=%s;' #διαγράφει employee τον από τη βάση
            mycur.execute(qry, ID)
            mycon.commit()
            print("Employee is deleted")
        else:
            print("Action canceled")
    else:
        print("Employee ID does not exist!")


def search_emp():
    emp = int(input('Enter employee ID: '))
    ID = (emp,)
    employees = check()
    if emp in employees:
        qry = 'select * from employee where ID_EMPLOYEE =%s;'
        mycur.execute(qry, ID)
        d = mycur.fetchall()
        print("Employee's data are: ", d)
        validation = input("Are you sure you wish to proceed?: Y/N")
        if validation in ("Yy"):
            choice = int(
                input("Choose an action: \n1)view employee\n2)edit employee\n3)delete employee\n4)promote employee")) #δηλώνουμε τι δράση θα ήθελε ο χρήστης να κάνει
            if choice == 1: #επιλέγει με αριθμό
                view_emp_data()
            elif choice == 2:
                edit_emp()
            elif choice == 3:
                del_emp()
            elif choice == 4:
                promo_emp()
        else:
            print("Action canceled")
    else:
        print("Employee ID does not exist!")

# main function για το τι θέλει ο χρήστης να κάνει στο table
home = int(input(
    "Choose an action: \n1)Add Employee \n2)View Eployee \n3)Edit Employee \n4)Delete Employee \n5)Promote Employee\n6)Search Employee\n\n"))
while home < 1 or home > 7: # εάν επιλέξει κάτι εκτός των αριθμών που του δίνονται ως επιλογή θα πρέπει να ξαναεπιλέξει σωστά
    home = int(input("Make a valid choice from 1-7\n\n"))
if home == 1:
    add_emp()
elif home == 2:
    view_emp_data()
elif home == 3:
    edit_emp()
elif home == 4:
    del_emp()
elif home == 5:
    promo_emp()
elif home == 6:
    search_emp()
else:
    print("Action canceled")
