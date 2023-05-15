import psycopg2
import csv

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')

cursor = conn.cursor()


query = '''
SELECT person.region, 
MAX(ball_100) FILTER (WHERE status = 'Зараховано' and year=2019 AND person_subject_eo.subject_name = 'Математика') as max_100_2019,
MAX(ball_100) FILTER (WHERE status = 'Зараховано' and year=2021 AND person_subject_eo.subject_name = 'Математика') as max_100_2021,
MAX(ball) FILTER (WHERE status = 'Зараховано' and year=2019 AND person_subject_eo.subject_name = 'Математика') as max_test_2019,
MAX(ball) FILTER (WHERE status = 'Зараховано' and year=2021 AND person_subject_eo.subject_name = 'Математика') as max_test_2021,
MAX(ball_12) FILTER (WHERE status = 'Зараховано' and year=2019 AND person_subject_eo.subject_name = 'Математика') as max_12_2019,
MAX(ball_12) FILTER (WHERE status = 'Зараховано' and year=2021 AND person_subject_eo.subject_name = 'Математика') as max_12_2021 
FROM person JOIN person_subject_eo ON person_subject_eo.out_id = person.out_id 
GROUP BY person.region
ORDER BY person.region;
'''

cursor.execute(query)


with open('result2.csv', 'w', encoding="utf-8") as f:
    writer = csv.writer(f, lineterminator="\n")
    for row in cursor:
        writer.writerow(row)


cursor.close()
conn.close()