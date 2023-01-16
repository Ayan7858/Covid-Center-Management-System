# import smtplib
# import imghdr
# from email.message import EmailMessage
# from tkinter import messagebox
#
# import mysql.connector
#
#
# sender_email = "care19centre@gmail.com"
#
#
# #def take_email():
#     # conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
#     #                                auth_plugin='mysql_native_password')
#     # my_cursor = conn.cursor()
#     # my_cursor.execute = "select email=%s from book_table where pin=%s"
#     # rec_email = my_cursor
#     # conn.commit()
#     # conn.close()
#     # messagebox.showinfo("Success", "Report Sent Successfully")
#     # return rec_email
#
#
#
# password =  "care19_python"
#
# msg = EmailMessage()
# msg['Subject'] = 'check out pic'
# msg['From'] = sender_email
# msg['To']  =
# msg.set_content('Image attached.')
#
# with open('covid report.png','rb') as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name
#
# msg.add_attachment(file_data,maintype='image',subtype=file_type, filename=file_name)
#
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(sender_email,password)
#     smtp.send_message(msg)