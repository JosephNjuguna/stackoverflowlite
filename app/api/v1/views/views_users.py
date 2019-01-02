"""user log in"""
@user_api.route('/auth/login', methods= ['POST'])
def user_log_in():
    data = request.get_json()
    if data == {}:
        return jsonify({"json cant be empty":empty}),401
    if data['email'] == '':
        return jsonify({"json cant be empty":empty}),401
    if data['password'] == '':
        return jsonify({"json cant be empty":empty}),401

    log_email =  data['email']
    log_password = data['password']

    user_available = [user for user in userdata if user['email'] == log_email]
   
    if len(user_available) == 0:
        return make_response(jsonify({"alert_error":alert_error}),404)
   
    if check_password_hash(user_available[0]['password'],log_password):
        token = jwt.encode({'public_id': user_available[0]["public_id"],'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)},app.config['SECRET_KEY'])
        return make_response(jsonify({"token" : token.decode('UTF-8')})) 
    return make_response(jsonify({"log in sucessful":"ok"}),200)
