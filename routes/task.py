from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId

from extensions import mongo

task_bp = Blueprint('task', __name__)

# Create Task
@task_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    task = {
        "user_id": user_id,
        "title": data.get("title"),
        "description": data.get("description", ""),
        "status": data.get("status", "pending")
    }
    
    mongo.db.tasks.insert_one(task)
    return jsonify({"msg": "Task created successfully"}), 201


# Get All Tasks for Logged-in User
@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = list(mongo.db.tasks.find({"user_id": user_id}))
    
    for task in tasks:
        task["_id"] = str(task["_id"])
    
    return jsonify(tasks), 200


# Update Task
@task_bp.route('/tasks/<task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    data = request.get_json()

    updated = mongo.db.tasks.update_one(
        {"_id": ObjectId(task_id), "user_id": user_id},
        {"$set": {
            "title": data.get("title"),
            "description": data.get("description"),
            "status": data.get("status")
        }}
    )

    if updated.modified_count == 0:
        return jsonify({"msg": "Task not found or not updated"}), 404

    return jsonify({"msg": "Task updated"}), 200


# Delete Task
@task_bp.route('/tasks/<task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    deleted = mongo.db.tasks.delete_one({
        "_id": ObjectId(task_id),
        "user_id": user_id
    })

    if deleted.deleted_count == 0:
        return jsonify({"msg": "Task not found or not deleted"}), 404

    return jsonify({"msg": "Task deleted"}), 200

