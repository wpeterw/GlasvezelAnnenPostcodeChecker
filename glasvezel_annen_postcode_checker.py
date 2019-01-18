import requests
import time
from postcodes import postcodes

counter = 0

base_url = 'https://www.deltaglasvezel.nl/app/actiecode/checkadres.web'
f = open('glasvezel.txt', 'w')

for postcode in postcodes:
    for huisnummer in range(int(postcode[1]), int(postcode[2]), 1):
        endpoint = '?zipcode={}&housenumber={}'.format('9999AA', '1')
        url = base_url + endpoint
        r = requests.post(url)
        if r.text[-35:-6] == 'maximaalaantalpogingenbereikt':
            print('IP geblokkeerd, 15 minuten pauze')
            time.sleep(1800)
        else:
            endpoint = '?zipcode={}&housenumber={}'.format(postcode[0], str(huisnummer))
            url = base_url + endpoint
            r = requests.post(url)
            if r.text[-34:-6] == 'bestellingbijandereaanbieder':
                counter += 1
                print(postcode[0], str(huisnummer) + ',Caiway,' + str(counter))
                line = (postcode[0] + ',' + huisnummer, 'Caiway')
                f.write(str(line))
            elif r.text[-34:-6] == 'kanordernietwijzigenviaadres':
                counter += 1
                print(postcode[0], str(huisnummer) + ',Delta,' + str(counter))
                line = (postcode[0] + ',' + huisnummer, 'Delta')
                f.write(str(line))
