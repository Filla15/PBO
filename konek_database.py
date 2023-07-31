# Integrasi dengan mysql
import pymysql

# membuka koneksi dengan mysql / open koneksi
db = pymysql.connect(user='root',password='',host='127.0.0.1',database='db_python')

# cursor
connect_db = db.cursor()

# Mengeksekusi SQL Statement: Create, Read, Delete, Update
#1. Create tabel
#sql = """create table karyawan (nama_depan char(20) Not Null,
#nama_belakang char(20),
#umur int,
#jenis_kelamin char(1),
#income float)"""

#connect_db.execute(sql)

#2. insert record 
sql_insert = """insert into karyawan(nama_depan,nama_belakang,umur,jenis_kelamin,income)
values ('Mur','salim',24,"L",3000000)"""

connect_db.execute(sql_insert)
db.commit()

# 3.insert multi record
sql_insert = """insert into karyawan(nama_depan,nama_belakang,umur,jenis_kelamin,income)
values('%s','%s',%d,'%s',%d)"""
try:
    #mengekseskusi sql
    #connect_db.execute(sql_insert % ('Mur','salim',24,"L",3000000))
    #connect_db.execute(sql_insert % ('Adi','Kususma',26,"L",4000000))
    #connect_db.execute(sql_insert % ('Elsa','sahara',14,"P",9000000))
    #connect_db.execute(sql_insert % ('filla','firontina',20,"P",7000000))
    #connect_db.execute(sql_insert % ('karlina','syahdu',24,"P",1000000))

    #melakukan commit, lakukan perubahan pada database
    db.commit()
    print ("Berhasil Di Simpan!")
except:
    #jika terjadi kesalahan dikembalikan seperti semula
    print ("gagal di simpan!")
    db.rollback

db = pymysql.connect(user='root',password='',host='127.0.0.1',database='db_python')
# cursor
connect_db = db.cursor()

#1. Create tabel
sql = """create table tb_produksi (id_produksi int PRIMARY KEY AUTO_INCREMENT, tgl_produksi Date, nama_produk varchar (50), jumlah int (11), id_karyawan int)"""

connect_db.execute(sql)

sql_insert = """insert into karyawan(nama_depan,nama_belakang,umur,jenis_kelamin,income)
values ('Mur','salim',24,"L",3000000)"""

connect_db.execute(sql_insert)
db.commit()

#closed/ menututup koneksi
connect_db.close()