import psycopg2
import matplotlib.pyplot as plt

conn = None
try:
    conn = psycopg2.connect(
        host="localhost",
        database="school_perf",
        port=5432,
        user="postgres",
        password="1")

    cur = conn.cursor()

    school_key_list = []
    key_get = """SELECT facility_code FROM school_list;"""
    cur.execute(key_get)
    k = cur.fetchall()
    for i in k:
        school_key_list.append(i[0])

    color_list = ["red", "green", "blue", "yellow", "black", "violet", "orange", ]
    plt.figure(figsize=(20, 5))
    plt.grid()
    i = 0
    x1 = []
    y1 = []
    for school in school_key_list[186::]:
        x1 = []
        y1 = []
        for year in [2010, 2011, 2012]:

            s = """SELECT overall_spi_overall,year FROM data WHERE facility_code = '{}' 
                    AND year={} ORDER BY facility_code;""".format(school, year)
            cur.execute(s)
            tab = cur.fetchall()
            for t in tab:
                x1.append(t[1])
                y1.append(t[0])

        s = "SELECT school_name FROM school_list WHERE facility_code= {}".format(school)
        cur.execute(s)
        sa = cur.fetchall()
        school_name = sa[0]
        plt.plot(x1, y1, label="Overall SPI in {}".format(school_name[0]), color=color_list[i])
        i += 1

    plt.xlabel("Y e a r")
    plt.title('SPI from 2010 to 2012')
    plt.legend()
    plt.show()
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None: conn.close()