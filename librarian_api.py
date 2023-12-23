import requests
from requests.auth import HTTPBasicAuth
import json

class librarianApi:
    def __init__(self):
        self.start=0

    @classmethod
    def insert_book(self , id ,  title , isbn , year , subject , totalcopies , availablecopies , auth1 , auth2 , auth3 ,genre , isAcademic ,username , password):
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
            "authorid3":auth3,
            "genre":genre,
            "isAcademic":isAcademic
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
    def get_genres(self,username,password):
        url = 'http://localhost:8081/librarian/get-genres'  # Replace with the actual URL

        try:
            response = requests.get(url,auth=HTTPBasicAuth(username,password))
            if response.status_code == 200:
                genre_names = response.json()
                return genre_names
            else:
                print(f"Failed to retrieve genres. Status code: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return []

    @classmethod
    def get_authors(self, genre , username, password):
        url = 'http://localhost:8081/librarian/get-authors'  # Replace with the actual URL

        payload = {
            "genreName": genre,

        }

        try:
            response = requests.get(url,params=payload, auth=HTTPBasicAuth(username, password))
            if response.status_code == 200:
                genre_names = response.json()
                return genre_names
            else:
                print(f"Failed to retrieve genres. Status code: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return []@classmethod
    @classmethod
    def get_books(self, genre ,authorId, username, password):
        url = 'http://localhost:8081/librarian/get-books'  # Replace with the actual URL

        payload = {
            "genreName": genre,
            "authorId":authorId
        }

        try:
            response = requests.get(url,params=payload, auth=HTTPBasicAuth(username, password))
            if response.status_code == 200:
                genre_names = response.json()
                return genre_names
            else:
                print(f"Failed to retrieve genres. Status code: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return []

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

    @classmethod
    def upload_file_to_api(self, file_path, username, password):

        api_url="http://localhost:8081/file/upload"
        try:
            with open(file_path, 'rb') as file:
                files = {'file': file}
                auth = HTTPBasicAuth(username, password)
                response = requests.post(api_url, files=files, auth=auth)

                if response.status_code == 200:
                    print("File uploaded successfully!")
                    print("Response:", response.json())  # If the API returns JSON response
                    return response.json()
                else:
                    print(f"Failed to upload file. Status code: {response.status_code}")
                    print("Response:", response.text)  # Get the error response text
        except FileNotFoundError:
            print(f"File not found at path: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def ebook_reg(self , pdfId,photoId):
            url="http://localhost:8081/ebook/create"

            payload = {
                "fileId": pdfId,
                "photoId":photoId

            }
            response = requests.post(url, params=payload)
            print(response.status_code)







if __name__ == "__main__":
    print(librarianApi.book_info(1 , '1234' , 'abcd'))