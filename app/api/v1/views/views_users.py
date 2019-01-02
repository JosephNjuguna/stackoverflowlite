"""get single user using public_id"""
@user_api.route('/user/<string:public_id>',methods=['GET'])
@token_required
def get_one_user_id(current_user,public_id):
    single_user = userauthdata.get_single_user_id(public_id,args)
    return make_response(jsonify({"single user": single_user}),200)
