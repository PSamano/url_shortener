from app import create_app, db

app = create_app()

# Ejecute la aplicación, creando las tablas de la base de datos si es necesario
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
