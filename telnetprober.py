import telnetlib
import logging
import socket
import time
host = "localhost"
port = 694


#tn = telnetlib.Telnet(host,port, timeout=1)
try:
#if tn:
    tn = telnetlib.Telnet(host,port, timeout=1)
    logging.basicConfig(filename='callbackProber.log', filemode='a+', level=logging.INFO)
    logging.info('Connected')


    #f = open("callbackProber.log", "a+")
    #f.write("Connected\n")
    #f.close()
    #tn.close()


except:


#else:

    # with open("callbackProber.log",w+) as f:
    # f.write("connection timeout, retrying in 1 sec")
    logging.basicConfig(filename='callbackProber.log', filemode='a+', level=logging.INFO)
    logging.info('Retrying')

    tn = telnetlib.Telnet(host, port, timeout=1)
    tn.close()


    #f = open("callbackProber.log", "a+")
    #f.write("connection timeout\n")
    #f.close()
    # time.sleep(2)
