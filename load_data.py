import psycopg2
import csv

def load_schools(cur, insert_command):
    with open("CAPT_School_Performance__2010-2012.csv") as cs:
        csv_file = csv.reader(cs, delimiter=",")
        next(csv_file, None)
        element_list = []
        el =[]
        for j in csv_file:
            el = []
            el.append(j[0])
            el.append(j[1])
            el.append(j[2])
            if el not in element_list:
                element_list.append(el)
        for element in element_list:
            cur.execute(insert_command, element)
            conn.commit()

def load_data(cur, insert_command):
    column_list_10 = [0,  3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]
    column_list_11 = [0,  4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    column_list_12 = [0,  5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    with open("CAPT_School_Performance__2010-2012.csv") as cs:
        csv_file = csv.reader(cs, delimiter=",")
        next(csv_file, None)
        for j in csv_file:
            y_2010 = [2010]
            y_2011 = [2011]
            y_2012 = [2012]
            for i in column_list_10:
                if j[i] != '':
                    y_2010.append(j[i])
                else:
                    y_2010.append(-999)
            for i in column_list_11:
                if j[i] != '':
                    y_2011.append(j[i])
                else:
                    y_2011.append(-999)
            for i in column_list_12:
                if j[i] != '':
                    y_2012.append(j[i])
                else:
                    y_2012.append(-999)
            cur.execute(insert_command, y_2010)
            conn.commit()
            cur.execute(insert_command, y_2011)
            conn.commit()
            cur.execute(insert_command, y_2012)
            conn.commit()


inset_c = """INSERT INTO data(Year, Facility_Code, Overall_SPI_OVERALL, Black_SPI_OVERALL,
        Hispanic_SPI_OVERALL, ELL_SPI_OVERALL , FRL_SPI_OVERALL, SWD_SPI_OVERALL , High_Needs_SPI_OVERALL, 
        Overall_SPI_MATH, Overall_SPI_READ, Overall_SPI_WRITE, Overall_SPI_SCIENCE) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
insert_i = """INSERT INTO school_list(Facility_Code, District_Name, School_Name) VALUES(%s, %s, %s)"""
try:
    conn = psycopg2.connect(
                   host="localhost",
                    database="school_perf",
                    user="postgres",
                    password="1")

    cur = conn.cursor()
    #load_schools(cur, insert_i)
    load_data(cur, inset_c)
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()