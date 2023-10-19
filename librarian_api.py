import requests
from requests.auth import HTTPBasicAuth

class librarianApi:
    def __init__(self):
        self.start=0

    @classmethod
    def insert_book(self , title , isbn , year , subject , totalcopies , availablecopies , auth1 , auth2 , auth3 ,username , password):
        url="http://localhost:8081/librarian/book-entry"

        payload={
            "title":title,
            "isbn":isbn,
            "year":year,
            "subject":subject,
            "totalcopies":totalcopies,
            "availablecopies":availablecopies,
            "authorid1":auth1,
            "authorid2":auth2,
            "authorid3":auth3
        }

        response= requests.post(url , params=payload , auth=HTTPBasicAuth(username,password))

        print(response.status_code)
    
    @classmethod
    def insert_author(self , id ,name , nationality ,username , password):
        url="http://localhost:8081/librarian/author-entry"

        payload={
            "id":id,
            "name":name,
            "nationality":nationality
        }

        response= requests.post(url , params=payload , auth=HTTPBasicAuth(username,password))

        print(response.status_code)



if __name__ == "__main__":
    librarianApi.insert_book("BAJE BOI" , 12345 ,"2014" , "CSE" , 26 ,15 ,0,0,0,  "1234" ,"abcd")