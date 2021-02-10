import psycopg2

# dataset contains the school performance indices for schools that are in Connecticut Academic Performance Test (CAPT).
# Cells left blank if there is no SPI, which happens when there are small N sizes for a particular subgroup or subject.
# students with disabilities (SWD)
# English Language learners (ELL)
# Students receiving free and reduced lunch (FRL)
# High-needs students: Students at risk of educational failure or special assistance and support

commands_list = ["""CREATE TABLE school_list(Facility_Code INTEGER NOT NULL PRIMARY KEY, 
    District_Name VARCHAR(100), School_Name VARCHAR(100)) """,
                 """CREATE TABLE data(Year INTEGER, Facility_Code INTEGER NOT NULL REFERENCES school_list(Facility_Code),
    Overall_SPI_OVERALL REAL, Black_SPI_OVERALL REAL, Hispanic_SPI_OVERALL REAL,
    ELL_SPI_OVERALL REAL, FRL_SPI_OVERALL REAL, SWD_SPI_OVERALL REAL, High_Needs_SPI_OVERALL REAL,
    Overall_SPI_MATH REAL, Overall_SPI_READ REAL, Overall_SPI_WRITE REAL, Overall_SPI_SCIENCE REAL); """,
                 """CREATE TABLE average_for_race (race VARCHAR(50), year INTEGER, Overall_SPI REAL);""",
                 """CREATE TABLE average_for_school(Facility_Code INTEGER NOT NULL REFERENCES school_list(Facility_Code), 
    Overall_SPI_MATH REAL, Overall_SPI_READ REAL, Overall_SPI_WRITE REAL, Overall_SPI_SCIENCE REAL)"""]
try:
    conn = psycopg2.connect(
        host="localhost",
        database="school_perf",
        user="postgres",
        password="1")
    cur = conn.cursor()
    for i in commands_list:
        cur.execute(i)
    conn.commit()
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
