import email.message
import smtplib



def send_email(player_email, player_role, from_email, from_password):

    msg = email.message.EmailMessage()
    msg["From"] = from_email
    msg["To"] = player_email
    msg["Subject"] = player_role
    msg.set_content(f"You are {player_role} player.")

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(from_email, from_password)
    server.send_message(msg)
    server.close()
    print(f"Email to {player_email} has been sent.")