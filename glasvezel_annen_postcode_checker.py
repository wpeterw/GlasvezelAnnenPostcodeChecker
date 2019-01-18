import requests
import time
from datetime import datetime
from postcodes import postcodes

counter = 0

base_url = 'https://www.deltaglasvezel.nl/app/actiecode/checkadres.web'
sleep = 1500

for postcode in postcodes:
    for huisnummer in range(int(postcode[1]), int(postcode[2]), 1):
        f = open('glasvezel.txt', 'w')
        endpoint = '?zipcode={}&housenumber={}'.format('9999AA', '1')
        url = base_url + endpoint
        r = requests.post(url)
        if r.text[-35:-6] == 'maximaalaantalpogingenbereikt':
            line = 'IP geblokkeerd, {} minuten pauze'.format(sleep/60)
            print('{} - {}'.format(datetime.now(), line))
            f.write('{} - {}'.format(datetime.now(), line))
            f.close()
            time.sleep(sleep)
        else:
            endpoint = '?zipcode={}&housenumber={}'.format(postcode[0], str(huisnummer))
            url = base_url + endpoint
            r = requests.post(url)
            if r.text[-34:-6] == 'bestellingbijandereaanbieder':
                counter += 1
                line = ('{} - {}, {}, {}, Caiway'.format(datetime.now(), str(counter), postcode[0], str(huisnummer)))
                f.write(line)
            elif r.text[-34:-6] == 'kanordernietwijzigenviaadres':
                counter += 1
                line = ('{} - {}, {}, {}, Delta'.format(datetime.now(), str(counter), postcode[0], str(huisnummer)))
                print(line)
                f.write(line)
            f.close()
f.close()
