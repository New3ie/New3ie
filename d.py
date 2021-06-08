# forlap nim-comod
# coder : oncom
from re import findall as fa
import requests as req
from urllib3.exceptions import InsecureRequestWarning
from time import sleep
from bs4 import BeautifulSoup as bs

req.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

for h in 'Assalamualaikum':
    print('\33[92m'+h, end='', flush=True)
    sleep(0.01)


def nim(ul):
    d = []
    raw = bs(req.get(ul, verify=False).text, 'html.parser').find('table').findAll('tr')
    for i in range(len(raw)):
        data = raw[i].findAll('td')
        try:
            d.append(data[1].text+' '+data[2].text)
        except Exception as e:
            pass
    for x in d:
        y = x.split()
        n = y[0]+':'+y[0]
#        print(n)
        try:
            for i in range(1, len(y)):
                if len(y[i]) > 2:
                    if ',' in y[i]:
                        y[i] = y[i].split(',')[0]
                        print(y[0]+':'+y[i].lower()+'123')
                        nl = y[0]+':'+y[i].lower()+'123'
                        with open('nim.txt', 'a') as f:
                            f.write(nl+'\n')
                        f.close()
                    if '.' in y[i]:
                        y[i] = y[i].split('.')[0]
                        print(y[0]+':'+y[i].lower()+'123')
                        nl = y[0]+':'+y[i].lower()+'123'
                        with open('nim.txt', 'a') as f:
                            f.write(nl+'\n')
                        f.close()

                    else:
                        nl = y[0]+':'+y[i].lower()+'123'
                        print(nl)
                        with open('nim.txt', 'a') as f:
                            f.write(nl+'\n')
                        f.close()
       

        except Exception as e:
            print(e)
#        with open('nim.txt', 'a') as f:
#            f.write(n+'\n')
#        f.close()


def main():
    try:
        n = []
        u = []
        js = []
        c = 0
        url = input('\n\33[mUrl prodi: ')
        r = req.get(url, verify=False).text
        pola = 'https://forlap.kemdikbud.go.id/mahasiswa/detai.*'
        lnk = fa(pola, r)
        for l in lnk:
            c += 1
            ln = l.split('"')[0]
            thn = ln.split('/')[6]
            jml = l.split('>')[1]
            j = jml.split('<')[0]
            js.append(j)
            print(str(c)+'. '+thn+' Jml='+j)
            u.append(ln)
            n.append(str(c))
        d = dict(zip(n, u))
        while True:
            z = input('\npilihan:\33[95m ')
            jn = 0
            x = 0
            url = d[z] + '/'
            while x <= int(js[int(z)-1]):
                print('\33[m\n'+url)
                print('\33[92m'+z+'\33[m')
                ul = url
                nim(ul)
                if True:
                    x += 20
                    url = d[z] +'/'
                    url += str(x)
                else:
                    break

    except EOFError:
        exit('\33[m')
    except KeyError:
        nns()
    except req.exceptions.RequestException:
        exit('\n\33[93mJaringan?\33[m')
    except KeyboardInterrupt:
        exit('\33[m')


def nns():
    try:
        with open('nim.txt', 'r') as f:
            x = f.readlines()
            z = str(len(x))+' line'
        with open('nim.txt', 'w') as f:
            y = set(x)
            for i in y:
                f.write(i)

        print('\nMengkompres nim yg sama...\n\33[m'+z+' > '+str(len(y))+' line')
        f.close()
    except KeyboardInterrupt:
        exit()
    except FileNotFoundError:
        exit('nim.txt not found')


if __name__ == '__main__':
    main()
