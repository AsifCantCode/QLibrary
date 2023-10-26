import requests
from requests.auth import HTTPBasicAuth
import json

class librarianApi:
    def __init__(self):
        self.start=0

    @classmethod
    def insert_book(self , id ,  title , isbn , year , subject , totalcopies , availablecopies , auth1 , auth2 , auth3 ,username , password):
        url="http://localhost:8081/librarian/book-entry"

        payload={
            "id":id,
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
    
    @classmethod
    def book_info(self,bookid , username , password):
        url="http://localhost:8081/librarian/book-info/"+str(bookid)

        

        response= requests.get(url , auth=HTTPBasicAuth(username,password))

        print(response.text)

        data = json.loads(response.text)

        return data


if __name__ == "__main__":
    print(librarianApi.book_info(1 , '1234' , 'abcd'))