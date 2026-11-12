from mysql import connector
from datetime import datetime

class BloodDonorManager:
    def __init__(self):
        self.connection = connector.connect(
            user = "root",
            password = "Gopika@123",
            database = "blood_db_aug26",
            host = "localhost"
        )
        print("Connected Successfull..!")
        
    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
        
    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = """insert into donor (name, blood_group, phone, city, last_donation)
            values(%s, %s, %s, %s, %s)"""
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Data Inserted Successfully..!")
        except Exception as e:
            print(e)
            
    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
            #for i in records:
            #  print(i)
        except Exception as e:
            print(e)
            
    def retrieve(self, id=None):
        try:
            
            record = self.get_object(id=id)
            if record == None:
                print("No donors found..!")
            print(record)
        except Exception as e:
            print(e)
            
    def delete(self, id=None):
        try:
            record = self.get_object(id=id)
            if record != None:
                query = "delete from donor where id=%s"
                self.cursor.execute(query, (id,))
                self.connection.commit()
                print("Donor deleted successfully..!")
            else:
                print("No donors found..!")
        except Exception as e:
            print(e)

    def put(self,donor_id=None,**kwargs):
        try:
            record = self.get_object(donor_id=donor_id)
            if record is not None:
                placeholder = ''
                for i in kwargs.keys():
                    placeholder += i+ '=%s, '
                values = list(kwargs.values())
                placeholder = placeholder.rstrip(', ')
                print(placeholder)
                values.append(donor_id)
                query = f'update donor set {placeholder} where id =%s'
                self.cursor.execute(query,values)
                self.connection.commit()
                return True, 'donor details edited successfully'
            else:
               return False , 'Invalid donor id'
        except Exception as e:
            return False , str(e)
    
            
donor_instance = BloodDonorManager()
#donor_instance.post(name="Rahul", blood_group="O+", phone="987654311", city="Kochi", last_donation=datetime.today())
donor_instance.get()
#donor_instance.retrieve(id=3)
#donor_instance.delete(id=3)    
         
        
