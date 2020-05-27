import smtplib 
	
sender_email= "thisisjustfortesting23@gmail.com"
password= "adarsh123"
developer_mail="adrshcool200061@gmail.com"
s = smtplib.SMTP('smtp.gmail.com', 587) 

s.starttls()   

s.login(sender_email, password)
 
message = "Congrats! The model is trained with a accuracy you desired .."

s.sendmail(sender_email, developer_mail, message)

s.quit()

