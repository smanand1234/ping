import argparse
import asyncio
import ipaddress
import aioping
async def myping(ipaddr, timeout,semaphore):
      await semaphore.acquire()
#      await asyncio.sleep(0)
      print("Pinging {}, timeout {}sec".format(ipaddr, timeout))
      aioping(ipaddr, timeout)
      semaphore.release()


async def main(loop):
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
       #Use semaphore to limit the number of concurrent tasks
       obj = asyncio.Semaphore(concurrent)
       i = 0
       i = i+1
       while i < numip:
           await asyncio.wait([myping(addrlist[i], timeout,obj)])
           i= i+1

loop=asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
