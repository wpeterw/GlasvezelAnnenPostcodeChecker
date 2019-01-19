import requests
import sys
import time
from datetime import datetime
from postcodes import postcodes

counter = 0

base_url = 'https://www.deltaglasvezel.nl/app/actiecode/checkadres.web'
sleep = 1800

for postcode in postcodes:
    for huisnummer in range(int(postcode[1]), int(postcode[2]), 2):
        f = open('glasvezel.txt', 'w')
        endpoint = '?zipcode={}&housenumber={}'.format('9999AA', '1')
        url = base_url + endpoint
        r = requests.post(url)
        if r.text[-35:-6] == 'maximaalaantalpogingenbereikt':
            line = 'IP geblokkeerd, {} minuten pauze'.format(int(sleep/60))
            print('{} - {}'.format(datetime.now(), line))
            f.write('{} - {}'.format(datetime.now(), line))
            f.close()
            for i in range(sleep, 0, -60):
                sys.stdout.write(str(int(i/60)) + '  ')
                sys.stdout.flush()
                time.sleep(60)
        else:
            endpoint = '?zipcode={}&housenumber={}'.format(postcode[0], str(huisnummer))
            url = base_url + endpoint
            r = requests.post(url)
            print(r.text)
            if r.text[-34:-6] == 'bestellingbijandereaanbieder':
                counter += 1
                print('{} - {}, {}, {}, Caiway'.format(datetime.now(), str(counter), postcode[0], str(huisnummer) + '\n'))
                f.write('{} - {}, {}, {}, Delta'.format(datetime.now(), str(counter), postcode[0], str(huisnummer)))
            elif r.text[-34:-6] == 'kanordernietwijzigenviaadres':
                counter += 1
                print('{} - {}, {}, {}, Delta'.format(datetime.now(), str(counter), postcode[0], str(huisnummer) + '\n'))
                f.write('{} - {}, {}, {}, Delta'.format(datetime.now(), str(counter), postcode[0], str(huisnummer)))
            f.close()
f.close()
