from app import app
from data import *
from flask import request, jsonify, abot

new_post_req = ['title, desc']

@app.route('/post', methods=['POST'])
def post():
    # Check if we got a JSON, otherwise reject request
    content = request.get_json()
    if content is None:
        return jsonify({'error': 'did not receive JSON'}), 400

    # Check that the request has the expected fields
    for key in post_request:
        if key not in content:
            return jsonify({'error': 'missing keys in post request'}), 400

    # Check that each key is a correct value
    #if not is_string(content['auth_token'], content['content']) or not is_iso8601(content['timestamp']) or not is_float(content['lat'], content['lon']):
    #    return jsonify({'error': 'incorrectly formatted values'}), 400

    # Add to database
    new_uuid = str(uuid.uuid4())
    post = Post(title=content['title'], 
                post_uuid=new_uuid
                desc=content['desc'])
    db.session.add(post)
    db.session.commit()

    return jsonify({'post_uuid': new_uuid}), 202


@app.route('/retrieve', methods=['GET', 'POST'])

def getposts():
    print request.get_data()

    content = request.get_json()
    if content is None:
        return jsonify({'error': 'did not receive JSON'}), 400

    for key in nearbyposts_request:
        if key not in content:
            return jsonify({'error': 'missing keys in post request'}), 400

    #if not is_string(content['auth_token']) or not is_iso8601(content['timestamp']) or not is_float(content['lat'], content['lon']):
    #    return jsonify({'error': 'incorrectly formatted values'}), 400

    # Fetch from database O(n) rn lol so bad
    ret = {
        'posts': []
    }
    for post in Post.query.all():
        data = {}
        data['title'] = post.title
        data['desc'] = post.desc
        data['post_uuid'] = post.post_uuid
        ret['posts'].append(data)

    return jsonify(ret), 202
