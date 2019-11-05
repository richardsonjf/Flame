import os,sys
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
	f = open(file,"rb").read()
	return f

def Lister(path):
	for fpath, dirs,files in os.walk(path):
	  	for file in files:
        		if extension in file:
            			sourcesList.append(os.path.join(fpath, file))

Lister(path)

print "[+] Sources list successfully generated !"

class Extractor:
	def __init__(self,file):
		self.file = file

	def emailEX(self):
		emails = open(sys.argv[1]+"/emails.txt","a")
		data = fileReader(self.file)
		ex_emails= list(set(re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', data)))

		for email in ex_emails:
                        if len(email) < 2:
                                pass
                        else:
                                emails.write(email.strip()+"\n")

	def urlsEX(self):
		urls = open(sys.argv[1]+"/urls.txt","a")
		data = fileReader(self.file)
                ex_urls = list(set(re.findall(r'(?:www?|http?|https?|ftp):\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+', data)))

		for url in ex_urls:
			if len(url) < 2:
				pass
			else:
				urls.write(url.strip()+"\n")

	def ipsEX(self):
		ips = open(sys.argv[1]+"/ip.txt","a")
		data = fileReader(self.file)
                ex_ips = list(set(re.findall(r'(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', data)))

		for ip in ex_ips:
			ips.write(ip.strip()+"\n")

	def domainsEX(self):
		domains = open(sys.argv[1]+"/domains.txt","a")
		data = fileReader(self.file)
                ex_domains = list(set(re.findall(r'(?:(?:[A-Z0-9][A-Z0-9-]{0,61}[A-Z0-9]\.)+)', data)))

		for domain in ex_domains:
			domains.write(domain.strip()+"\n")

	def queriesEX(self):
		queries = open(sys.argv[1]+"/query.txt","a")
		data = fileReader(self.file)
                ex_queries = list(set(re.findall(r'(?:(\/\S+)*)', data)))

		for query in ex_queries:
			queries.write(query.strip()+"\n")

	def portsEX(self):
		ports = open(sys.argv[1]+"/ports.txt","a")
		data = fileReader(self.file)
                ex_ports = list(set(re.findall(r'(?::(\d{1,5}))?', data)))

		for port in ex_ports:
			ports.write(port.strip()+"\n")

	def sachaEX(self):
		sacha = open(sys.argv[1]+"/scheme.txt","a")
		data = fileReader(self.file)
                ex_sacha = list(set(re.findall(r'(?:(www?|https?|s?ftp):\/\/)?', data)))

		for sach in ex_sacha:
			sacha.write(sach.strip()+"\n")


	def interes_files(self):
		int_files = open(sys.argv[1]+"/DATA.txt","a")
		words = ['base_url',"ftp_","db_","user","pass","user_pass","user_name","smtp_","passwd","mysql://","ftp://"]
		data = fileReader(self.file)
		for word in words:
			if word.upper() in data or word.lower() in data:
				 int_files.write("{} \t: {}\n".format(word,self.file))


if __name__ == '__main__':
	for sl in sourcesList:
		EX = Extractor(sl)
		EX.emailEX()
		EX.urlsEX()
		EX.ipsEX()
		EX.domainsEX()
		EX.queriesEX()
		EX.portsEX()
		EX.sachaEX()
EX.interes_files()
