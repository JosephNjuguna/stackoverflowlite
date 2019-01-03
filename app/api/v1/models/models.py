class Users():
# constructor of the application
	def __init__(self):
	    self.userslist = userlist.authdata()
#add new user to the database
	def create_a_new_user(self, signupinfo):
		newuser = self.userslist.append(signupinfo)
		all_users = self.userslist
		return all_users 
# return all users in the data structure
	def get_users(self):
		all_users = self.userslist
		return all_users
# get single users
	def get_single_user(self, name, *args):
		user = [single_user for single_user in self.userslist if single_user['name'] == name]
		if not user:
		    return name_error
		return user
# get single user by id
	def get_single_user_id(self, id, *args):
		user = [single_user for single_user in self.userslist if single_user['public_id'] == id]
		if not user:
		    return name_error
		return user
# user update profile
	def user_update_profile(self,public_id,name,password):
		for update in self.userslist:
		    update['name'] == name
		    update['password'] == password
		updated_data = update
		return updated_data
# user delete account 
	def delete_account(self, public_id, args):
		user = [userid for userid in self.userslist if userid['name'] == public_id]
		if not user:
			return name_error
		deletedaccount = self.userslist.remove(user[0])
		all_users = self.userslist
		return all_users
