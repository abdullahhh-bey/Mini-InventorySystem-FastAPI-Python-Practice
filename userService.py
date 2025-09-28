from models import AddUser, UserInfo

class UserService:
    def __init__(self):
        self.user_list : list[UserInfo] = [
            UserInfo(id=2, name="Alex", email="a@demo.com"),
            UserInfo(id=3, name="Pingu", email="p@demo.com")
        ]
        self.user_id = 5
        
    def get_users(self) -> list[UserInfo]:
        return self.user_list
    
    
    def get_user_by_id(self , id : int) -> UserInfo:
        for v in self.user_list:
            if id == v.id:
                return v
            else:
                continue
        
        return None
    
    def add_user(self, user: AddUser) -> UserInfo:
        new_user = UserInfo(
            id=self.user_id,
            name=user.name,
            email=user.email
        )
        self.user_list.append(new_user)
        self.user_id += 1   
        return new_user
