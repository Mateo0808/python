class Config:
    
    #Definir 'la cadena de conexion' (connectionstring)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3307/flask-shopy-2687340'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = 'loqueudquiera'