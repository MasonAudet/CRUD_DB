# Author: Mason Audet
# Due Date: 12/13/23
# Description: This is a python program that uses streamlit and mysqlconnector to make a crud web application 
# that runs on a local host.


import mysql.connector
from mysql.connector import Error
import streamlit as st
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123!2023",
    database="project2"
)

mycursor = mydb.cursor()
print("Connection Established")

def main():
    st.title("CRUD GUI for Project 2: CSE 5720")
    st.write("Welcome to the CRUD GUI for CSE 5720's Project 2!\nPlease select an available option from the left to begin.")

    crud_option = st.sidebar.selectbox("Select an operation", ("Create", "Read", "Update", "Delete", "Custom Query"), index=None)

    if crud_option == "Create":
        st.header("Create a Record")
        create_option = st.selectbox("Select a table to create a record for", ("Authors", "Customer", "Publishers", "Subjects", "TitleAuthors", "Titles"), index=None)

        if create_option == "Authors":

            st.subheader("Create a record for Authors")
            auID = st.text_input("Enter Author's ID")
            aName = st.text_input("Enter Author's Name")
            email = st.text_input("Enter Email")
            phone = st.text_input("Enter Phone")

            if st.button("Create"):
                sql = "insert into authors(auID,aName,email,phone) values(%s,%s,%s,%s)"
                val = (auID, aName, email, phone)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully added to the table!")




        if create_option == "Customer":

            st.subheader("Create a record for Customer")
            custID = st.text_input("Enter Customer's ID")
            custName = st.text_input("Enter Customer's Name")
            zip = st.text_input("Enter Zip Code")
            city = st.text_input("Enter City")
            state = st.text_input("Enter State")

            if st.button("Create"):
                sql = "insert into customer(custID,custName,zip,city,state) values(%s,%s,%s,%s,%s)"
                val = (custID, custName, zip, city, state)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully added to the table!")




        if create_option == "Publishers":

            st.subheader("Create a record for Publishers")
            pubID = st.text_input("Enter Publisher's ID")
            pname = st.text_input("Enter Publisher's Name")
            email = st.text_input("Enter Email")
            phone = st.text_input("Enter Phone")

            if st.button("Create"):
                sql = "insert into publishers(pubID,pname,email,phone) values(%s,%s,%s,%s)"
                val = (pubID, pname, email, phone)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully added to the table!")




        if create_option == "Subjects":

            st.subheader("Create a record for Subjects")
            subID = st.text_input("Enter a Subject ID")
            sName = st.text_input("Enter Subject Name")

            if st.button("Create"):
                sql = "insert into subjects(subID,sName) values(%s,%s)"
                val = (subID, sName)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully added to the table!")




        if create_option == "TitleAuthors":

            st.subheader("Create a record for TitleAuthors")
            titleID = st.text_input("Enter a Title ID")
            auID = st.text_input("Enter an Author ID")
            importance = st.text_input("Enter Importance Level")

            if st.button("Create"):
                sql = "insert into titleauthors(titleID,auID,importance) values(%s,%s,%s)"
                val = (subID, sName)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully added to the table!")




        if create_option == "Titles":

            st.subheader("Create a record for Titles")
            titleID = st.text_input("Enter Title ID")
            title = st.text_input("Enter Title Name")
            pubID = st.text_input("Enter Pub ID")
            subID = st.text_input("Enter Sub ID")
            pubDate = st.text_input("Enter Date Published (ex. 2002-04-02)")
            cover = st.text_input("Enter Cover Type (HARD COVER or PAPER BACK)")
            price = st.text_input("Enter Price (ex. 345)")

            if st.button("Create"):
                sql = "insert into titles(titleID,title,pubID,subID,pubDate,cover,price) values(%s,%s,%s,%s,%s,%s,%s)"
                val = (titleID, title, pubID, subID, pubDate, cover, price)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully added to the table!")


    elif crud_option == "Read":
        st.header("Read Records based on a selected table")
        read_option = st.selectbox("Select a table to read records from", ("Authors", "Customer", "Publishers", "Subjects", "TitleAuthors", "Titles"), index=None)

        if read_option == "Authors":

            st.subheader("Displaying Records for Authors")

            mycursor.execute("select * from authors")
            result = mycursor.fetchall()
            df = pd.DataFrame(result)
            df.columns = ["auID", "aName", "email", "phone"]
            st.table(df)



        if read_option == "Customer":

            st.subheader("Displaying Records for Customer")

            mycursor.execute("select * from customer")
            result = mycursor.fetchall()
            df = pd.DataFrame(result)
            df.columns = ["custID", "custname", "zip", "city", "state"]
            st.table(df)



        if read_option == "Publishers":

            st.subheader("Displaying Records for Publishers")

            mycursor.execute("select * from publishers")
            result = mycursor.fetchall()
            df = pd.DataFrame(result)
            df.columns = ["pubID", "pname", "email", "phone"]
            st.table(df)



        if read_option == "Subjects":

            st.subheader("Displaying Records for Subjects")

            mycursor.execute("select * from subjects")
            result = mycursor.fetchall()
            df = pd.DataFrame(result)
            df.columns = ["subID", "sName"]
            st.table(df)



        if read_option == "TitleAuthors":

            st.subheader("Displaying Records for TitleAuthors")

            mycursor.execute("select * from titleauthors")
            result = mycursor.fetchall()
            df = pd.DataFrame(result)
            df.columns = ["titleID", "auID", "importance"]
            st.table(df)



        if read_option == "Titles":

            st.subheader("Displaying Records for Titles")

            mycursor.execute("select * from titles")
            result = mycursor.fetchall()
            df = pd.DataFrame(result)
            df.columns = ["titleID", "title", "pubID", "subID", "pubDate", "cover", "price"]
            st.table(df)


    elif crud_option == "Update":
        st.header("Update a Record")
        update_option = st.selectbox("Select a table to update a record for", ("Authors", "Customer", "Publishers", "Subjects", "TitleAuthors", "Titles"), index=None)

        if update_option == "Authors":

            st.subheader("Enter an existing Authors ID to edit its corresponding data.")
            auID = st.text_input("Enter Author's ID")
            st.subheader("Enter new information in the fields below.")
            aName = st.text_input("Enter Author's Name")
            email = st.text_input("Enter Email")
            phone = st.text_input("Enter Phone")

            if st.button("Make Changes"):
                sql = "update authors set aName=%s, email=%s, phone=%s where auID=%s"
                val = (aName, email, phone, auID)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully updated!")



        if update_option == "Customer":

            st.subheader("Enter an existing Customer ID to edit its corresponding data.")
            custID = st.text_input("Enter Customer ID")
            st.subheader("Enter new information in the fields below.")
            custName = st.text_input("Enter Customer's Name")
            zip = st.text_input("Enter Zip")
            city = st.text_input("Enter City")
            state = st.text_input("Enter State")

            if st.button("Make Changes"):
                sql = "update customer set custName=%s, zip=%s, city=%s, state=%s where custID=%s"
                val = (custName, zip, city, state, custID)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully updated!")



        if update_option == "Publishers":

            st.subheader("Enter an existing Pub ID to edit its corresponding data.")
            pubID = st.text_input("Enter Pub ID")
            st.subheader("Enter new information in the fields below.")
            pname = st.text_input("Enter Publisher's Name")
            email = st.text_input("Enter Email")
            phone = st.text_input("Enter Phone")

            if st.button("Make Changes"):
                sql = "update publishers set pname=%s, email=%s, phone=%s where pubID=%s"
                val = (pname, email, phone, pubID)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully updated!")



        if update_option == "Subjects":

            st.subheader("Enter an existing Sub ID to edit its corresponding data.")
            subID = st.text_input("Enter Sub ID")
            st.subheader("Enter new information in the field below.")
            sName = st.text_input("Enter Subject Name")

            if st.button("Make Changes"):
                sql = "update subjects set sName=%s where subID=%s"
                val = (sName, subID)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully updated!")



        if update_option == "TitleAuthors":

            st.subheader("Enter an existing Title ID to edit its corresponding data.")
            titleID = st.text_input("Enter Title ID")
            st.subheader("Enter new information in the fields below.")
            auID = st.text_input("Enter Author ID")
            importance = st.text_input("Enter Importance level")

            if st.button("Make Changes"):
                sql = "update titleauthors set auID=%s, importance=%s where titleID=%s"
                val = (auID, importance, titleID)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully updated!")



        if update_option == "Titles":

            st.subheader("Enter an existing Title ID to edit its corresponding data.")
            titleID = st.text_input("Enter Title ID")
            st.subheader("Enter new information in the fields below.")
            title = st.text_input("Enter Title")
            pubID = st.text_input("Enter pubID")
            subID = st.text_input("Enter subID")
            pubDate = st.text_input("Enter Date Published (ex. 2002-02-04)")
            cover = st.text_input("Enter Cover Type (PAPER BACK or HARD COVER)")
            price = st.text_input("Enter Price (ex. 345)")

            if st.button("Make Changes"):
                sql = "update titles set title=%s, pubID=%s, subID=%s, pubDate=%s, cover=%s, price=%s where titleID=%s"
                val = (title, pubID, subID, pubDate, cover, price, titleID)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully updated!")


    elif crud_option == "Delete":
        st.header("Delete a Record")
        delete_option = st.selectbox("Select a table to delete a record from", ("Authors", "Customer", "Publishers", "Subjects", "TitleAuthors", "Titles"), index=None)

        if delete_option == "Authors":

            st.subheader("Enter an existing Authors ID to delete its record from the table.")
            auID = st.number_input("Enter Author's ID")

            if st.button("Delete Record"):
                sql = "delete from authors where auID=%s"
                val = (auID,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully deleted!")



        if delete_option == "Customer":

            st.subheader("Enter an existing Customer ID to delete its record from the table.")
            custID = st.number_input("Enter Customer ID")

            if st.button("Delete Record"):
                sql = "delete from customer where custID=%s"
                val = (custID,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully deleted!")



        if delete_option == "Publishers":

            st.subheader("Enter an existing Pub ID to delete its record from the table.")
            pubID = st.number_input("Enter Pub ID")

            if st.button("Delete Record"):
                sql = "delete from publishers where pubID=%s"
                val = (pubID,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully deleted!")



        if delete_option == "Subjects":

            st.subheader("Enter an existing Sub ID to delete its record from the table.")
            subID = st.text_input("Enter Sub ID")

            if st.button("Delete Record"):
                sql = "delete from subjects where subID=%s"
                val = (subID,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully deleted!")



        if delete_option == "TitleAuthors":

            st.subheader("Enter an existing Title ID to delete its record from the table.")
            titleID = st.number_input("Enter Title ID")

            if st.button("Delete Record"):
                sql = "delete from titleauthors where titleID=%s"
                val = (titleID,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully deleted!")



        if delete_option == "Titles":

            st.subheader("Enter an existing Title ID to delete its record from the table.")
            titleID = st.number_input("Enter Title ID")

            if st.button("Delete Record"):
                sql = "delete from titles where titleID=%s"
                val = (titleID,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record was successfully deleted")


    elif crud_option == "Custom Query":

        userText = st.text_area("Please enter your custom query in the box below and click enter to run it.")

        if st.button("Enter"):
            mycursor.execute(userText)
            mydb.commit()
            st.success("Your query was successfully ran!")


if __name__ == "__main__":
    main()