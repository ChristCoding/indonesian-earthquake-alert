from bs4 import BeautifulSoup
import requests


def getdata() :
    try :
        content = requests.get ( 'https://www.bmkg.go.id/' )
    except :
        return None
    if content.status_code == 200 :
        soup = BeautifulSoup ( content.text , 'html.parser' )
        data=soup.find('div','col-md-6 col-xs-6 gempabumi-detail no-padding')
        alldate=data.find('span',{'class':'waktu'}).text.split(', ')
        datali=data.findAll('li')
        coord=datali[3].text.split(' - ')
        hasil = dict ( )
        hasil [ 'date' ] = alldate[0]
        hasil [ 'time' ] = alldate[1]
        hasil [ 'magnitude' ] = datali[1].text
        hasil [ 'depth' ] = datali[2].text
        hasil [ 'location' ] ={ 'ls' : coord[0].split(' ')[0] , 'bt' : coord[1].split(' ')[0] }
        hasil [ 'center' ] = datali[4].text
        hasil [ 'impact scale' ] = datali[5].text.split(': ')[1]
        return hasil


"""
08 Juni 2022, 21:25:20 WIB
2.5
10 km
3.26 LS - 128.34 BT
Pusat gempa berada di darat 9 km utara Kairatu
Dirasakan (Skala MMI): II Kairatu
"""


def displaydata(result) :
    if result == None :
        print ( 'url not found' )
    else:
        print (f'Latest Earthquake News in Indonesia' )

