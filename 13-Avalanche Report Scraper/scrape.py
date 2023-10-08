import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import mysql.connector

# Web sitesini iste
url = "https://static.avalanche.report/bulletins/archive/tyrol/caaml/"
response = requests.get(url)

if response.status_code == 200:
    # Web sayfasının içeriğini analiz et
    soup = BeautifulSoup(response.text, "html.parser")

    # XML dosyalarını içeren bağlantıları bul
    xml_links = [link.get("href") for link in soup.find_all("a") if link.get("href").endswith(".xml")]

    # Kaç tane XML dosyası olduğunu yazdır
    print(f"Toplam {len(xml_links)} XML dosyası bulunmaktadır.")

    if xml_links:
        # Veritabanı bağlantısını oluştur
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="Avalance",  # Veritabanı adınıza uygun olarak değiştirin
            auth_plugin="mysql_native_password"
        )

        cursor = connection.cursor()

        for xml_link in xml_links:
            # XML dosyasını indir
            xml_url = url + xml_link
            xml_response = requests.get(xml_url)

            if xml_response.status_code == 200:
                # XML verilerini işle
                xml_data = xml_response.text
                root = ET.fromstring(xml_data)

                # XML verilerini işleme ve saklama (örneğin, bir veri yapısında)
                for danger_rating in root.findall('.//caaml:DangerRating', namespaces={'caaml': 'http://caaml.org/Schemas/V5.0/Profiles/BulletinEAWS'}):
                    valid_time_elem = danger_rating.find('caaml:validTime/caaml:TimeInstant/caaml:timePosition', namespaces={'caaml': 'http://caaml.org/Schemas/V5.0/Profiles/BulletinEAWS'})
                    
                    if valid_time_elem is not None:
                        valid_time = valid_time_elem.text

                    else: 
                        valid_time = None

                    main_value_elem = danger_rating.find('caaml:mainValue', namespaces={'caaml': 'http://caaml.org/Schemas/V5.0/Profiles/BulletinEAWS'})
                    
                    if main_value_elem is not None:
                        main_value = main_value_elem.text

                    else: 
                        main_value = None

                    loc_ref_elem = danger_rating.find('caaml:locRef', namespaces={'caaml': 'http://caaml.org/Schemas/V5.0/Profiles/BulletinEAWS'})
                    if loc_ref_elem is not None:
                        loc_ref = loc_ref_elem.get('{http://www.w3.org/1999/xlink}href')
                    else:
                        loc_ref = None

                    valid_elevation_elem = danger_rating.find('caaml:validElevation/caaml:ElevationRange', namespaces={'caaml': 'http://caaml.org/Schemas/V5.0/Profiles/BulletinEAWS'})
                    
                    if valid_elevation_elem is not None:
                        valid_elevation = valid_elevation_elem.find('caaml:endPosition')

                        if valid_elevation is not None:
                            valid_elevation = valid_elevation.text
                        else:
                            valid_elevation = None

                    else: 
                        valid_elevation = None

                    # Veriyi veritabanına yazma (örneğin, 'your_table' ve sütun adlarınıza uygun olarak değiştirin)
                    sql = "INSERT INTO DangerRatings (valid_time, main_value, loc_ref, valid_elevation) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (valid_time, main_value, loc_ref, valid_elevation))
                    connection.commit()

        # Bağlantıyı kapat
        cursor.close()
        connection.close()
    else:
        print("XML dosyası bulunamadı.")
else:
    print("Web sitesine erişim başarısız oldu.")
