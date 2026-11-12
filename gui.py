import streamlit as st 
from donorview import BloodDonorManager

donor_instance = BloodDonorManager()

tab1, tab2, tab3 = st.tabs(["Add Donor", "View Donors"])

blood_groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

with tab1:
    st.header("Add New Donor..!")
    name = st.text_input("Enter Donor Name")
    phone = st.text_input("Enter Donor Phone Number")
    blood_group = st.selectbox("Select Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
    city = st.text_input("Enter Donor City")
    last_donation = st.date_input("Enter Last Donation Date")
    if st.button("Submit"):
        donor_instance.post(name=name, blood_group=blood_group, phone=phone, city=city, last_donation=last_donation)
        st.success("Donor added successfully..!")
    
with tab2:
    st.header("View Blood Donor Details..!")
    records= donor_instance.get()
    st.dataframe(records)
    
with tab3:
    st.title("Update Donor Details")
    records = donor_instance.get()
    
    if records:
        donor_ids = [r[0] for r in records]
        #donor_ids = [1,5,6,7]
        id = st.selectbox("Select Donor ID", donor_ids, key="update_id")
        
        record = donor_instance.get_object(id=id)
        
        name = st.text_input("Enter your name :", value=record[1])
        phone = st.text_input("Enter Donor Phone Number", value=record[3])
        blood_group = st.selectbox("Select Your Blood Group", 
                                   blood_groups,
                                   index=blood_groups.index(record[2]),
                                   keys="update_group"
                                   )
        city = st.text_input("Enter Your City", value=record[4])
        last_donation = st.date_input("Last donation date :", value=record[5])
        
        if st.button("Update"):
            status, message = donor_instance.put(id=id,
                                                 name=name,
                                                 blood_group=blood_group,
                                                 city=city,
                                                 last_donation=last_donation)
            if status:
                st.success(message)
                st.rerun()
            else:
                st.error(message)
                
        else:
            st.warning("No donor found..!")
    
    
    

