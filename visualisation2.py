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

    race_key_list = []
    key_get = """SELECT race FROM average_for_race;"""
    cur.execute(key_get)
    k = cur.fetchall()
    for i in k:
        if i[0] not in race_key_list:
            race_key_list.append(i[0])

    color_list = ["red", "green", "blue", "yellow", "black", "violet", ]
    plt.figure(figsize=(20, 5))
    plt.grid()
    i = 0
    x1 = []
    y1 = []
    for race in race_key_list:
        x1 = []
        y1 = []
        for year in [2010, 2011, 2012]:

            s = """SELECT overall_spi FROM average_for_race WHERE year={} AND race='{}' ;""".format(year,race)
            cur.execute(s)
            tab = cur.fetchall()
            for t in tab:
                x1.append(year)
                y1.append(t[0])

        plt.plot(x1, y1, label="Average SPI for {}".format(race), color=color_list[i])
        i += 1

    plt.xlabel("Y e a r")
    plt.title('SPI from 2010 to 2012')
    plt.legend()
    plt.show()
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()