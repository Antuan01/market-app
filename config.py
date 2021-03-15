class Config:
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = "uploads"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = True



#load_dotenv()
#mysql://username:password@server/db
#print(os.getenv("DOMAIN"))
