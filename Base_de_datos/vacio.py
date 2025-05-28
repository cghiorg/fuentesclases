"SELECT * FROM usuarios WHERE edad > 18"
Usuario.query.filter_by(edad=18).all()


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/mi_basedatos'