import pymysql

class Database:

    def __init__(self) -> None:
        
        self.db = pymysql.connect(
            host = "10.162.14.147",
            user = "root",
            password="Govee123@",
            database='sys'   
        )
        self.cursor =  self.db.cursor()

    def execute_sql(self, sql):
        
        self.cursor.execute(sql)
        self.db.commit()
      
    def close_db(self):

        self.db.close()

    def del_table(self, table_name):
        sql = f"DROP TABLE {table_name}"
        self.execute_sql(sql)

    def create_table_info(self, table_name):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")    # 如果表存在则删除
        sql = f"""CREATE TABLE {table_name}(
                ID  INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Label_Id    INT(255),
                Label_Name  CHAR(255), 
                Lamp_Effect INT(255))"""
        self.execute_sql(sql)

    def create_table_amount(self, table_name):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")    # 如果表存在则删除
        sql = f"""CREATE TABLE {table_name}(
                ID  INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Label_Id    INT(255),
                Label_Name  CHAR(255), 
                Train_Image_data INT(255),
                Test_Image_data INT(255),
                Other_Image_data INT(255)
                )
            """
        self.execute_sql(sql)

    def create_table_images(self, table_name):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")    # 如果表存在则删除
        sql = f"""CREATE TABLE {table_name}(
                ID  INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Label_Id    INT(255),
                Label_Name  CHAR(255), 
                Image_Name CHAR(255),
                Image_Path CHAR(255),
                Label_Txt_Path CHAR(255)
                )
            """

        self.execute_sql(sql)

    def insert_data_info(self, table_name, label_id, label, lamp_effect_id):
        sql_insert = f"insert into {table_name}(Label_Id, Label_Name, Lamp_Effect) values({label_id}, '{label}', {lamp_effect_id})"
        self.execute_sql(sql_insert)

    def insert_data_amount(self, table_name, label_id, label, trani_amount, test_amount, other_amount):
        sql_insert = f"insert into {table_name}(Label_Id, Label_Name, Train_Image_data, Test_Image_data, Other_Image_data) \
                                        values({label_id}, '{label}', {trani_amount}, {test_amount}, {other_amount})"
        self.execute_sql(sql_insert)
        
    def insert_data_images(self, table_name, label_id, label, image, image_path, label_path):
        sql_insert = f"insert into {table_name}(Label_Id, Label_Name, Lamp_Effect) \
                                        values({label_id}, '{label}', '{image}', '{image_path}', '{label_path}')"
        self.execute_sql(sql_insert)

    def select_from(self, table_name):
        sql = f"SELECT * FROM {table_name}"
        self.execute_sql(sql)
        return self.cursor.description, self.cursor.fetchall()

    def update_from(self, table_name):
        sql = f"UPDATE {table_name} SET Label_Name = 'defeat' WHERE Lamp_Effect = '2'"
        self.execute_sql(sql)

    def delete_data(self, table_name):
        sql = f"DELETE FROM {table_name} WHERE Lamp_Effect = '2'"
        self.execute_sql(sql)

