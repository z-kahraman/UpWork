import mysql.connector

# MySQL bağlantısını oluştur
connection = mysql.connector.connect(
    host="localhost",  # Docker MySQL konteynerinin adresi
    user="vscode",       # MySQL kullanıcı adı (varsayılan olarak "root")
    password="123456",  # MySQL kök şifresi
    database="Avalance",   # Kullanmak istediğiniz veritabanı adı
    auth_plugin="mysql_native_password"
)

# MySQL bağlantısını kontrol et
if connection.is_connected():
    print("MySQL veritabanına başarıyla bağlandı.")

# MySQL bağlantısını kapat
connection.close()
