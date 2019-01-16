import requests
import time
from postcodes import postcodes

counter = 0

base_url = 'https://www.deltaglasvezel.nl/app/actiecode/checkadres.web'

for postcode in postcodes:
    for huisnummer in range(int(postcode[1]), int(postcode[2]), 1):
        endpoint = '?zipcode={}&housenumber={}'.format('9999AA', '1')
        url = base_url + endpoint
        r = requests.post(url)
        if r.text[-35:-6] == 'maximaalaantalpogingenbereikt':
            print('IP geblokkeerd, 10 minuten pauze')
            time.sleep(1800)
        else:
            endpoint = '?zipcode={}&housenumber={}'.format(postcode[0], str(huisnummer))
            url = base_url + endpoint
            r = requests.post(url)
            if r.text[-34:-6] == 'bestellingbijandereaanbieder':
                counter += 1
                print('Glasvezel bij een andere aanbieder: ' + postcode[0] + ' met huisnummer ' + str(huisnummer) + 'totaal :' + counter)
            elif r.text[-5:-1] == 'null':
                counter += 1
                print('Glasvezel bij Delta ' + postcode[0] + ' met huisnummer ' + str(huisnummer) + 'totaal :' + counter)

