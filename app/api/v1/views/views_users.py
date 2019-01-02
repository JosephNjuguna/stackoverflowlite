"""user can delete their account........"""
@user_api.route('/users/<string:public_id>',methods=['DELETE'])
@token_required
def user_delete_account(current_user,public_id):
    account_remove =userauthdata.delete_account(public_id,args)
    return make_response(jsonify({"user removed .. remaining users": account_remove}),200)
