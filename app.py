from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from extensions import mongo, jwt       

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")


## app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)

mongo.init_app(app) 
jwt.init_app(app)

try:
    mongo.cx.admin.command("ping")
    print("MongoDB connected successfully!")
except Exception as e:
    print("MongoDB connection failed:", e)


from routes.auth import auth_bp
app.register_blueprint(auth_bp)

from routes.task import task_bp
app.register_blueprint(task_bp)    


@app.route('/')
def home():
    return jsonify({"msg": "Task API is running!"})

if __name__ == "__main__":
    app.run(debug=True)
