"""update single user profile using public_id"""
@user_api.route('/users/<string:public_id>',methods=['PUT'])
@token_required
def user_update_profile(current_user,public_id):
    data = request.get_json()
    if data == {}:
        return "fields cant be empty",201
    name = data['name']
    password = data['password']
    user_update = userauthdata.user_update_profile(public_id,name,password)
    return make_response(user_update)