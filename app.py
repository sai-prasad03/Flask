from application import create_app,db
import os
config_name = os.getenv('FLASK_CONFIG','development')

app1 = create_app(config_name)

if __name__ == "__main__":
    with app1.app_context():
        db.create_all()
    app1.run(debug = True)