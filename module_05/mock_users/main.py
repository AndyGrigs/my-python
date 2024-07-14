from mock import get_mock_user
import json 

# mock_user = get_mock_user()
# print(mock_user)
file_name = input("Enter filename:")
amount = int(input("Enter amount of users:"))

with open(file_name, "w") as file:
    moked_users=[]
    for i in range(amount):
        user = get_mock_user()
        moked_users.append(json.dumps(user))
    file.writelines(moked_users)
