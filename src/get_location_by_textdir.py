import googlemaps


import csv
import json
import os

def FindLatLonByDirtext(response_route):

    script_path = os.path.dirname(os.path.realpath(__file__))

    KEY = 'AIzaSyBnvTEYfjQ8IA59AW_wZ26nJ_Joa_B7m-E'
    gmaps = googlemaps.Client(key=KEY)

    geojson = {
        'type': 'FeatureCollection',
        'features': []
    }
    report_noloc = ''
    results = 0
    total = 0

    with open(os.path.join(script_path,"csv_in.csv"), encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',', quotechar='\'')
        next(csv_data) # skip header

        for row in csv_data:
            city = 'Cali'
            country = 'CO'
            direction = str(row[1]) +', '+ city + ', ' + country
            geodir = gmaps.geocode(direction)
            total += 1
            getDirection = True
            if geodir:
                # print('{},{},{},{},{}'.format(int(row[0]), row[1], row[2], geodir.latlng[1], geodir.latlng[0]))
                
                address_components = geodir[0]['address_components']
                for x in range(0, len(address_components)):
                    if address_components[x]['types'][0] == "administrative_area_level_2":
                        if address_components[x]['long_name'] != city:
                            getDirection = False
                    elif address_components[x]['types'][0] == "country":
                        if address_components[x]['short_name'] != country:
                            getDirection = False

                if getDirection == True:
                    print(direction)
                    geojson['features'].append({
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [geodir[0]['geometry']['location']],
                        },
                        "properties": {
                            "id": row[0],
                            "direccion": row[1],
                            "tipo": row[2],
                        }
                    })
                    results += 1
                        
                else:
                    # print('{},{},{},0,0'.format(int(row[0]), row[1], row[2]))
                    report_noloc += '{},{},{}\n'.format(int(row[0]), row[1], row[2])

            else:
                print('{},{},{},0,0'.format(int(row[0]), row[1], row[2]))
                report_noloc += '{},{},{}\n'.format(int(row[0]), row[1], row[2])
                
        print('Number of matches {}/{}'.format(results, total))

            
    with open('geo_results.geojson', 'w') as geofile:
        geofile.write(json.dumps(geojson, indent=2))

    with open('report.txt', 'w') as report_file:
        report_file.write('Number of matches {}/{}\n\n'.format(results, total))
        report_file.write(report_noloc)

    return geojson