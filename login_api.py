import requests

class loginController:
    
    librarian_url="http://localhost:8081/login/librarian"
    def __init__(self):
        self.url = "https://api.example.com/data"

    @classmethod    
    def librarian_login(self , username , password):

        login_payload ={
            "username":username,
            "password":password
        }
        response = requests.post(loginController.librarian_url , params=login_payload )

        print(response.json())



if __name__ == "__main__":
    loginController.librarian_login("1234" , "abcd")
          
