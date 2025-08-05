import json
from app import create_app
from app.db import db

def test_add_comment():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        # Step 1: Add a comment
        response = client.post('/api/comments/', json={
            'task_id': 1,
            'content': 'Test comment'
        })

        assert response.status_code == 201
        assert b'Comment added' in response.data
