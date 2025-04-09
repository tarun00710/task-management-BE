from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from extensions import mongo, jwt       

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

mongo.init_app(app) 
jwt.init_app(app)

try:
    mongo.cx.admin.command("ping")
    print("MongoDB connected successfully!")
except Exception as e:
    print("MongoDB connection failed:", e)


@app.route('/')
def home():
    return jsonify({"msg": "Task API is running!"})

if __name__ == "__main__":
    app.run(debug=True)
