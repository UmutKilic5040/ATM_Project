from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton
from PyQt5.QtCore import Qt
from pymongo import MongoClient
from bson.objectid import ObjectId

client=MongoClient("mongodb://localhost:27017/")
db=client["Info"]
person=db["Person1"]

target_id1="693eeb9406e3cb57ae437e23"
query1={"_id":ObjectId(target_id1)}
person_data=person.find_one(query1)

target_id2="6947deca5741e5273c3c7e30"
query2={"_id":ObjectId(target_id2)}
paying_data=person.find_one(query2)

target_id3="694a9c0d160630f8064c47ec"
query3={"_id":ObjectId(target_id3)}
tax_data=person.find_one(query3)

target_id4="694a9c29160630f8064c47ed"
query4={"_id":ObjectId(target_id4)}
credit_data=person.find_one(query4)

target_id5="694a9c3f160630f8064c47ee"
query5={"_id":ObjectId(target_id5)}
edu_data=person.find_one(query5)

class Paying(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ödeme İşlemleri")
        self.setFixedSize(990,800)
        self.initUI()
    
    def initUI(self):
        self.master_layout=QVBoxLayout()

        self.text = QLabel("LÜTFEN YAPMAK İSTEDİĞİNİZ ÖDEMEYİ SEÇİNİZ")
        self.text.setStyleSheet("font-size:40px; color:red; font-family:Arial")

        self.bill = QPushButton("Fatura Ödemeleri")
        self.bill.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.tax = QPushButton("Vergi ve Devlet Ödemeleri")
        self.tax.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.credit = QPushButton("Borç ve Kredi Ödemeleri")
        self.credit.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.edu = QPushButton("Eğitim ve Sınav Ödemeleri")
        self.edu.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.geri=QPushButton("Geri Dön")
        self.geri.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        self.row4 = QHBoxLayout()
        
        self.row1.addWidget(self.text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.row2.addWidget(self.bill)
        self.row2.addWidget(self.tax)
        self.row3.addWidget(self.credit)
        self.row3.addWidget(self.edu)
        self.row4.addWidget(self.geri)
        
        self.geri.setFixedWidth(479)        
        self.row4.addStretch()

        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row3)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row4)
        self.master_layout.addStretch()

        self.setLayout(self.master_layout)

        self.setStyleSheet("background:darkblue")

        #Butonlar
        self.bill.clicked.connect(self.go_to_bills)
        self.tax.clicked.connect(self.go_to_tax)
        self.credit.clicked.connect(self.go_to_credit)
        self.edu.clicked.connect(self.go_to_edu)
        self.geri.clicked.connect(self.get_back_from_paying)


    def go_to_bills(self):
        self.go_bills=Bill()
        self.go_bills.show()
        self.close()
    
    def go_to_tax(self):
        self.go_tax=Tax()
        self.go_tax.show()
        self.close()

    def go_to_credit(self):
        self.go_credit=Credit()
        self.go_credit.show()
        self.close()

    def go_to_edu(self):
        self.go_edu=Edu()
        self.go_edu.show()
        self.close()

    def get_back_from_paying(self):
        from main5 import MotherPage
        self.get_back_to_menu=MotherPage()
        self.get_back_to_menu.show()
        self.close()

class Bill(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fatura Ödemeleri")
        self.setFixedSize(990,800)
        self.billUI()
    
    def billUI(self):
        self.master_layout=QVBoxLayout()
        
        self.text=QLabel("ÖDEMEK İSTEDİĞİNİZ FATURA İŞLEMİNİ SEÇİNİZ")
        self.text.setStyleSheet("font-size:40px; color:red; font-family:Arial")
        
        self.electric_bill=QPushButton("Elektrik Faturası (673 TL Ödenmedi)")
        self.electric_bill.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.water_bill=QPushButton("Su Faturası (430 TL Ödenmedi)")
        self.water_bill.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.natgas_bill=QPushButton("Doğalgaz Faturası (1023 TL Ödenmedi)")
        self.natgas_bill.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.tel_bill=QPushButton("Telefon Faturası (200 TL Ödenmedi)")
        self.tel_bill.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.int_bill=QPushButton("İnternet Faturası (552 TL Ödenmedi)")
        self.int_bill.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.back=QPushButton("Geri Dön")
        self.back.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.row1=QHBoxLayout()
        self.row2=QHBoxLayout()
        self.row3=QHBoxLayout()
        self.row4=QHBoxLayout()
        self.row5=QHBoxLayout()

        self.row1.addWidget(self.text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.row2.addWidget(self.electric_bill)
        self.row2.addWidget(self.water_bill)
        self.row3.addWidget(self.natgas_bill)
        self.row3.addWidget(self.tel_bill)
        self.row4.addWidget(self.int_bill)
        self.row4.addWidget(self.back)

        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row3)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row4)
        self.master_layout.addStretch()

        self.setLayout(self.master_layout)
        self.setStyleSheet("background:darkblue")

        #Butonlar ve kontrol
        self.electric_bill.clicked.connect(self.elect_payed)
        if paying_data["electricty_bill"] == 673:
            self.electric_bill.setText("Elektrik Faturası (Ödendi)")
            self.electric_bill.setEnabled(False)
            self.electric_bill.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
        
        self.water_bill.clicked.connect(self.water_payed)
        if paying_data["water_bill"] == 430:
            self.water_bill.setText("Su Faturası (Ödendi)")
            self.water_bill.setEnabled(False)
            self.water_bill.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

        self.natgas_bill.clicked.connect(self.natgas_payed)
        if paying_data["naturalgas_bill"] == 1023:
            self.natgas_bill.setText("Doğalgaz Faturası (Ödendi)")
            self.natgas_bill.setEnabled(False)
            self.natgas_bill.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

        self.tel_bill.clicked.connect(self.tel_payed)
        if paying_data["telephone_bill"] == 200:
            self.tel_bill.setText("Telefon Faturası (Ödendi)")
            self.tel_bill.setEnabled(False)
            self.tel_bill.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

        self.int_bill.clicked.connect(self.int_payed)
        if paying_data["internet_bill"] == 552:
            self.int_bill.setText("İnternet Faturası (Ödendi)")
            self.int_bill.setEnabled(False)
            self.int_bill.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

        self.back.clicked.connect(self.get_back_to_paying)


    #Buton fonksiyonları

    def elect_payed(self):
        if paying_data["electricty_bill"] == 0:
            self.current_balance = person_data["current_value"]
            self.bill_amount=673

            self.new_amount = self.current_balance - self.bill_amount

            self.new_value = {"$set":{"current_value":self.new_amount}}
            self.payed_elect = {"$set":{"electricty_bill":self.bill_amount}}

            person.update_one(query1,self.new_value)
            person.update_one(query2,self.payed_elect)

            person_data["current_value"] = self.new_amount  
            paying_data["electricty_bill"] = self.bill_amount

            self.electric_bill.setText("Elektrik Faturası (Ödendi)")
            self.electric_bill.setEnabled(False)
            self.electric_bill.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

    def water_payed(self):
        if paying_data["water_bill"]==0:
            self.current_balance = person_data["current_value"]
            self.bill_amount = 430

            self.new_amount = self.current_balance - self.bill_amount

            self.new_value = {"$set":{"current_value":self.new_amount}}
            self.payed_elect = {"$set":{"water_bill":self.bill_amount}}

            person.update_one(query1,self.new_value)
            person.update_one(query2,self.payed_elect)

            person_data["current_value"] = self.new_amount  
            paying_data["water_bill"] = self.bill_amount

            self.water_bill.setText("Su Faturası (Ödendi)")
            self.water_bill.setEnabled(False)
            self.water_bill.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

    def natgas_payed(self):
        if paying_data["naturalgas_bill"]==0:
            self.current_balance = person_data["current_value"]
            self.bill_amount = 1023

            self.new_amount = self.current_balance - self.bill_amount

            self.new_value = {"$set":{"current_value":self.new_amount}}
            self.payed_elect = {"$set":{"naturalgas_bill":self.bill_amount}}

            person.update_one(query1,self.new_value)
            person.update_one(query2,self.payed_elect)

            person_data["current_value"] = self.new_amount  
            paying_data["naturalgas_bill"] = self.bill_amount

            self.natgas_bill.setText("Doğalgaz Faturası (Ödendi)")
            self.natgas_bill.setEnabled(False)
            self.natgas_bill.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

    def tel_payed(self):
        if paying_data["telephone_bill"]==0:
            self.current_balance=person_data["current_value"]
            self.bill_amount = 200

            self.new_amount = self.current_balance - self.bill_amount

            self.new_value = {"$set":{"current_value":self.new_amount}}
            self.payed_elect = {"$set":{"telephone_bill":self.bill_amount}}

            person.update_one(query1,self.new_value)
            person.update_one(query2,self.payed_elect)

            person_data["current_value"] = self.new_amount  
            paying_data["telephone_bill"] = self.bill_amount

            self.tel_bill.setText("Telefon Faturası (Ödendi)")
            self.tel_bill.setEnabled(False)
            self.tel_bill.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
    
    def int_payed(self):
        if paying_data["internet_bill"]==0:
            self.current_balance=person_data["current_value"]
            self.bill_amount = 552

            self.new_amount = self.current_balance - self.bill_amount

            self.new_value = {"$set":{"current_value":self.new_amount}}
            self.payed_elect = {"$set":{"internet_bill":self.bill_amount}}

            person.update_one(query1,self.new_value)
            person.update_one(query2,self.payed_elect)

            person_data["current_value"] = self.new_amount  
            paying_data["internet_bill"] = self.bill_amount

            self.int_bill.setText("İnternet Faturası (Ödendi)")
            self.int_bill.setEnabled(False)
            self.int_bill.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

    def get_back_to_paying(self):
        self.get_back_paying=Paying()
        self.get_back_paying.show()
        self.close()

class Tax(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vergi ve Devlet Ödemeleri")
        self.setFixedSize(990,800)
        self.taxUI()
    
    def taxUI(self):
        self.master_layout=QVBoxLayout()
        
        self.text=QLabel("ÖDEME YAPMAK İSTEDİĞNİZ İŞLEMİ SEÇİNİZ")
        self.text.setStyleSheet("font-size:40px; color:red; font-family:Arial")

        self.mtv=QPushButton("Motorlu Taşıtlar Vergisi (3372 TL Ödenmedi)")
        self.mtv.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.traff=QPushButton("Trafik Cezaları (2167 TL Ödenmedi)")
        self.traff.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.passport=QPushButton("Pasaport Harcı (5630 TL Ödenmedi)")
        self.passport.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.d_license=QPushButton("Ehliyet Harcı (7438 TL Ödenmedi)")
        self.d_license.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.sgk=QPushButton("SGK Primi (4225 TL Ödenmedi)")
        self.sgk.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.back=QPushButton("Geri Dön")
        self.back.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.row1=QHBoxLayout()
        self.row2=QHBoxLayout()
        self.row3=QHBoxLayout()
        self.row4=QHBoxLayout()

        self.row1.addWidget(self.text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.row2.addWidget(self.mtv)
        self.row2.addWidget(self.traff)
        self.row3.addWidget(self.passport)
        self.row3.addWidget(self.d_license)
        self.row4.addWidget(self.sgk)
        self.row4.addWidget(self.back)

        self.master_layout.addStretch
        self.master_layout.addLayout(self.row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row3)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row4)
        self.master_layout.addStretch()

        self.setLayout(self.master_layout)
        self.setStyleSheet("background:darkblue")

        self.mtv.clicked.connect(self.paying_mtv)
        if tax_data["mtv"] == 3372:
            self.mtv.setText("Motorlu Taşıtlar Vergisi (Ödendi)")
            self.mtv.setEnabled(False)
            self.mtv.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
        
        self.traff.clicked.connect(self.paying_traff)
        if tax_data["traffic"] == 2167:
            self.traff.setText("Trafik Cezaları (Ödendi)")
            self.traff.setEnabled(False)
            self.traff.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
        
        self.passport.clicked.connect(self.paying_passport)
        if tax_data["passport"] == 5630:
            self.passport.setText("Pasaport Harcı (Ödendi)")
            self.passport.setEnabled(False)
            self.passport.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
        
        self.d_license.clicked.connect(self.paying_d_licence)
        if tax_data["d_licence"] == 7438:
            self.d_license.setText("Ehliyet Harcı (Ödendi)")
            self.d_license.setEnabled(False)
            self.d_license.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
        
        self.sgk.clicked.connect(self.paying_sgk)
        if tax_data["sgk"] == 4225:
            self.sgk.setText("SGK Primi (Ödendi)")
            self.sgk.setEnabled(False)
            self.sgk.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
        
        self.back.clicked.connect(self.get_back_to_paying)


    def paying_mtv(self):
        if tax_data["mtv"] == 0:
            self.current_balance=person_data["current_value"]
            self.mtv_fee = 3372

            self.new_amount= self.current_balance - self.mtv_fee
            
            self.new_value={"$set":{"current_value":self.new_amount}}
            self.mtv_amount={"$set":{"mtv":self.mtv_fee}}

            person.update_one(query1,self.new_value)
            person.update_one(query3,self.mtv_amount)

            person_data["current_value"] = self.new_amount  
            tax_data["mtv"] = self.mtv_fee

            self.mtv.setText("Motorlu Taşıtlar Vergisi (Ödendi)")
            self.mtv.setEnabled(False)
            self.mtv.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
    
    def paying_traff(self):
        if tax_data["traffic"] == 0:
            self.current_balance=person_data["current_value"]
            self.traff_fee = 2167

            self.new_amount= self.current_balance - self.traff_fee
            
            self.new_value={"$set":{"current_value":self.new_amount}}
            self.traff_amount={"$set":{"traffic":self.traff_fee}}

            person.update_one(query1,self.new_value)
            person.update_one(query3,self.traff_amount)

            person_data["current_value"] = self.new_amount  
            tax_data["traffic"] = self.traff_fee

            self.traff.setText("Trafik Cezaları (Ödendi)")
            self.traff.setEnabled(False)
            self.traff.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
    
    def paying_passport(self):
        if tax_data["passport"] == 0:
            self.current_balance=person_data["current_value"]
            self.passport_fee = 5630

            self.new_amount= self.current_balance - self.passport_fee
            
            self.new_value={"$set":{"current_value":self.new_amount}}
            self.passport_amount={"$set":{"passport":self.passport_fee}}

            person.update_one(query1,self.new_value)
            person.update_one(query3,self.passport_amount)

            person_data["current_value"] = self.new_amount  
            tax_data["passport"] = self.passport_fee

            self.passport.setText("Pasaport Harcı (Ödendi)")
            self.passport.setEnabled(False)
            self.passport.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
    

    def paying_d_licence(self):
        if tax_data["d_licence"] == 0:
            self.current_balance=person_data["current_value"]
            self.licence_fee = 7438

            self.new_amount= self.current_balance - self.licence_fee
            
            self.new_value={"$set":{"current_value":self.new_amount}}
            self.licence_amount={"$set":{"d_licence":self.licence_fee}}

            person.update_one(query1,self.new_value)
            person.update_one(query3,self.licence_amount)

            person_data["current_value"] = self.new_amount  
            tax_data["d_licence"] = self.licence_fee

            self.d_license.setText("Ehliyet Harcı (Ödendi)")
            self.d_license.setEnabled(False)
            self.d_license.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
    
    def paying_sgk(self):
        if tax_data["sgk"] == 0:
            self.current_balance=person_data["current_value"]
            self.sgk_fee = 4225

            self.new_amount= self.current_balance - self.sgk_fee
            
            self.new_value={"$set":{"current_value":self.new_amount}}
            self.sgk_amount={"$set":{"sgk":self.sgk_fee}}

            person.update_one(query1,self.new_value)
            person.update_one(query3,self.sgk_amount)

            person_data["current_value"] = self.new_amount  
            tax_data["sgk"] = self.sgk_fee

            self.sgk.setText("SGK Primi (Ödendi)")
            self.sgk.setEnabled(False)
            self.sgk.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
    
    def get_back_to_paying(self):
        self.get_back_paying=Paying()
        self.get_back_paying.show()
        self.close()

class Credit(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Borç ve Kredi Ödemeleri")
        self.setFixedSize(990,800)
        self.creditUI()

    def creditUI(self):
        self.master_layout=QVBoxLayout()
        self.text=QLabel("ÖDEMEK İSTEDİĞNİZ BORÇ İŞLEMİNİ SEÇİNİZ")
        self.text.setStyleSheet("font-size:40px; color:red; font-family:Arial")

        self.credit_card=QPushButton("Kredi Kartı Taksidi (500 TL Ödenmedi)")
        self.credit_card.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.credit_debt=QPushButton("Kredi Taksidi (1050 TL Ödenmedi)")
        self.credit_debt.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.back=QPushButton("Geri Dön")
        self.back.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.row1=QHBoxLayout()
        self.row2=QHBoxLayout()
        self.row3=QHBoxLayout()

        self.row1.addWidget(self.text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.row2.addWidget(self.credit_card)
        self.row2.addWidget(self.credit_debt)
        self.row3.addWidget(self.back)

        self.row3.addStretch()
        self.back.setFixedWidth(479)

        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row3)
        self.master_layout.addStretch()
        
        self.setLayout(self.master_layout)

        self.setStyleSheet("background:darkblue")

        self.credit_card.clicked.connect(self.paying_credit_card)
        if credit_data["credit_card_debt"] == 500:
            self.credit_card.setText("Kredi Kartı Taksidi (Ödendi)")
            self.credit_card.setEnabled(False)
            self.credit_card.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
        
        self.credit_debt.clicked.connect(self.paying_credit_debt)
        if credit_data["credit_debt"] == 1050:
            self.credit_debt.setText("Kredi Taksidi (Ödendi)")
            self.credit_debt.setEnabled(False)
            self.credit_debt.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

        self.back.clicked.connect(self.get_back_to_paying)

    def paying_credit_card(self):
        if credit_data["credit_card_debt"] == 0:
            self.current_balance=person_data["current_value"]
            self.card_debt = 500

            self.new_amount= self.current_balance - self.card_debt
            
            self.new_value={"$set":{"current_value":self.new_amount}}
            self.credit_card_amount={"$set":{"credit_card_debt":self.card_debt}}

            person.update_one(query1,self.new_value)
            person.update_one(query4,self.credit_card_amount)

            person_data["current_value"] = self.new_amount  
            credit_data["credit_card_debt"] = self.card_debt

            self.credit_card.setText("Kredi Kartı Taksidi (Ödendi)")
            self.credit_card.setEnabled(False)
            self.credit_card.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")
    
    def paying_credit_debt(self):
        if credit_data["credit_debt"] == 0:
            self.current_balance=person_data["current_value"]
            self.credit = 1050

            self.new_amount= self.current_balance - self.credit
            
            self.new_value={"$set":{"current_value":self.new_amount}}
            self.credit_amount={"$set":{"credit_debt":self.credit}}

            person.update_one(query1,self.new_value)
            person.update_one(query4,self.credit_amount)

            person_data["current_value"] = self.new_amount  
            credit_data["credit_debt"] = self.credit

            self.credit_debt.setText("Kredi Taksidi (Ödendi)")
            self.credit_debt.setEnabled(False)
            self.credit_debt.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")


    def get_back_to_paying(self):
        self.get_back_paying=Paying()
        self.get_back_paying.show()
        self.close()

class Edu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eğitim ve Sınav Ödemeleri")
        self.setFixedSize(990,800)
        self.eduUI()
    
    def eduUI(self):
        self.master_layout=QVBoxLayout()

        self.text=QLabel("ÖDEME YAPMAK İSTEDİĞNİZ İŞLEMİ SEÇİNİZ")
        self.text.setStyleSheet("font-size:40px; color:red; font-family:Arial")

        self.osym=QPushButton("Üniversite Sınavı Harcı (900 TL Ödenmedi)")
        self.osym.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.uni_tuition=QPushButton("Üniversite Harcı (1677 TL Ödenmedi)")
        self.uni_tuition.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.back=QPushButton("Geri Dön")
        self.back.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.row1=QHBoxLayout()
        self.row2=QHBoxLayout()
        self.row3=QHBoxLayout()

        self.row1.addWidget(self.text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.row2.addWidget(self.osym)
        self.row2.addWidget(self.uni_tuition)
        self.row3.addWidget(self.back)

        self.row3.addStretch()
        self.back.setFixedWidth(479) 

        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row3)
        self.master_layout.addStretch()

        self.setLayout(self.master_layout)

        self.setStyleSheet("background: darkblue")
        
        self.osym.clicked.connect(self.paying_osym)
        if edu_data["osym"] == 900:
            self.osym.setText("Üniversite Sınavı Harcı (Ödendi)")
            self.osym.setEnabled(False)
            self.osym.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

        self.uni_tuition.clicked.connect(self.paying_uni_tuition)
        if edu_data["uni_tuition"] == 1677:
            self.uni_tuition.setText("Üniversite Harcı (Ödendi)")
            self.uni_tuition.setEnabled(False)
            self.uni_tuition.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

        self.back.clicked.connect(self.get_back_to_paying)

    def paying_osym(self):      
        if edu_data["osym"] == 0:
            self.current_balance=person_data["current_value"]
            self.fee = 900

            self.new_amount= self.current_balance - self.fee
            
            self.new_value={"$set":{"current_value":self.new_amount}}
            self.fee_amount={"$set":{"osym":self.fee}}

            person.update_one(query1,self.new_value)
            person.update_one(query5,self.fee_amount)

            person_data["current_value"] = self.new_amount  
            edu_data["osym"] = self.fee

            self.osym.setText("Üniversite Sınavı Harcı (Ödendi)")
            self.osym.setEnabled(False)
            self.osym.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

    def paying_uni_tuition(self):
        if edu_data["uni_tuition"] == 0:
            self.current_balance=person_data["current_value"]
            self.tuition=1677

            self.new_amount= self.current_balance - self.tuition
            
            self.new_value={"$set":{"current_value":self.new_amount}}
            self.tuition_amount={"$set":{"uni_tuition":self.tuition}}

            person.update_one(query1,self.new_value)
            person.update_one(query5,self.tuition_amount)

            person_data["current_value"] = self.new_amount  
            edu_data["uni_tuition"] = self.tuition

            self.uni_tuition.setText("Üniversite Harcı (Ödendi)")
            self.uni_tuition.setEnabled(False)
            self.uni_tuition.setStyleSheet("QPushButton {background: darkgray; border: 10px solid darkgray;border-radius: 16px; color: black; font-size: 20px; font-weight:bold}")

    def get_back_to_paying(self):
        self.get_back_paying=Paying()
        self.get_back_paying.show()
        self.close()