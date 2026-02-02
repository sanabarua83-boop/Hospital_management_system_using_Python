import pickle


#Accepting data for Dictionary
def insertpatientRec():
    pid = int(input('Enter patient ID:'))
    name = input('Enter patient name:')
    age = int(input('Enter patient age'))
    disease = input('Enter disease:')
                  

    #Creating the dictionary
    rec = {'ID':pid,'Name':name,'Age':age,'Disease':disease}

    #writing the dictionary
    f= open('patient.dat','ab')
    pickle.dump(rec,f)
    f.close()

#Reading the records
def readrec():
    f = open("patient.dat","rb")
    while True:
        try:
            rec= pickle.load(f)
            print('patient ID:',rec['ID'])
            print('patient name:',rec['Name'])
            print('patient age:',rec['Age'])
            print('patient disease:',rec['Disease'])
        except EOFError:
            break
    f.close()

#searching a record based on patient ID
def searchpatientID(r):
    f = open('pateint.dat','rb')
    flag = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['patient ID'] == r:
                print('patient ID:',rec['patient ID'])
                print('patient Name:',rec['patient Name'])
                print('patient Age:',rec['patient age'])
                print('patient disease:',['patient disease'])
                flag = True
        except EOFError:
                break
    if flag == False:
        print('No Record found')
    f.close()
            

#Deleting a record based on ID
def deletepatientRec(r):
    f = open('patient.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
        f.close()
        f = open('patient.dat','wb')
        for x in reclst:
            if x['patient ID']==r:
                continue
            pickle.dump(x,f)
        f.close()
        
#Accepting data for Dictionary
def insertdoctorRec():
    did = int(input('Enter Doctor ID:'))
    name = input('Enter Doctot name:')
    spec = input('Enter Specialization:')
    fees = int(input('Enter Fess:'))

    #creating the Dictionary
    doctorrec = {'ID':pid,'Name':name,'Specialization':spec,'Fees':fees}

    #writing the Dictionary
    f= open('doctor.dat','ab')
    pickle.dump(doctorrec,f)
    f.close()

#Reading the records
def readdoctorRec():
    f = open('Doctor.dat','rb')
    while True:
        try:
            rec = pickle.load(f)
            print('ID:',rec['ID'])
            print('Name:',rec['Name'])
            print('Specialization:',rec['Specialization'])
        except EOFError:
            break
    f.close() 


#searching a record based on Doctor ID
def searchdoctorID(r):
    f = open('Doctor.dat','rb')
    flag = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['ID'] == r:
                print('ID:', rec['ID'])
                print('Name:', rec['Name'])
                print('Specialization:', rec['Specialization'])
                print('Fees:', rec['Fees'])
                flag  = True
        except EOFError:
            break
    if flag == False:
         print('No Records found')
    f.close()


#Deleting a record based on ID
def deleteDoctorRec(r):
    reclst = []

    # Step 1: Read all records
    with open('doctor.dat', 'rb') as f:
        while True:
            try:
                rec = pickle.load(f)
                reclst.append(rec)
            except EOFError:
                break

    # Step 2: Write back all records except the one to delete
    with open('doctor.dat', 'wb') as f:
        for x in reclst:
            if x['ID'] != r:
                pickle.dump(x, f)


def bookAppointment():
    
    appid = int(input("Enter Appointment ID: "))
    pid = int(input("Enter Patient ID:" ))
    did = int(input("Enter Doctor ID:" ))
    date = input("Enter Date (dd-mm-yyyy) ")
    spec = input("Enter Specialization: ")
    fees = input("Enter Fees: ")

    #creating the Dictionary
    app = {'AppID':appid,'PatientID':pid,'DoctorID':did,
           'Date':date,'Specialization':spec,'Fees':fees}

    #writing the Dictionary
    f = open('appointment.dat','ab')
    pickle.dump(app,f)
    f.close()

    #Reading the records
def readapprec():
    f = open("Appointment.dat","rb")
    while True:
        try:
            rec= pickle.load(f)
            print('PatientID:',rec['PatientID'])
            print('DoctorID:',rec['DoctorID'])
            print('Date:',rec['Date'])
            print('Specialization:',rec['Specialization'])
            print('Fees:',rec['Fees'])
        except EOFError:
            break
    f.close()
               
while True:
    print('Type 1 to insert patient rec.')
    print('Type 2 to disply patient rec.')
    print('Type 3 to search patient ID.')
    print('Type 4 to delete a patient record.')
    print('Type 5 to insert Doctor Rec.')
    print('Type 6 to disply Doctor Rec.')
    print('Type 7 to search Doctor ID.')
    print('Type 8 to delete a Doctor Rec.')
    print('Type 9 to book appointment.')
    print('Type 10 to view appointment.')
    
    
    choice = int(input('Enter you choice:'))
    if choice == 1:
        insertpatientRec()
    if choice == 2:
        readpatientrec()
    if choice == 3:
        r = int(input('Enter a patient ID'))
        searchpatientID(r)
    if choice == 4:
        deletepatientRec(r)
    if choice == 5:
        insertdoctorRec()
    if choice == 6:
        readdoctorRec()
    if choice == 7:
        r = int(input('Enter a Doctor ID'))
        searchdoctorID(r)
    if choice == 8:
        r = int(input('Enter a Doctor ID'))
        deleteDoctorRec(r)
    if choice == 9:
        bookAppointment()
    if choice == 10:
        readapprec()
    if choice == 11:
        exit()
        
        
        
           
            
        


    
      
                  
                  
