import argparse
import asyncio
import ipaddress
import time
from threading import *
import aioping
async def myping(ipaddr, timeout,obj):
      await asyncio.sleep(0)
      print("Pinging {}, timeout {}sec".format(ipaddr, timeout))
      aioping(ipaddr, timeout)
      obj.release()


def main():
       parser = argparse.ArgumentParser()
       parser.add_argument("ipaddr", type=str, help="IP address to scan in network/prefix format")
       parser.add_argument("--concurrent", type=int, help="Number of concurrent pings")
       parser.add_argument("--timeout", type=int, help="Ping timeout value in seconds")
       args = parser.parse_args()
       #Get list of all possible IP addresses within the network
       addrlist = list(ipaddress.ip_network(args.ipaddr))
       #Default concurrent task = 1
       concurrent = 1
       #Default timeout is 5 seconds
       timeout = 5
       if int(args.concurrent) > 1:
            concurrent = int(args.concurrent)
       #Allow timeout down to 1 second
       if args.timeout >= 1:
            timeout = args.timeout
       #Get the number of available io addresses to ping
       numip = len(addrlist)
       obj = Semaphore(concurrent)
       i = 0
       while i < numip:
           obj.acquire()
           asyncio.run(myping(addrlist[i], timeout,obj))
           i= i+1


main()       
