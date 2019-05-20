import pymysql.cursors
from openpyxl import load_workbook

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='deneme',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

try:
    wb = load_workbook('data/pk_list_06.05.2019.xlsx')
    ws = wb.active
	
    lower_map = { ord(u'I'): u'ı' }
    regions = {}
    for index, row in enumerate(ws.rows):
        if index == 0:
            continue

        index_str = str(index + 1)

        city = ws["A" + index_str].value
        district = ws["B" + index_str].value
        neighborhood = ws["C" + index_str].value
        part = ws["D" + index_str].value
        postal_code = ws["E" + index_str].value

        if city not in regions:
            regions[city] = {}

        if district not in regions[city]:
            regions[city][district] = {}

        if neighborhood not in regions[city][district]:
            regions[city][district][neighborhood] = {}

        regions[city][district][neighborhood][part] = postal_code

    for city in regions.keys():
        city_name = city.translate(lower_map).title().strip()

        with connection.cursor() as cursor:
            sql = "INSERT INTO `iller` (`il_adi`) VALUES (%s);"
            cursor.execute(sql, (city_name))
            connection.commit()
            city_id = cursor.lastrowid

            for district in regions[city].keys():
                district_name = district.translate(lower_map).title().strip()

                with connection.cursor() as cursor:
                    sql = "INSERT INTO `ilceler` (`il_id`, `ilce_adi`) VALUES (%s, %s);"
                    cursor.execute(sql, (city_id, district_name))
                    connection.commit()
                    district_id = cursor.lastrowid

                    for neighborhood in regions[city][district].keys():
                        neighborhood_name = neighborhood.translate(lower_map).title().strip()

                        with connection.cursor() as cursor:
                            sql = "INSERT INTO `semtler` (`ilce_id`, `semt_adi`) VALUES (%s, %s);"
                            cursor.execute(sql, (district_id, neighborhood_name))
                            connection.commit()
                            neighborhood_id = cursor.lastrowid

                            for part in regions[city][district][neighborhood].keys():
                                part_name = part.translate(lower_map).title().strip()

                                with connection.cursor() as cursor:
                                    sql = "INSERT INTO `mahalleler` (`semt_id`, `mahalle_adi`, `posta_kodu`) VALUES (%s, %s, %s);"
                                    cursor.execute(sql, (neighborhood_id, part_name, regions[city][district][neighborhood][part]))
                                    connection.commit()
                                    part_id = cursor.lastrowid
                                    postal_code = regions[city][district][neighborhood][part]

                                    print(city_name + ' / ' + district_name + ' / ' + neighborhood_name + ' / ' + part_name + ' - ' + str(postal_code))

finally:
    connection.close()
