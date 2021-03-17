#!/usr/bin/env python3
import subprocess
from os import system, sys, path
import getpass

def start():
    hello = ("[ Welcome to System Admin scripts, design by System Admin Mat Bao, maintanance: hiendt1@matbao.com, please enter your choice: ]\n1. Webserver\t2. Database\t3. Firewall\n4. File manager\t5. Manage DB\t6. Exit")
    print(hello.center(50))
    choice = input()
    sys.stdout.write("\033[F")
    if choice == "1":
        system("clear")
        install_webserver()
        main()
    elif choice == "2":
        system("clear")
        install_database()
        main()
    elif choice == "3":
        system("clear")
        config_imunify()
        main()
    elif choice == "4":
        print("Welcome to File Manager, please enter your choice:\n1. Backup\t2. Restore\t3. Disk usage\n4. Inodes usage\t 5. Back")
        reply = input()
        sys.stdout.write("\033[F")
        if reply == "1":
            system("clear")
            backup()
            main()
        elif reply == "2":
            system("clear")
            restore()
            main()
        elif reply == "3":
            system("clear")
            calculate()
            main()
        elif reply == "4":
            system("clear")
            inodes()
            main()
        elif reply == "5":
            system("clear")
            main()
    elif choice == "5":
        mysql()
    elif choice == "6":
        print("Ban muon thoat chuong trinh ? [Y/n]")
        reply = input()
        sys.stdout.write("\033[F")
        if reply == "Y" or reply == "y":
            print("Bye bye")
            sys.exit()
        elif reply == "n" or reply == "N":
            system("clear")
            print("Back to main page !!!!!!")
            main()
        else:
            system("clear")
            print("Back to main page !!!")
            main()
    else:
        print("Please enter again !!!")
        main()

def install_webserver():
    print("Welcome to page install Webserver, please enter your choice:\n 1. Nginx\t 2. Apache\t 3. Switch webserver\t 4. Back\t 5. Exit")
    reply = input()
    sys.stdout.write("\033[F")
    if reply == "1":
        if str(path.exists("/etc/nginx/")) == "True":
            print("Nginx was installed on server, please remove or clear it from server and run again !")
        else:
            print("Installing Nginx ...")
            result = system("apt-get update -y >/dev/null 2>&1" + ";" + "apt-get install nginx -y >/dev/null 2>&1")
            if result == "":
                print("Install completed")
            else:
                print("Install Error")
                install_webserver()
    elif reply == "2":
        if str(path.exists("/etc/apache2/")) == "True":
            print("Apache was installed on server, please remove or clear it from server and run again !")
        else:
            print("Installing Apache ...")
            system("apt-get update -y >/dev/null 2>&1" + ";" + "apt-get install apache2 -y >/dev/null 2>&1")
            print("Install completed")
    elif reply == "3":
        print("Please enter your choice:\n1. Nginx to Apache\n2. Apache to Nginx\n3. Back")
        choice = input()
        sys.stdout.write("\033[F")
        if choice == "1":
            print("Switching from Nginx to Apache2 ... ")
            if str(path.exists("/etc/nginx/")) == "True" and str(path.exists("/etc/apache2/")) == "False":
                print("Switching from Nginx to Apache2 ...")
                system("apt-get remove nginx* -y >/dev/null 2>&1" + ";" + "apt-get install apache2 -y >/dev/null 2>&1" + ";" + "rm -rf /etc/nginx >/dev/null 2>&1")
            elif str(path.exists("/etc/nginx/")) == "True" and str(path.exists("/etc/apache2")) == "True":
                print("Switching from Nginx to Apache2 ... ")
                system("systemctl stop nginx >/dev/null 2>&1" + ";" + "systemctl start apache2 >/dev/null 2>&1")
            elif str(path.exists("/etc/nginx/")) == "False" and str(path.exists("/etc/apache2/")) == "False":
                print("Nginx and Apache does not install on this server, do you want to install new webserver ? [Y/n]")
                reply_1 = input()
                sys.stdout.write("\033[F")
                if reply_1 == "Y" or reply_1 == "y":
                    print("Please choose type of webserver:\n 1. Nginx\t 2. Apache2\t 3. Back")
                    reply_2 = input()
                    sys.stdout.write("\033[F")
                    if reply_2 == "1":
                        print("Installing Nginx ... ")
                        result = system("apt-get update -y >/dev/null 2>&1" + ";" + "apt-get install nginx -y >/dev/null 2>&1")
                        if result == "":
                            print("Install completed")
                        else:
                            print("Can not install Nginx")
                    elif reply_2 == "2":
                        print("Install Apache2 ... ")
                        result_1 = system("apt-get update -y >/dev/null 2>&1" + ";" + "apt-get install apache2 -y >/dev/null 2>&1")
                        if result_1 == "":
                            print("Install completed")
                        else:
                            print("Can not install Apache2")
                    elif reply_2 == "3":
                        install_webserver()
                elif reply_1 == "N" or reply_1 == "n":
                    install_webserver()
            elif str(path.exists("/etc/nginx/")) == "False" and str(path.exists("/etc/apache2")) == "True":
                print("Apache2 already running on server !")
                install_webserver()
        if choice == "2":
            if str(path.exists("/etc/apache2/")) == "True" and str(path.exists("/etc/nginx/")) == "False":
                print("Switching from Nginx to Apache2 ...")
                result = system("apt-get remove nginx -y >/dev/null 2>&1" + ";" + "apt-get install apache2 -y >/dev/null 2>&1" + ";" + "rm -rf /etc/nginx >/dev/null 2>&1")
                if result == "":
                    print("Switch completed !")
                else:
                    print("Can not switch, please check again !")
            elif str(path.exists("/etc/apache2/")) == "True" and str(path.exists("/etc/nginx/")) == "True":
                print("Switching from Nginx to Apache2 ... ")
                result = system("systemctl stop nginx >/dev/null 2>&1" + ";" + "systemctl start apache2 >/dev/null 2>&1")
                if result == "":
                    print("Switch completed !")
                else:
                    print("Can not switch, please check again !")
            elif str(path.exists("/etc/apache2/")) == "False" and str(path.exists("/etc/nginx/")) == "False":
                print("Nginx and Apache does not install on this server, do you want to install new webserver ? [Y/n]")
                reply_1 = input()
                sys.stdout.write("\033[F")
                if reply_1 == "Y" or reply_1 == "y":
                    print("Please choose type of webserver:\n 1. Nginx\t 2. Apache2\t 3. Back")
                    reply_2 = input()
                    sys.stdout.write("\033[F")
                    if reply_2 == "1":
                        print("Installing Nginx ... ")
                        result = system("apt-get update -y >/dev/null 2>&1" + ";" + "apt-get install nginx -y >/dev/null 2>&1")
                        if result == "":
                            print("Install completed")
                        else:
                            print("Can not install Nginx")
                    elif reply_2 == "2":
                        print("Install Apache2 ... ")
                        result_1 = system("apt-get update -y >/dev/null 2>&1" + ";" + "apt-get install apache2 -y >/dev/null 2>&1")
                        if result_1 == "":
                            print("Install completed")
                        else:
                            print("Can not install Apache2")
                    elif reply_2 == "3":
                        install_webserver()
                elif reply_1 == "N" or reply_1 == "n":
                    install_webserver()
            elif str(path.exists("/etc/nginx/")) == "False" and str(path.exists("/etc/apache2")) == "True":
                print("Apache2 already running on server !")
                install_webserver()
        elif choice == "3":
            install_webserver()
    elif reply == "4":
        main()
    elif reply == "5":
        exit()
    else:
        print("Please enter again your choice !!!")
        install_webserver()

def install_database():
    print("Welcome to page install Database, Please enter your choice:\n1. Mariadb\t\t2. MySQL\t\t3. Back")
    reply = input()
    sys.stdout.write("\033[F")
    if reply == "1":
        if str(path.exists("/var/lib/mysql/")) == "False":
            print("Installing MariaDB ... ")
            result = system("apt update -y >/dev/null 2>&1" + ";" + "apt install mariadb-server mariadb-client -y >/dev/null 2>&1")
            if result == "":
                print("Install MariaDB completed !!!")
            else:
                print("Can not install MariaDB !!!")
        elif str(path.exists("/var/lib/mysql/")) == "True":
            print("MariaDB already running on server !")
            system("mariadb -V")
    elif reply == "2":
        if str(path.exists("/var/lib/mysql/")) == "False":
            print("Installing MySQL ... ")
            system("apt update -y >/dev/null 2>&1" + ";" + "apt install mysql-server mysql-client -y >/dev/null 2>&1")
            if result == "":
                print("Install MariaDB completed !!!")
            else:
                print("Can not install MariaDB !!!")
        elif str(path.exists("/var/lib/mysql")) == "True":
            print("MySQL already running on server !")
            system("mysql -V")
    elif reply == "3":
        main()

def inodes():
    user = str(input("User count Inodes: "))
    if user == "":
        system("clear")
        print("Please enter user again: ")
        inodes()
    else:
        system("clear")
        print("Calculating ...")
        system("find /home/"  + user + " " + """-printf "%h\n" | cut -d/ -f-2 | sort | uniq -c | sort -rn""") 
        print("Calculate completed !!!")

def backup():
    system("clear")
    command = "tar"
    command_1 = "mv"
    args = "-cvf"
    path = input("Vui long nhap du lieu can backup:")
    name = input("Vui long nhap ten can file:")
    store = input("Vui long nhap duong dan luu tru: ")
    print("Backing up ...")
    subprocess.call([command, args, name, path])
    subprocess.call([command_1, name, store])
    print("Backup completed")

def restore():
    system("clear")
    command = "unzip"
    args = "-d"
    path_file = input("File can restore la (vui long nhap duong dan day du): ")
    path_restore = input("Duong dan restore:")
    print("Restoring ...")
    subprocess.call([command, path_file, args, path_restore])
    print("Restore completed")

def calculate():
    system("clear")
    command = "du"
    args = "-sh"
    print("Vui long nhap duong dan can thong ke dung luong:\n 1. Log\t 2. Website\t 3. Home\t 4. Tmp\t 5. Back")
    choice = input()
    if choice == "1":
        path = "/var/log/"
        subprocess.call([command, args, path])
    elif choice == "2":
        domain = input("Domain: ")
        path = "/var/www/" + domain
        subprocess.call([command, args, path])
    elif choice == "3":
        path = "/home"
        subprocess.call([command, args, path])
    elif choice == "4":
        path = "/tmp"
        subprocess.call([command, args, path])
    elif choice == "5":
        main()

def config_imunify():
    print("Please enter your choice:\n 1. Add / Remove whitelist IP\t 2. Add / Remove blacklist IP\t 3. Add / Remove whitelist Country\n 4. Add / Remove blacklist Country\t 5. Back")
    reply = input()
    if reply == "1":
        system("clear")
        print("Please enter your choice:\n 1. Add\t 2. Remove\t 3. Back")
        choice = input()
        if choice == "1":
            command = "imunify360-agent whitelist ip add"
            ip = input("IP can add: ")
            args = "--comment"
            comment = input("Noi dung comment: ")
            subprocess.call([command, ip, args, comment])
        elif choice == "2":
            command = "imunify360-agent whitelist ip delete"
            ip = input("IP can remove: ")
            subprocess.call([command, ip])
        elif choice == "3":
            config_imunify()
    elif reply == "2":
        system("clear")
        print("Please enter your choice:\n 1. Add\t 2. Remove\t 3. Back")
        choice = input()
        if choice == "1":
            command = "imunify360-agent blacklist ip add"
            ip = input("IP can add: ")
            args = "--comment"
            comment = input("Noi dung comment: ")
            subprocess.call([command, ip, args, comment])
        elif choice == "2":
            command = "imunify360-agent blacklist ip remove"
            ip = input("IP can remove: ")
            subprocess.call([command, ip])
        elif choice == "3":
            config_imunify()
    elif reply == "3":
        system("clear")
        print("Please enter your choice:\n 1. Add\t 2. Remove\t 3. Back")
        choice = input()
        if choice == "1":
            command = "imunify360-agent whitelist country add"
            country = input("Country can add: ")
            args = "--comment"
            comment = input("Noi dung comment: ")
            subprocess.call([command, country, args, comment])
        elif choice == "2":
            command = "imunify360-agent whitelist country remove"
            country = input("Country can remove: ")
            subprocess.call([command, country])
        elif choice == "3":
            config_imunify()
    elif reply == "4":
        system("clear")
        print("Please enter your choice:\n 1. Add\t 2. Remove\t 3. Back")
        choice = input()
        if choice == "1":
            command = "imunify360-agent blacklist country add"
            country = input("Country can add: ")
            args = "--comment"
            comment = input("Noi dung comment: ")
            subprocess.call([command, country, args, comment])
        elif choice == "2":
            command = "imunify360-agent blacklist country remove"
            country = input("Country can remove: ")
            subprocess.call([command, country])
        elif choice == "3":
            config_imunify()
    elif reply == "5":
        system("clear")
        main()
def mysql():
    print("Please enter your choice:\n 1. Backup\t 2. Restore\t 3. Create Database\t 4. Create User\n 5. Grant Privilege\t 6. Change password user mysql\t 7. Drop database\t 8. Show user & databases\t 9.Back")
    choice = input()
    if choice == "1":
        user = input("User database: ")
        password = getpass.getpass("Password database: ")
        dbname = input("Database name: ")
        print("Backing up database" + " " + dbname + " " + "..." )
        system("mysqldump -u" + user + " " + "-p" + password + " " + dbname + ">" + dbname + ".sql")
        print("Backup database" + " " + dbname + " " + "completed")
    elif choice == "2":
        user = input("User database: ")
        password = getpass.getpass("Password database: ")
        dbname = input("Database name: ")
        path = input("Path storage backup file: ")
        print("Backing up database" + " " + dbname + " " + "..." )
        command = system("mysql -u" + user + " " + "-p" + password + " " + dbname + "<" + path + "/" + dbname + ".sql")
        if command == "":
            print("Backup database" + " " + dbname + " " + "completed")
        else:
            print("Backup Failed !!!")
    elif choice == "3":
        database_name = input("Database name: ")
        password = getpass.getpass("Root password database: ")
        args = "-Ne"
        command = "create database"
        system("mysql -uroot -p" + password + " " + args + " " + "\"" + command + " " + database_name + ";" + "\"")
        print("Database" + " " + database_name + " " + "create success !!!")
    elif choice == "4":
        user_name = input("User name: ")
        user_pass = getpass.getpass("User password: ")
        args = "-Ne"
        command = "create user"
        host = "localhost"
        password = getpass.getpass("Root password database: ")
        system("mysql -uroot -p" + password + " " + args + " " + "\"" + command + "\'" + user_name + "\'" + "@" + "\'" + host + "\'" + "IDENTIFIED BY" + " " + "\'" + user_pass + "\'" + ";" + "\"")
        print("User" + " " + user_name + " " + "create success")
    elif choice == "5":
        database_name = input("Database name: ")
        user_name = input("User name: ")
        password = getpass.getpass("Root password database: ")
        args = "-Ne"
        host = "localhost"
        command = "grant all privileges on"
        system("mysql -uroot -p" + password + " " + args + " " + "\"" + command + " " + database_name + ".* TO" + " " + "\'" + user_name + "\'" + "@" + "\'" + host + "\'" + ";" + "\"")
        print("Grant privileges success !!!")
    elif choice == "6":
        user = input("Username: ")
        root_password = getpass.getpass("Root password database: ")
        new_password = getpass.getpass("New password for user" + " "+ user + ":")
        args = "-Ne"
        command = "UPDATE mysql.user SET Password=PASSWORD"
        system("mysql -uroot -p" + root_password + " " + args + " " + "\"" + command + "('" + new_password + "')" + "WHERE User=" + "\'" + user + "'" + ";" + "\"")
        print("Change password for user" + " " + user + " " + "completed, new password is: " + new_password)
    elif choice == "7" :
        user_name = input("Please enter user database: ")
        database_name = input("Please enter database name: ")
        password = getpass.getpass("Please enter password: ")
        args = "-Ne"
        command = "drop database"
        system("mysql -u" + user_name + " " + "-p" + password + " " + args + "\"" + command + " " + database_name + "\"")
    elif choice == "8":
        print("Please enter your choice:\n 1. List databases\t 2. List user database\t 3. Back")
        reply = input()
        if reply == "1":
            password = getpass.getpass("Please enter password root: ")
            command = "show databases;"
            args = "-Ne"
            system("mysql -uroot -p" + password + " " + args + " " + "\"" + command + "\"")
            mysql()
        elif reply == "2":
            password = getpass.getpass("Please enter password root: ")
            command = "select user from mysql.user;"
            args = "-Ne"
            system("mysql -uroot -p" + password + " " + args + " " + "\"" + command + "\"")
            mysql()
        elif reply == "3":
            mysql()
    elif choice == "9":
        main()
    else:
        print("Please enter your choice again !!!")
        mysql()

def main():
    start()
if __name__ == "__main__":
    main()
main()
