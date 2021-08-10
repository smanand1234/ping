import argparse
import asyncio
import ipaddress
import aioping

async def myping(ipaddr, timeout):
      print("Pinging {}, timeout {}sec",ipaddr, timeout)
      aioping(ipaddr, timeout)

async def main:
       parser = argparse.ArgumentParser()
       parser.add_argument("ipaddr", type=str, help="IP address to scan in network/prefix format")
       parser.add_argument("--concurrent", type=int, help="Number of concurrent pings")
       parser.add_argument("--timeout", type=int, help="Ping timeout value in seconds")
       args = parser.parse_args()
       #Get list of all possible IP addresses within the network
       addrlist = list(ip_network(arg.ipaddr))
       #Default concurrent task = 1
       concurrent = 1
       #Default timeout is 5 seconds
       timeout = 5
       if args.concurrent > 1:
            concurrent = args.concurrent
       #Allow timeout down to 1 second
       if args.timeout >= 1:
            timeout = args.timeout
       #Get the number of available io addresses to ping
       numip = len(addrlist)
       i = 0

       while i < numip:
            j = 0
            while i < numip and j < concurrent:
                   await myping(addrlist[i], timeout)
                   i++
                   j++  
            
       
