#!/usr/bin/python3
import requests
import sys
def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

f = open(sys.argv[1], "r")
try:
    for sub in f:
        sub="https://" + sub.split("://")[-1].rstrip("\n")
        test1="" + sub.split(".")[-2]
        evil="https://evil"+test1+".com"

        try:
            #print('\x1b[1;30;40m[-] ' + sub)
            x = requests.head(sub,headers=origin,timeout=(5,5))
            header=x.headers
            code=x.status_code
            print('[-] ' + sub+' -- ',code)
            with open(test1+".txt", "a") as f:
                f.writelines("%s\n" %sub)
                f.close()
            withocde=sub +' -- ' + str(code)
            with open(test1+"_code.txt", "a") as f:
                f.writelines("%s\n" %withocde)
                f.close()
            c1="Access-Control-Allow-Credentials".casefold()
            c2="Access-Control-Allow-Origin".casefold()
            check1="true".casefold()
            check2="*"
            x1=0
            x2=0
            x3=0
            for k,v in header.items():
                k1=k.casefold()
                v1=v.casefold()
                if c1 in k1:
                    if v1==check1:
                        x1=1
                elif c2 in k1:
                    if v1==check2:
                        x2=1
                    elif v1 == evil:
                        x3=1
            if x1==1 and x2 ==1:
                print('\x1b[1;35;40m[+]'+'[+] '+sub+ '\33[5m ------> '+'\33[0m',x.status_code,'\x1b[1;32;40m'+'[Vuln]'+ '\33[0m')
                print('\x1b[1;32;40m' + 'Access-Control-Allow-Credentials ', '\x1b[1;31;40m'+'True'+ '\33[0m')
                print('\x1b[1;32;40m' + "Access-Control-Allow-Origin: ", '\x1b[1;31;40m'+'*' + '\33[0m')
                with open(test1+"-output.txt", "a") as f:
                    print(sub, file=f)
                    lines_seen = set()
                    for line in open(test1+"-output.txt", "r"):
                        if line not in lines_seen: # not a duplicate
                            f.write(line)
                            lines_seen.add(line)
                    f.close()
            elif x1==1 and x3==1:
                print('\x1b[1;35;40m[+]'+'[+] '+sub+ '\33[5m ------> '+'\33[0m',x.status_code,'\x1b[1;32;40m'+'[Vuln]'+ '\33[0m')
                print('\x1b[1;32;40m' + 'Access-Control-Allow-Credentials ', '\x1b[1;31;40m'+'True'+ '\33[0m')
                print('\x1b[1;32;40m' + "Access-Control-Allow-Origin: ", '\x1b[1;31;40m'+evil + '\33[0m' )
                with open(test1+"-output.txt", "a") as f:
                    print(sub, file=f)
                    lines_seen = set()
                    for line in open(test1+"-output.txt", "r"):
                        if line not in lines_seen: # not a duplicate
                            f.write(line)
                            lines_seen.add(line)
                    f.close()


        except:
            print('[-] '+strike(sub)+' [x_x] ')

except:
    print('----------------------')