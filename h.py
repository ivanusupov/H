import dns.resolver,dns.reversename
from termcolor import colored
import sys

if (len(sys.argv)>1):
    D = str(sys.argv[1])
else:
    print(colored('Usage: '+sys.argv[0]+" doman.name",'red'))
    sys.exit(-1)


print(colored('IPv4:\n', 'green'))
myResolver = dns.resolver.Resolver()

try:
    myAnswers = myResolver.resolve(D, "A")
    for rdata in myAnswers:
        try:
            ip=str(rdata)
            n = dns.reversename.from_address(ip)
            ptrs=dns.resolver.resolve(n,"PTR")
            for num in ptrs:
                print("A:\t"+D+" -> "+str(rdata)+" -> "+str(num))
        except:
            print("A:\t"+D+" -> "+str(rdata)+" -> "+colored('? ? ?','red'))
except:
    print("A:\t"+D+" -> "+colored('? ? ?','red'))
print("")

try:
    myAnswers = myResolver.resolve(D, "MX")
    for rdata in myAnswers:
        try:
            myAnswersA = myResolver.resolve(rdata.exchange, "A")
            for ips in myAnswersA:
                ip=str(ips)
                try:
                    n = dns.reversename.from_address(ip)
                    ptrs=dns.resolver.resolve(n,"PTR")
                    for num in ptrs:
                        print("MX: "+str(rdata.preference)+"\t"+str(rdata.exchange)+" -> "+str(ips)+" -> "+str(num))
                except:
                    print("MX: "+str(rdata.preference)+"\t"+str(rdata.exchange)+" -> "+str(ips)+" -> "+colored('? ? ?','red'))
        except:
            print("MX: "+str(rdata.preference)+"\t"+str(rdata.exchange)+" -> "+colored('? ? ?','red'))
except:
    print("MX: "+colored('? ? ?','red'))
print("")


try:
    myAnswers = myResolver.resolve(D, "NS")
    for rdata in myAnswers:
        try:
            myAnswersA = myResolver.resolve(str(rdata), "A")
            for ips in myAnswersA:
                ip=str(ips)
                try:
                    n = dns.reversename.from_address(ip)
                    ptrs=dns.resolver.resolve(n,"PTR")
                    for num in ptrs:
                        print("NS: "+str(rdata)+" -> "+str(ips)+" -> "+str(num))
                except:
                    print("NS: "+str(rdata)+" -> "+str(ips)+" -> "+colored('? ? ?','red'))
        except:
            print("NS: "+str(rdata)+" -> "+colored('? ? ?','red'))
except:
    print("NS: "+colored('? ? ?','red'))
print("\n")

print(colored('IPv6:\n', 'green'))
try:
    myAnswers = myResolver.resolve(D, "AAAA")
    for rdata in myAnswers:
        ip=str(rdata)
        n = dns.reversename.from_address(ip)
        try:
            ptrs=dns.resolver.resolve(n,"PTR")
            for num in ptrs:
                print("AAAA:\t"+D+" -> "+str(rdata)+" -> "+str(num))
        except:
            print("AAAA:\t"+D+" -> "+str(rdata)+" -> " + colored('? ? ?', 'red'))
except:
    print("AAAA:\t"+D+" -> "+colored('? ? ?','red'))
print("")

try:
    myAnswers = myResolver.resolve(D, "MX")
    for rdata in myAnswers:
        try:
            myAnswersA = myResolver.resolve(rdata.exchange, "AAAA")
            for ips in myAnswersA:
                ip=str(ips)
                try:
                    n = dns.reversename.from_address(ip)
                    ptrs=dns.resolver.resolve(n,"PTR")
                    for num in ptrs:
                        print("MX: "+str(rdata.preference)+"\t"+str(rdata.exchange)+" -> "+str(ips)+" -> "+str(num))
                except:
                    print("MX: "+str(rdata.preference)+"\t"+str(rdata.exchange)+" -> "+str(ips)+" -> "+colored('? ? ?','red'))
        except:
            print("MX: "+str(rdata.preference)+"\t"+str(rdata.exchange)+" -> "+colored('? ? ?','red'))
except:
    print("MX: "+colored('? ? ?','red'))
print("")


try:
    myAnswers = myResolver.resolve(D, "NS")
    for rdata in myAnswers:
        try:
            myAnswersA = myResolver.resolve(str(rdata), "AAAA")
            for ips in myAnswersA:
                ip=str(ips)
                try:
                    n = dns.reversename.from_address(ip)
                    ptrs=dns.resolver.resolve(n,"PTR")
                    for num in ptrs:
                        print("NS: "+str(rdata)+" -> "+str(ips)+" -> "+str(num))
                except:
                    print("NS: "+str(rdata)+" -> "+str(ips)+" -> "+colored('? ? ?','red'))
        except:
            print("NS: "+str(rdata)+" -> "+colored('? ? ?','red'))
except:
    print("NS: "+colored('? ? ?','red'))
print("")

print(colored('Other:\n', 'green'))

try:
    myAnswers = myResolver.resolve(D, "TXT")
    for rdata in myAnswers:
        print("TXT:\t"+str(rdata))
except:
    print("TXT:\t"+colored('? ? ?','red'))
print("")

try:
    myAnswers = myResolver.resolve(D, "SOA")
    for rdata in myAnswers:
        print("SOA:\t"+str(rdata))
except:
    print("SOA:\t"+colored('? ? ?','red'))
print("")
