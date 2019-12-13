#!/usr/bin/env python3
# encoding: utf-8

import os
import sys
import re


path = sys.argv[1]
tool = sys.argv[2]

if tool == "jadx":
    extension = ".java"
elif tool == "apktool":
    extension = ".smali"
else:
    sys.exit()

sourcesList = []


def fileReader(file):
    #    f = open('file', 'rb', encoding='utf-8').read()
    f = open(file, encoding='utf-8').read()
    return f


def Lister(path):
    for fpath, dirs, files in os.walk(path):
        for file in files:
            if extension in file:
                sourcesList.append(os.path.join(fpath, file))


Lister(path)

print ("[+] Decoded Successfully")


class Extractor:
    def __init__(self, file):
        self.file = file

    def emailEX(self):
        emails = open(sys.argv[1]+"/emails.txt", "a")
        data = fileReader(self.file)
        ex_emails = list(
            set(re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', data)))

        for email in ex_emails:
            if len(email) < 2:
                pass
            else:
                emails.write(email.strip()+"\n")

    def urlsEX(self):
        urls = open(sys.argv[1]+"/url.txt", "a")
        data = fileReader(self.file)
        ex_urls = list(set(re.findall(
            r'(?:http?|ftp|www|subdomain|domain|app|.):\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+', data)))

        for url in ex_urls:
            if len(url) < 2:
                pass
            else:
                urls.write(url.strip()+"\n")

    def ipsEX(self):
        ips = open(sys.argv[1]+"/ip_list.txt", "a")
        data = fileReader(self.file)
        ex_ips = list(set(re.findall(r'[0-9]+(?:\.[0-9]+){3}', data)))
        ex_ips += list(set(re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', data)))

        for ip in ex_ips:
                ips.write(ip.strip()+"\n")

    def portsEX(self):
        ports = open(sys.argv[1]+"/ports.txt", "a")
        data = fileReader(self.file)
        ex_ports = list(set(re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+[0-9]?', data)))

        for port in ex_ports:
            ports.write(port.strip()+"\n")


    def interes_files(self):
        int_files = open(sys.argv[1]+"/interestingdata.txt", "a")
        words = ['base_url', "google_api_key", "<domain","includeSubdomains","domain","</domain>","sub","google_crash_repoting_api_key","google_storage_bucket","facebook_api_key","facebook_api","SELECT","username FROM","execSQL","source","Source","Timestamp","timestgap","message","Message","mode","ftp","_db|/api","api","api","ssh","config","admin","php","db","dump","_db","passwd_","user","pass","user_pass","user_name","smtp_","passwd","_passwd","select","put","dit","add","gopher://","mysql://","ftp://,","source", "Source", "Timestamp", "timestgap", "message", "Message", "mode", "ftp", "_db", "\/api", "api\/", "api", "ssh", "config", "admin", "php", "db_", "dump", "_db_", "passwd_", "user", "pass", "user_pass", "user_name", "smtp_", "passwd", "_passwd", "select", "put", "edit", "add", "gopher://", "mysql://", "ftp://"]
        data = fileReader(self.file)
        for word in words:
            if word.upper() in data or word.lower() in data:
                int_files.write("{} \t: {}\n".format(word, self.file))


if __name__ == '__main__':
    for sl in sourcesList:
        EX = Extractor(sl)
        EX.emailEX()
        EX.urlsEX()
        EX.ipsEX()
        EX.portsEX()
EX.interes_files()
