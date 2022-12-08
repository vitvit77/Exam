import pymysql.cursors
from config import CONFIG

# Подключиться к базе данных. Открыл временно для всех IP. После сдачи / не сдачи уберу ))


class Database:
    def __init__(self, db_location: str) -> None:
        self.mydb = pymysql.connect(host=CONFIG['HOST'],
                               user=CONFIG['USER'],
                               password=CONFIG['PASS'],
                               db=CONFIG['DB'],
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)

    def getAllSensors(self):
        with self.mydb.cursor() as cursor:
            sql = "SELECT id, Count FROM Sensors"
            return cursor.execute(sql)