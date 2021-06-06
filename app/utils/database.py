import databases

# DATABASE_URL = "sqlite:///database/data_dev.sqlite?check_same_thread=False"
DATABASE_URL = "sqlite:///database/data_dev.sqlite"
database = databases.Database(DATABASE_URL)