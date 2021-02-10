import psycopg2
global alldata
alldata =[]

def getdata (cursor):
    for r in [2010, 2011, 2012]:
        select_command_black = "SELECT black_spi_overall FROM data WHERE year={} ORDER BY facility_code;".format(r)
        cursor.execute(select_command_black)
        conn.commit()
        data_black = cursor.fetchall()
        d = 0
        for i in data_black:
            if i[0] != -999:
                d += i[0]
        data_black_average = d / (len(data_black)-len([i[0] for i in data_black if i[0] == -999]))
        alldata.append(data_black_average)
        
        select_command_hispanic = "SELECT hispanic_spi_overall FROM data WHERE year={} ORDER BY facility_code;".format(r)
        cursor.execute(select_command_hispanic)
        conn.commit()
        hispanic_data = cursor.fetchall()
        d = 0
        for i in hispanic_data:
            if i[0] != -999:
                d += i[0]
        data_hispanic_average = d / (len(hispanic_data) - len([i for i in hispanic_data if i[0] == -999]))
        alldata.append(data_hispanic_average)
        
        select_command_ell = "SELECT ell_spi_overall FROM data WHERE year={} ORDER BY facility_code;".format(r)
        cursor.execute(select_command_ell)
        conn.commit()
        ell_data = cursor.fetchall()
        d = 0
        for i in ell_data:
            if i[0] != -999:
                d += i[0]
        data_ell_average = d / (len(ell_data) - len([i for i in ell_data if i[0] == -999]))
        alldata.append(data_ell_average)
        
        select_command_frl = """SELECT frl_spi_overall FROM data WHERE year={} ORDER BY facility_code;""".format(r)
        cursor.execute(select_command_frl)
        conn.commit()
        frl_data = cursor.fetchall()
        d = 0
        for i in frl_data:
            if i[0] != -999:
                d += i[0]
        data_frl_average = d / (len(ell_data) - len([i for i in frl_data if i[0] == -999]))
        alldata.append(data_frl_average)
        
        select_command_swd = """SELECT swd_spi_overall FROM data WHERE year={} ORDER BY facility_code;""".format(r)
        cursor.execute(select_command_swd)
        conn.commit()
        swd_data = cursor.fetchall()
        d = 0
        for i in swd_data:
            if i[0] != -999:
              d += i[0]
        data_swd_average = d / (len(ell_data) - len([i for i in swd_data if i[0] == -999]))
        alldata.append(data_swd_average)

        select_command_highneeds = "SELECT high_needs_spi_overall FROM data WHERE year={} ORDER BY facility_code;".format(r)
        cursor.execute(select_command_highneeds)
        conn.commit()
        high_needs_data = cursor.fetchall()
        d = 0
        for i in high_needs_data:
            if i[0] != -999:
                d += i[0]
        data_frl_average = d / (len(ell_data) - len([i for i in frl_data if i[0] == -999]))
        alldata.append(data_frl_average)

def insert_data(cursor):
# TABLE average_for_race (race VARCHAR(50), year INTEGER, Overall_SPI);
    i = 0


    for year in [2010, 2011, 2012]:
        for race in ['Black', 'Hispanic', 'Ell', 'FRL', 'SWD', 'High_needs']:
        #for year in [2010, 2011, 2012]:
            insert_command = "INSERT INTO average_for_race VALUES('{}', {}, {});".format(race, year, alldata[i])
            i += 1
            cur.execute(insert_command)
            conn.commit()

            

try:
    conn = psycopg2.connect(
                   host="localhost",
                    database="school_perf",
                    user="postgres",
                    password="1")

    cur = conn.cursor()
    getdata(cur)
    insert_data(cur)
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()