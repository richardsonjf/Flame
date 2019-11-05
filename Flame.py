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
		emails = open(sys.argv[1]+"/EX_EMAILS.txt","a")
		data = fileReader(self.file)
		ex_emails= list(set(re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', data)))

		for email in ex_emails:
                        if len(email) < 2:
                                pass
                        else:
                                emails.write(email.strip()+"\n")

	def urlsEX(self):
		urls = open(sys.argv[1]+"/URLS.txt","a")
		data = fileReader(self.file)
#                ex_urls = list(set(re.findall(r'(?:|api?|www?|http?|https?|ftp):\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+', data)))
                ex_urls = list(set(re.findall(r'(?:(\/\S+))*', data)))

		for url in ex_urls:
			if len(url) < 2:
				pass
			else:
				urls.write(url.strip()+"\n")

	def ipsEX(self):
		ips = open(sys.argv[1]+"/IPS.txt","a")
		data = fileReader(self.file)
                ex_ips = list(set(re.findall(r'|(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', data)))

		for ip in ex_ips:
			ips.write(ip.strip()+"\n")

	def domainsEX(self):
		ips = open(sys.argv[1]+"/DOMAINS.txt","a")
		data = fileReader(self.file)
                ex_ips = list(set(re.findall(r'(?:(?:[A-Z0-9][A-Z0-9-]{0,61}[A-Z0-9]\.)+)', data)))

		for ip in ex_ips:
			ips.write(ip.strip()+"\n")

	def queryEX(self):
		ips = open(sys.argv[1]+"/QUERIES.txt","a")
		data = fileReader(self.file)
                ex_ips = list(set(re.findall(r'(?:(\/\S+)*)', data)))

		for ip in ex_ips:
			ips.write(ip.strip()+"\n")

	def portEX(self):
		ips = open(sys.argv[1]+"/PORTS.txt","a")
		data = fileReader(self.file)
                ex_ips = list(set(re.findall(r'(?:(\/\S+)*)', data)))

		for ip in ex_ips:
			ips.write(ip.strip()+"\n")

	def schemeEX(self):
		ips = open(sys.argv[1]+"/PORTS.txt","a")
		data = fileReader(self.file)
                ex_ips = list(set(re.findall(r'(?:(https?|s?ftp):\/\/)?', data)))

		for ip in ex_ips:
			ips.write(ip.strip()+"\n")


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
		EX.urlsEX()
		EX.emailEX()
		EX.ipsEX()
		EX.schemeEX()
		EX.domainsEX()
		EX.queryEX()
		EX.portEX()
EX.interes_files()