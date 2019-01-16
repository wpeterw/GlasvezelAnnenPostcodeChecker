import requests
import time
from postcodes import postcodes

counter = 0
base_url = 'https://www.buitengewoonglasvezel.nl/app/actiecode/checkadres.web'

for postcode in postcodes:
    for huisnummer in range(int(postcode[1]), int(postcode[2]), 1):
        endpoint = '?zipcode={}&housenumber={}'.format('9999AA', '1')
        url = base_url + endpoint
        r = requests.post(url)
        if r.text[44:73] == 'maximaalaantalpogingenbereikt':
            print('IP geblokkeerd, 10 minuten pauze')
            time.sleep(600)
        else:
            endpoint = '?zipcode={}&housenumber={}'.format(postcode[0], str(huisnummer))
            url = base_url + endpoint
            r = requests.post(url)
            if r.text[44:72] == 'kanordernietwijzigenviaadres':
                counter += 1
                print('Caiway aansluiting op ' + postcode[0] + ' met huisnummer ' + str(huisnummer))
