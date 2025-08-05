from flask import Blueprint, request, jsonify
from ..db import db
from ..models.comment import Comment

comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/', methods=['POST'])
def add_comment():
    data = request.get_json()
    comment = Comment(task_id=data['task_id'], content=data['content'])
    db.session.add(comment)
    db.session.commit()
    return jsonify({'message': 'Comment added'}), 201

@comments_bp.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.get_json()
    comment = Comment.query.get_or_404(comment_id)
    comment.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Comment updated'})

@comments_bp.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Comment deleted'})

@comments_bp.route('/task/<int:task_id>', methods=['GET'])
def get_comments(task_id):
    comments = Comment.query.filter_by(task_id=task_id).all()
    return jsonify([{'id': c.id, 'content': c.content} for c in comments])
