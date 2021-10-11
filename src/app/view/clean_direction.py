import googlemaps
from models.directions_model import DirectionsModel
from models.deta_file import DetaFile

from db import db
import csv
import json
import os

def FindLatLonByDirtext(id_file):

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

    data_file = DetaFile.query.filter_by(id_file=id_file).all()
    data_file_json = [e.serialize() for e in data_file]
    print(data_file_json)
    for row in data_file_json:
        print(row['address'])
        city = 'Cali'
        country = 'CO'
        direction = str(row['address']) +', '+ city + ', ' + country
        geodir = gmaps.geocode(direction)
        total += 1
        getDirection = True
        if geodir:
            # print('{},{},{},{},{}'.format(int(row[0]), row[1], row[2], geodir.latlng[1], geodir.latlng[0]))
            point = 'SRID=4326;POINT(' + str(geodir[0]['geometry']['location']['lng']) + ' ' + str(geodir[0]['geometry']['location']['lat']) + ')'
            direction = DirectionsModel(row['address'], None, point, city, country)
            db.session.add(direction)
            db.session.commit()
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
                        "id": row['id_file'],
                        "direccion": row['address'],
                        "driver": row['driver'],
                    }
                })
                results += 1
                    
            else:
                # print('{},{},{},0,0'.format(int(row[0]), row[1], row[2]))
                report_noloc += '{},{},{}\n'.format(int(row[0]), row[1], row[2])

        else:
            print('{},{},{},0,0'.format(int(row[0]), row[1], row[2]))
            report_noloc += '{},{},{}\n'.format(int(row[0]), row[1], row[2])
                
    #     print('Number of matches {}/{}'.format(results, total))

            
    # with open('geo_results.geojson', 'w') as geofile:
    #     geofile.write(json.dumps(geojson, indent=2))

    # with open('report.txt', 'w') as report_file:
    #     report_file.write('Number of matches {}/{}\n\n'.format(results, total))
    #     report_file.write(report_noloc)

    return geojson