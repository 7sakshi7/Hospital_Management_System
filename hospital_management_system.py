from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry('1540x800+0+0')

        # variables
        self.name_of_tablets = StringVar()
        self.reference_no = StringVar()
        self.dose = StringVar()
        self.no_of_tablets = StringVar()
        self.lot = StringVar()
        self.issued_date = StringVar()
        self.expiry_date = StringVar()
        self.daily_dose = StringVar()
        self.furthur_information = StringVar()
        self.storage_advice = StringVar()
        self.medicine = StringVar()
        self.blood_pressue_advice = StringVar()
        self.patient_id = StringVar()
        self.patient_name = StringVar()
        self.date_of_birth = StringVar()
        self.patient_address = StringVar()

        label_title = Label(self.root, bd=10, relief=RIDGE, text="Hospital Management System",
                            fg="red", bg="white", font=("times new roman", 50, "bold"))
        label_title.pack(side=TOP, fill=X)

        # -------------------------------DATA FRAME------------------------------
        data_frame = Frame(self.root, bd=10, relief=RIDGE)
        data_frame.place(x=0, y=130, width=1530, height=400)

        # left frame
        data_frame_left = LabelFrame(data_frame, bd=5, relief=RIDGE, padx=10, font=(
            "arial", 12, "bold"), text="Patient Information")
        data_frame_left.place(x=5, y=5, width=980, height=350)

        # right frame
        data_frame_right = LabelFrame(data_frame, bd=5, relief=RIDGE, padx=10, font=(
            "arial", 12, "bold"), text="Prescription")
        data_frame_right.place(x=990, y=5, width=490, height=350)

        # ------------------------------------BUTTONS FRAME-------------------------------
        button_frame = Frame(self.root, bd=10, relief=RIDGE)
        button_frame.place(x=0, y=530, width=1530, height=70)

        # ------------------------------------DETAILS  FRAME-------------------------------
        details_frame = Frame(self.root, bd=10, relief=RIDGE)
        details_frame.place(x=0, y=610, width=1530, height=170)

        # -----------------------------------------DATABASE OPERATION---------------------
        def check_patient_id():
            if os.path.isfile('data.txt'):
                with open('data.txt', 'r') as fp:
                    content = fp.readlines()
                    print(content)
                    for data in content:
                        my_list = data.split(',')[9]
                        print(my_list[my_list.find(':')+2:],self.patient_id.get())
                        if my_list[my_list.find(':')+2:]== "'"+self.patient_id.get()+"'":
                            return True
            return False

        def show_prescription():
            pres_text = '''
            Name of Tablet:{}\n
            Reference Number:{}\n
            Dose:{}\n
            Number of Tablets:{}\n
            Issued Date:{}\n
            Expiry Date:{}\n
            Patient Name:{}\n
            Patient Id:{}\n'''.format(
                self.name_of_tablets.get(),
                self.reference_no.get(),
                self.dose.get(),
                self.no_of_tablets.get(),
                self.issued_date.get(),
                self.expiry_date.get(),
                self.patient_name.get(),
                self.patient_id.get())

            ############### CONTENT INSIDE RIGHT FRAME ######################
            self.prescription_text = Text(data_frame_right, font=(
                "arial", 10), width=45, height=19, padx=2, pady=6)
            self.prescription_text.grid(row=0, column=0)
            self.prescription_text.insert(END, pres_text)
            clear_field()

        def add_prescription_data():
            val = check_patient_id()
            if val == True:
                messagebox.showerror("Error", "Patient Id already Exist")
                return
            print('hello')
            if self.name_of_tablets.get() == "" or self.reference_no.get() == "" or self.patient_id.get() == "":
                messagebox.showerror("Error", "All fields are required")
            else:
                with open('data.txt','a')as fp:
                    fp.write(str({
                        'name_of_tablets': self.name_of_tablets.get(),
                        'reference_no': self.reference_no.get(),
                        'dose': self.dose.get(),
                        'no_of_tablets': self.no_of_tablets.get(),
                        'lot': self.lot.get(),
                        'issued_date': self.issued_date.get(),
                        'expiry_date': self.expiry_date.get(),
                        'medicine': self.medicine.get(),
                        'patient_name': self.patient_name.get(),
                        'patient_id': self.patient_id.get(),
                        'date_of_birth': self.date_of_birth.get(),
                        'patient_address': self.patient_address.get()
                    }))
                    fp.write('\n')
                show_prescription()

        ############### CONTENT INSIDE LEFT FRAME ######################

        #  tablet name
        tablet_name = Label(data_frame_left, text="Names of Tablet", font=(
            "arial", 12), padx=2, pady=6)
        tablet_name.grid(row=0, column=0, sticky=W)

        com_tablet_name = ttk.Combobox(
            data_frame_left, textvariable=self.name_of_tablets, font=("arial", 12), width=33)
        com_tablet_name['values'] = ('Paracetamol', 'Ativan', 'Adderall')
        com_tablet_name.current(0)
        com_tablet_name.grid(row=0, column=1)

        # refereb=nce number
        ref_num = Label(data_frame_left, font=("arial", 12),
                        text="Reference No. ", padx=2)
        ref_num.grid(row=1, column=0, sticky=W)
        text_ref = Entry(
            data_frame_left, textvariable=self.reference_no, font=("arial", 12), width=35)
        text_ref.grid(row=1, column=1)

        # dose
        dose = Label(data_frame_left, font=("arial", 12),
                     text="Dose ", padx=2, pady=4)
        dose.grid(row=2, column=0, sticky=W)
        text_dose = Entry(data_frame_left, textvariable=self.dose,
                          font=("arial", 12), width=35)
        text_dose.grid(row=2, column=1)

        # number of tablets
        no_of_tablets = Label(data_frame_left, font=(
            "arial", 12), text="Numbet Of Tablets ", padx=2, pady=6)
        no_of_tablets.grid(row=3, column=0, sticky=W)
        no_of_tablets_text = Entry(
            data_frame_left, textvariable=self.no_of_tablets, font=("arial", 12), width=35)
        no_of_tablets_text.grid(row=3, column=1)

        # lots
        lots = Label(data_frame_left, font=("arial", 12),
                     text="Lots ", padx=2, pady=6)
        lots.grid(row=4, column=0, sticky=W)
        lots_text = Entry(data_frame_left, textvariable=self.lot,
                          font=("arial", 12), width=35)
        lots_text.grid(row=4, column=1)

        # issue date
        issue_date = Label(data_frame_left, font=(
            "arial", 12), text="Issue Date ", padx=2, pady=6)
        issue_date.grid(row=5, column=0, sticky=W)
        issue_date_text = Entry(
            data_frame_left, textvariable=self.issued_date, font=("arial", 12), width=35)
        issue_date_text.grid(row=5, column=1)

        # expiry date
        expiry_date = Label(data_frame_left, font=(
            "arial", 12), text="Expiry Date", padx=2, pady=6)
        expiry_date.grid(row=6, column=0, sticky=W)
        expiry_date_text = Entry(
            data_frame_left, textvariable=self.expiry_date, font=("arial", 12), width=35)
        expiry_date_text.grid(row=6, column=1)

        # daily dose
        daily_dose = Label(data_frame_left, font=(
            "arial", 12), text="Daily Dose ", padx=2, pady=6)
        daily_dose.grid(row=7, column=0, sticky=W)
        daily_dose_text = Entry(
            data_frame_left, textvariable=self.daily_dose, font=("arial", 12), width=35)
        daily_dose_text.grid(row=7, column=1)

        # Furthur Info
        furthur_info = Label(data_frame_left, font=(
            "arial", 12), text="Furthur Info  ", padx=3, pady=6)
        furthur_info.grid(row=0, column=2, sticky=W)
        furthur_info_text = Entry(
            data_frame_left, textvariable=self.furthur_information, font=("arial", 12), width=35)
        furthur_info_text.grid(row=0, column=3)

        # Blood Pressure
        blood_pressure = Label(data_frame_left, font=(
            "arial", 12), text="Blood Pressure  ", padx=3, pady=6)
        blood_pressure.grid(row=1, column=2, sticky=W)
        blood_pressure_text = Entry(
            data_frame_left, textvariable=self.blood_pressue_advice, font=("arial", 12), width=35)
        blood_pressure_text.grid(row=1, column=3)

        # Storage
        storage = Label(data_frame_left, font=("arial", 12),
                        text="Storage  ", padx=3, pady=6)
        storage.grid(row=2, column=2, sticky=W)
        storage_text = Entry(
            data_frame_left, textvariable=self.storage_advice, font=("arial", 12), width=35)
        storage_text.grid(row=2, column=3)

        # Medicine
        medicine = Label(data_frame_left, font=("arial", 12),
                         text="Medicine  ", padx=3, pady=6)
        medicine.grid(row=3, column=2, sticky=W)
        medicine_text = Entry(
            data_frame_left, textvariable=self.medicine, font=("arial", 12), width=35)
        medicine_text.grid(row=3, column=3)

        # Patient Id
        patient_id = Label(data_frame_left, font=(
            "arial", 12), text="Patient Id  ", padx=3, pady=6)
        patient_id.grid(row=4, column=2, sticky=W)
        patient_id_text = Entry(
            data_frame_left, textvariable=self.patient_id, font=("arial", 12), width=35)
        patient_id_text.grid(row=4, column=3)

        # Patient Name
        patient_name = Label(data_frame_left, font=(
            "arial", 12), text="Patient Name  ", padx=3, pady=6)
        patient_name.grid(row=5, column=2, sticky=W)
        patient_name_text = Entry(
            data_frame_left, textvariable=self.patient_name, font=("arial", 12), width=35)
        patient_name_text.grid(row=5, column=3)

        # Date of Birth
        date_of_birth = Label(data_frame_left, font=(
            "arial", 12), text="Date Of Birth  ", padx=3, pady=6)
        date_of_birth.grid(row=6, column=2, sticky=W)
        date_of_birth_text = Entry(
            data_frame_left, textvariable=self.date_of_birth, font=("arial", 12), width=35)
        date_of_birth_text.grid(row=6, column=3)

        # Patient Address
        patient_add = Label(data_frame_left, font=(
            "arial", 12), text="Patient Address  ", padx=3, pady=6)
        patient_add.grid(row=7, column=2, sticky=W)
        patient_add_text = Entry(
            data_frame_left, textvariable=patient_add, font=("arial", 12), width=35)
        patient_add_text.grid(row=7, column=3)

        # ############################ CLEARING ENTRY FIELD###########################
        def update_data():
            if not os.path.isfile('data.txt'):
                messagebox.showinfo("Nothing To Update")
            with open('data.txt', 'r')as f:
                content = f.readlines()
                my_dict = content[-1].split(',')
                text_ref.insert(0, my_dict[1][my_dict[1].find(':')+3:len(my_dict[1])-1])
                text_dose.insert(0, my_dict[2][my_dict[2].find(':')+3:len(my_dict[2])-1])
                no_of_tablets_text.insert(0, my_dict[3][my_dict[3].find(':')+3:len(my_dict[3])-1])
                lots_text.insert(0, my_dict[4][my_dict[4].find(':')+3:len(my_dict[4])-1])
                issue_date_text.insert(0, my_dict[5][my_dict[5].find(':')+3:len(my_dict[5])-1])
                expiry_date_text.insert(0, my_dict[6][my_dict[6].find(':')+3:len(my_dict[6])-1])
                medicine_text.insert(0, my_dict[7][my_dict[7].find(':')+3:len(my_dict[7])-1])
                patient_id_text.insert(0, my_dict[8][my_dict[8].find(':')+3:len(my_dict[8])-1])
                patient_name_text.insert(0, my_dict[9][my_dict[9].find(':')+3:len(my_dict[9])-1])
                date_of_birth_text.insert(0, my_dict[10][my_dict[10].find(':')+3:len(my_dict[10])-1])
                patient_add_text.insert(0, my_dict[11][my_dict[11].find(':')+3:len(my_dict[11])-2])
            


        def clear_field():
            text_ref.delete(0, 'end')
            text_dose.delete(0, 'end')
            no_of_tablets_text.delete(0, 'end')
            lots_text.delete(0, 'end')
            issue_date_text.delete(0, 'end')
            expiry_date_text.delete(0, 'end')
            daily_dose_text.delete(0, 'end')
            furthur_info_text.delete(0, 'end')
            blood_pressure_text.delete(0, 'end')
            storage_text.delete(0, 'end')
            medicine_text.delete(0, 'end')
            patient_id_text.delete(0, 'end')
            patient_name_text.delete(0, 'end')
            date_of_birth_text.delete(0, 'end')
            patient_add_text.delete(0, 'end')

        # ##################### DELETING PRESCRIPTION DATA
        def delete_table():
            for i in self.hospital_table.get_children():
                self.hospital_table.delete(i)

        # ############### CONTENT INSIDE RIGHT FRAME ######################
        # self.prescription_text = Text(data_frame_right, font=(
        #     "arial", 12), width=45, height=16, padx=2, pady=6)
        # self.prescription_text.grid(row=0, column=0)

        ############### CONTENT INSIDE BUTTONS FRAME ######################
        prescription_button = Button(button_frame, text="Prescription", command=add_prescription_data, bg="green", fg="white", padx=10, pady=10, font=(
            "arial", 12, "bold"), width=28)
        prescription_button.grid(row=0, column=0)

        # prescription_data = Button(button_frame,text="Prescription Data",command=show_table_data,bg="green",fg="white", padx=10, pady=10,font=(
        #     "arial", 12,"bold"),width=28)
        # prescription_data.grid(row=0,column=1)   this is tranfered  below

        update = Button(button_frame, text="Update", command=update_data,bg="green", fg="white", padx=10, pady=10, font=(
            "arial", 12, "bold"), width=28)
        update.grid(row=0, column=2)

        delete = Button(button_frame, text="Delete", command=delete_table, bg="green", fg="white", padx=10, pady=10, font=(
            "arial", 12, "bold"), width=28)
        delete.grid(row=0, column=3)

        reset = Button(button_frame, text="Reset", command=clear_field, bg="green", fg="white", padx=10, pady=10, font=(
            "arial", 12, "bold"), width=28)
        reset.grid(row=0, column=4)

        ############### CONTENT INSIDE DETAILS FRAME ######################
        # ---------------TABLE-----------
        scroll_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(details_frame, columns=("name_of_tablets", "reference_no",
                                                                   "dose", "no_of_tablets", "lot", "issued_date", "expiry_date", "medicine",
                                                                   "pname", "pid", "dob", "padd"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("name_of_tablets", text="Name Of Tablets")
        self.hospital_table.heading("reference_no", text="Reference Number")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("no_of_tablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issued_date", text="Issued Date")
        self.hospital_table.heading("expiry_date", text="Expiry Date")
        self.hospital_table.heading("medicine", text="Medicine")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("pid", text="Patient Id")
        self.hospital_table.heading("dob", text="Date Of Birth")
        self.hospital_table.heading("padd", text="Patient Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("name_of_tablets", width=100)
        self.hospital_table.column("reference_no", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("no_of_tablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issued_date", width=100)
        self.hospital_table.column("expiry_date", width=100)
        self.hospital_table.column("medicine", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("pid", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("padd", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)

        def show_table_data():
            delete_table()
            if not os.path.isfile('data.txt'):
                return
            with open('data.txt', 'r')as f:
                content = f.readlines()
                # if(content == []):
                #     messagebox.showerror("Error", "Nothing to Show")
                #     return
                for data in content:
                    my_dict = data.split(',')
                    self.hospital_table.insert('', 'end', text="1", values=('{}'.format(my_dict[0][my_dict[0].find(':')+3:len(my_dict[0])-1]),
                                                                            '{}'.format(
                                                                                my_dict[1][my_dict[1].find(':')+3:len(my_dict[1])-1]),
                                                                            '{}'.format(
                                                                                my_dict[2][my_dict[2].find(':')+3:len(my_dict[2])-1]),
                                                                            '{}'.format(
                                                                                my_dict[3][my_dict[3].find(':')+3:len(my_dict[3])-1]),
                                                                            '{}'.format(
                                                                                my_dict[4][my_dict[4].find(':')+3:len(my_dict[4])-1]),
                                                                            '{}'.format(
                                                                                my_dict[5][my_dict[5].find(':')+3:len(my_dict[5])-1]),
                                                                            '{}'.format(
                                                                                my_dict[6][my_dict[6].find(':')+3:len(my_dict[6])-1]),
                                                                            '{}'.format(
                                                                                my_dict[7][my_dict[7].find(':')+3:len(my_dict[7])-1]),
                                                                            '{}'.format(
                                                                                my_dict[8][my_dict[8].find(':')+3:len(my_dict[8])-1]),
                                                                            '{}'.format(
                                                                                my_dict[9][my_dict[9].find(':')+3:len(my_dict[9])-1]),
                                                                            '{}'.format(
                                                                                my_dict[10][my_dict[10].find(':')+3:len(my_dict[10])-1]),
                                                                            '{}'.format(
                                                                                my_dict[11][my_dict[11].find(':')+3:len(my_dict[11])-2])
                                                                            ))
                self.hospital_table.pack(fill=BOTH, expand=1)
        prescription_data = Button(button_frame, text="Prescription Data", command=show_table_data, bg="green", fg="white", padx=10, pady=10, font=(
            "arial", 12, "bold"), width=28)
        prescription_data.grid(row=0, column=1)


root = Tk()
obj = Hospital(root)
root.mainloop()
