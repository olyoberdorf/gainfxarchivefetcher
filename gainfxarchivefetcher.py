
import ConfigParser
import os
import requests

years = ['2015','2016',]
months = ['01 January', '02 February', '03 March', '04 April', '05 May', \
        '06 June', '07 July', '08 August', '09 September', '10 October', \
        '11 November', '12 December']
weeks = ['Week1', 'Week2', 'Week3', 'Week4', 'Week5',]
pairs = ['USD/JPY',]

base_path = '/home/oly/GainFXCache/'
host = 'http://ratedta.gaincaptial.com'

cp = ConfigParser.ConfigParser()
cp.read('gainfxarchivefetcher.ini')
years = cp.get('GainFXArchiveFetcher', 'years').split(',')
pairs = cp.get('GainFXArchiveFetcher', 'pairs').split(',')
base_path = cp.get('GainFXArchiveFetcher', 'basepath')
host = cp.get('GainFXArchiveFetcher', 'host')

print years
print pairs
print base_path
print host

for year in years:
    for month in months:
        path = "%s/%s/%s/" % (base_path, year, month)
        for pair in pairs:
            pair = pair.replace('/','_')
            for week in weeks:
                filename = "%s_%s.zip" % (pair, week)
                filepath = "%s/%s/%s/%s" % (base_path, year, month, filename)
                url = "%s/%s/%s/%s" % (host, year, month, filename)
                print "fetching url: %s" % url
                r = requests.get(url)
                if r.status_code == 200:
                    d = os.path.dirname(path)
                    if not os.path.exists(d):
                        os.makedirs(d)
                    with open(filepath, "wb") as csvzipfile:
                        csvzipfile.write(r.content)
