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
    def book_info(self, bookid , username , password):
        url="http://localhost:8081/librarian/book-info/"+str(bookid)

        

        response= requests.get(url , auth=HTTPBasicAuth(username,password))

        print(response.text)

        data = json.loads(response.text)

        return data

    @classmethod
    def insert_member(self, name, studentId, email, phoneNo, memUsername, username, password):
        url = "http://localhost:8081/librarian/member-registration"

        payload = {
        "name": name,
        "memberid": studentId,
        "email": email,
        "contactNumber": phoneNo,
        "username": memUsername,
        }
        response = requests.post(url, params=payload, auth=HTTPBasicAuth(username, password))
        print(response.status_code)

    @classmethod
    def bookborrow(self,  Id, books , username , password):
        url = "http://localhost:8081/librarian/book-borrow/"+str(Id)

        booklist = list(books)
        print(booklist)
        payload = {
            "bookids": booklist
        }
        response = requests.post(url, params=payload, auth=HTTPBasicAuth(username, password))
        print(response.status_code)

    @classmethod
    def bookBorrowDeets(self , memberid,username,password):
        url="http://localhost:8081/librarian/book-borrow-deets/"+str(memberid)
        response=requests.get(url, auth=HTTPBasicAuth(username,password))
        print(response.text)
        return (json.loads(str(response.text)))

    @classmethod
    def fineDeets(self , borrowid,username,password):
        url="http://localhost:8081/librarian/fine-deets/"+str(borrowid)
        response=requests.get(url, auth=HTTPBasicAuth(username,password))
        print(response.text)
        return str(response.text)

    @classmethod
    def bookreturn(self, borrowid, username, password):
        url = "http://localhost:8081/librarian/book-return/" + str(borrowid)
        response = requests.post(url, auth=HTTPBasicAuth(username, password))
        print(response.text)
        return str(response.text)


if __name__ == "__main__":
    print(librarianApi.book_info(1 , '1234' , 'abcd'))