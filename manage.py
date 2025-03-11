from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def _init_(self,root):
        self.root=root
        self.root.title("Hospital management system")
        self.root.geometry("1366x768+0+0")
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEfect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="blue",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #===========================Dataframe===============================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=350)


        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=940,height=300)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("arial", 12, "bold"),
                                   text="prescription")
        DataframeRight.place(x=950, y=5, width=380,height=300)
        #========================buttons frame====================
        bDataframe = Frame(self.root, bd=20, relief=RIDGE)
        bDataframe.place(x=0, y=480, width=1360, height=60)

        # ========================details frame====================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=540, width=1360, height=150)

       #=================Dataframeleft==========================

        lblNameTablet=Label(DataframeLeft,font=("arial",12,"bold"),text="no of tablet:",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)
        txtNameTablet=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Nameoftablets,width=35)
        txtNameTablet.grid(row=0,column=1)

        lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="ref no:", padx=2,pady=6)
        lblref.grid(row=1, column=0, sticky=W)
        txtref= Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="dose:", padx=2,pady=6)
        lblDose.grid(row=2, column=0, sticky=W)
        lblDose= Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.Dose,width=35)
        lblDose.grid(row=2, column=1)

        lblNooftablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="name of tablets:", padx=2,pady=6)
        lblNooftablets.grid(row=3, column=0, sticky=W)
        lblNooftablets = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.NumberofTablets,width=35)
        lblNooftablets.grid(row=3, column=1)

        lblissueDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="issue date:", padx=2,pady=6)
        lblissueDate.grid(row=4, column=0, sticky=W)
        lblissueDate= Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.Issuedate,width=35)
        lblissueDate.grid(row=4, column=1)

        lblExpDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="exp date", padx=2,pady=6)
        lblExpDate.grid(row=5, column=0, sticky=W)
        lblExpDate = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.ExpDate,width=35)
        lblExpDate.grid(row=5, column=1)

        lblDailyDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="daily dose", padx=2,pady=6)
        lblDailyDose.grid(row=6, column=0, sticky=W)
        lblDailyDose = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.DailyDose,width=35)
        lblDailyDose.grid(row=6, column=1)

        lblsideEffect = Label(DataframeLeft, font=("arial", 12, "bold"), text="side effect", padx=2,pady=6)
        lblsideEffect.grid(row=7, column=0, sticky=W)
        lblsideEffect = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.sideEfect,width=35)
        lblsideEffect.grid(row=7, column=1)

        lblFurtherinfo = Label(DataframeLeft, font=("arial", 12, "bold"), text="further info", padx=2, pady=6)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        lblFurtherinfo = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.FurtherInformation,width=35)
        lblFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, font=("arial", 12, "bold"), text="blood pressure", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        lblBloodPressure = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.DrivingUsingMachine,width=35)
        lblBloodPressure.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=("arial", 12, "bold"), text="storage device", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        lblStorage = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.StorageAdvice,width=35)
        lblStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, font=("arial", 12, "bold"), text="medication", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        lblMedicine = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.HowToUseMedication,width=35)
        lblMedicine.grid(row=3, column=3)

        lblPatientID = Label(DataframeLeft, font=("arial", 12, "bold"), text="patient id", padx=2, pady=6)
        lblPatientID.grid(row=4, column=2, sticky=W)
        lblPatientID = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.PatientId,width=35)
        lblPatientID.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, font=("arial", 12, "bold"), text="nhs number", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        lblNhsNumber = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.nhsNumber,width=35)
        lblNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(DataframeLeft, font=("arial", 12, "bold"), text="patient name", padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        lblPatientname = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.PatientName,width=35)
        lblPatientname.grid(row=6, column=3)

        lblDateOfBirth = Label(DataframeLeft, font=("arial", 12, "bold"), text="date of birth", padx=2, pady=6)
        lblDateOfBirth.grid(row=7 ,column=2, sticky=W)
        lblDateOfBirth = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.DateOfBirth,width=35)
        lblDateOfBirth.grid(row=7, column=3)

        #======================Dataframeright==========================

        self.txtprescription=Text(DataframeRight, font=("arial", 13, "bold"), width=35,height=13,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)

        #=========================buttons================================

        btntxtprescriptionData=Button(bDataframe,command=self.iPrectioption,text="prescription",bg="red",fg="white",font=("arial", 13, "bold"),width=20,padx=2,pady=6)
        btntxtprescriptionData.grid(row=0,column=1)

        btntxtprescriptiond = Button(bDataframe,command=self.iprescriptiond,text="prescription data", bg="red", fg="white",
                                        font=("arial", 13, "bold"), width=20, padx=2, pady=6)
        btntxtprescriptiond.grid(row=0, column=2)

        btntxtup = Button(bDataframe,command=self.txtup,text="update", bg="red", fg="white",
                                        font=("arial", 13, "bold"), width=20, padx=2, pady=6)
        btntxtup.grid(row=0, column=3)

        btntxtdel = Button(bDataframe,command=self.idelete,text="delete", bg="red", fg="white",
                                        font=("arial", 13, "bold"), width=20, padx=2, pady=6)
        btntxtdel.grid(row=0, column=4)

        btntxtclear = Button(bDataframe,command=self.clear, text="clear", bg="red", fg="white",
                                        font=("arial", 13, "bold"), width=20, padx=2, pady=6)
        btntxtclear.grid(row=0, column=5)

        btntxtexit = Button(bDataframe,command=self.iExit, text="exit", bg="red", fg="white",
                             font=("arial", 13, "bold"), width=20, padx=2, pady=6)
        btntxtexit.grid(row=0, column=6)

        #===========================TABLE======================================
        Framedetails=Frame(Dataframe,bd=6,relief=RIDGE,padx=20,bg="powder blue")
        Framedetails.place(x=0,y=2,width=1370,height=190)
        self.hospital_table=ttk.Treeview(Framedetails,column=("nooftable","ref","dose","nametablets","issue date","exp date","daily dose","storage","nhs number","pname","dob"))


        self.hospital_table.heading("nooftable",text="no of tablelts")
        self.hospital_table.heading("ref", text="ref no")
        self.hospital_table.heading("dose", text="dose")
        self.hospital_table.heading("nametablets", text="name of tablets")
        self.hospital_table.heading("issue date", text="issue date")
        self.hospital_table.heading("exp date", text="exp date")
        self.hospital_table.heading("daily dose", text="daily dose")
        self.hospital_table.heading("storage", text="storage")
        self.hospital_table.heading("nhs number", text="nhs number")
        self.hospital_table.heading("pname", text="patient name")
        self.hospital_table.heading("dob", text="DOB")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nooftable",width=25)
        self.hospital_table.column("ref",width=25)
        self.hospital_table.column("dose",width=25)
        self.hospital_table.column("nametablets", width=25)
        self.hospital_table.column("issue date",width=25)
        self.hospital_table.column("exp date", width=25)
        self.hospital_table.column("daily dose", width=25)
        self.hospital_table.column("storage", width=25)
        self.hospital_table.column("nhs number",width=25)
        self.hospital_table.column("pname", width=25)
        self.hospital_table.column("dob",width=25)


        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()

    #===================functionality===============================================
    def iprescriptiond(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
         conn=mysql.connector.connect(host="localhost",username="root",password="Dinesh@123",database="ram")
         my_cursor=conn.cursor()
         my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Nameoftablets.get(),
                                                                                                         self.ref.get(),
                                                                                                         self.Dose.get(),
                                                                                                         self.NumberofTablets.get(),
                                                                                                         self.Issuedate.get(),
                                                                                                         self.ExpDate.get(),
                                                                                                         self.DailyDose.get(),
                                                                                                         self.StorageAdvice.get(),
                                                                                                         self.nhsNumber.get(),
                                                                                                         self.PatientName.get(),
                                                                                                         self.DateOfBirth.get()                                                                              ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("success","record has been inserted")

    def txtup(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Dinesh@123", database="ram")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE hospital SET nooftablets=%s,dose=%s,nameofmeds=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s WHERE Reference_No=%s",(
            self.Nameoftablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.ref.get()))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("success", "it has been updated")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Dinesh@123", database="ram")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        if row:
         self.Nameoftablets.set(row[0])
         self.ref.set(row[1])
         self.Dose.set(row[2])
         self.NumberofTablets.set(row[3])
         self.Issuedate.set(row[4])
         self.ExpDate.set(row[5])
         self.DailyDose.set(row[6])
         self.StorageAdvice.set(row[7])
         self.nhsNumber.set(row[8])
         self.PatientId.set(row[9])
         self.DateOfBirth.set(row[10])
    def idelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Dinesh@123", database="ram")
        my_cursor = conn.cursor()
        query="DELETE FROM hospital WHERE  Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("delete","patient has been deleted successfully")
    def iPrectioption(self):
        self.txtprescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtprescription.insert(END,"Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtprescription.insert(END, "DOSE:\t\t\t" + self.Dose.get() + "\n")
        self.txtprescription.insert(END, "Issue date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtprescription.insert(END, "EXP date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtprescription.insert(END, "daily dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtprescription.insert(END, "side effect:\t\t\t" + self.sideEfect.get() + "\n")
        self.txtprescription.insert(END, "further info:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtprescription.insert(END, "nhs num:\t\t\t" + self.nhsNumber.get() + "\n")
        self.txtprescription.insert(END, "patient name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtprescription.insert(END, "dob:\t\t\t" + self.DateOfBirth.get() + "\n")
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FurtherInformation.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.StorageAdvice.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.txtprescription.delete("1.0",END)
    def iExit(self):
        Iexit=messagebox.askyesno("HOSPITAL MANAGEMENT SYSTEM","CONFIRM DO U WANT TO EXIT")
        if Iexit>0:
            root.destroy()
            return





















root=Tk()
ob=Hospital(root)
root.mainloop()
