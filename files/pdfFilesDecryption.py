#!/usr/bin/python3

# 1、使用pikepdf库暴力破解PDF文件。
import pikepdf
from tqdm import tqdm
# load password list
passwords = [ line.strip() for line in open("wordlist.txt") ]
# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF file 
        with pikepdf.open("Quectel_AG55xQ系列_QuecOpen_Linux系统时间同步_V1.0.pdf", password=password) as pdf:
            # Password decrypted successfully, break out of the loop 
            print("[+] Password found:", password) 
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop 
        continue




# 2、提取PDF密码哈希并使用John Ripper来破解它。
# 3、使用iSeePassword Dr.PDF程序破解PDF密码。
