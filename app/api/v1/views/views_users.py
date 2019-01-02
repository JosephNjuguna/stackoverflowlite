"""---get a list of all users on the website"""
@user_api.route('/users',methods =['GET'])
def get_all():
    all_users =  userauthdata.get_users()
    return make_response(jsonify({"users": all_users}),200)
