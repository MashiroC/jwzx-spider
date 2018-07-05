import pymysql


class connection():

    # def __init__(self):
    #     print('init')

    def __init__(self,username,password,database):
        self.username=username
        self.password=password
        self.database=database

        self.db=pymysql.connect('localhost',username,password,database,use_unicode=True,charset="utf8")
        self.cursor=self.db.cursor()
        self.__create_table__()

    def __create_table__(self):
        sql="""CREATE TABLE `student` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `stu_id` varchar(12) NOT NULL,
                `name` varchar(20) NOT NULL,
                `sex` varchar(2) NOT NULL,
                `class_id` varchar(12) NOT NULL,
                `major_id` varchar(8) NOT NULL,
                `major_name` varchar(30) NOT NULL,
                `collage_name` varchar(50) NOT NULL,
                `enter` varchar(4) NOT NULL,
                `pic_url` varchar(255) NOT NULL,
                PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
        self.cursor.execute(sql)
        self.db.commit()

    def insert(self,param):
        sql = """INSERT INTO student(stu_id,name,sex,class_id,major_id,major_name,collage_name,enter,pic_url)
              VALUE('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % param
        self.cursor.execute(sql)
        self.db.commit()

    def close(self):
        self.db.close()

