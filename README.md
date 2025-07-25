# COMP6441
Project Implementation

For all the files, the libraries listed at the top will need to be installed to run the implementations. You can do this through pip install. You also need to have Python installed to run the files. This can be done by running python3 software_logger.py / python software_logger.py. 

software_keylogger.py
1. The log_file_path will need to be changed to your specific device directory
2. The email will need to be changed to your email. I recommend making a test one to be safe
3. For the password, I had to allow Gmail to generate a two-factor authentication password so I could successfully send emails using smtplib.
4. The keylogging_duration and repetitions variables can be altered to suit your needs. Currently, the file runs for 2 repetitions, each lasting 10 seconds. Hence, it sends emails with the log file in intervals of 10 seconds twice.

software_keylogger_obfuscated.py
This is the obfuscated version of software_keylogger.py. Runs like a normal Python file, but can not be edited easily like the original file.

hardware_keylogger.py
1. The usb_path should be altered to meet your USB path, along with a log.txt file in there to which the path should point.

hardware_keylogger_obfuscated.py
This is the obfuscated version of hardware_keylogger.py. Runs like a normal Python file, but can not be edited easily like the original file.
