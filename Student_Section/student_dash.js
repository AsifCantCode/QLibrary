const sidebarItems = document.querySelectorAll(".sidebar li");
const sections = document.querySelectorAll(".section");

sidebarItems.forEach((item) => {
  item.addEventListener("click", () => {
    // Remove active class from all sidebar items
    sidebarItems.forEach((item) => item.classList.remove("active"));
    // Add active class to clicked item
    item.classList.add("active");
    const target = item.getAttribute("data-target");
    // Hide all sections
    sections.forEach((section) => section.classList.remove("active"));
    // Show target section
    document.querySelector(target).classList.add("active");
  });
});

hostaddr="localhost";
localStorage.setItem('host', hostaddr);

$('#loginButton').click(function() {
    const userType = $('#userType').val();
    const id = $('#email').val();
    const password = $('#password').val();
    //const remember = $('#remember').prop('checked');

    // Send login request to the server using jQuery's AJAX

    const requestBody = {
        id : Number(id),
        password : password
    }

    let hash = btoa(id + ":" + password);
    
});
const hash = localStorage.getItem("myhash")

function getBorrowedBooks(){
  const username = localStorage.getItem("myusername");
  $.ajax({
    type: 'GET',
    url: 'http://'+hostaddr+':8081/borrowedBooks/'+ username,
    contentType: 'application/json',
    headers:{
        'Authorization': 'Basic ' + hash
    },

    
    success: function(data) {
        displayBorrowedBooks(data);
    },
    error: function() {
    }
  });
}

function fetchAllBorrow(){


  const requestBody = {
    username : localStorage.getItem("myusername"),
  }
  $.ajax({
    type: 'GET',
    url: 'http://'+hostaddr+':8081/student/get-all-borrow',
    contentType: 'application/x-www-form-urlencoded',
    headers:{
        'Authorization': 'Basic ' + hash
    },
    data:requestBody,


    success: function(data) {
        //console.log(data);
        displayBorrowedBooks(data);
    },
    error: function() {

    }
  });
}

fetchAllBorrow();

function displayBorrowedBooks(borrowedBooks) {
  const borrowedBooksList = document.getElementById('borrowedBooksList');
  // Clear existing borrowed books list items
  borrowedBooksList.innerHTML = '';

  borrowedBooks.forEach(book => {
      const row = document.createElement('tr');


      const overdueDays = 'test';
      const fine = 0;

      console.log(book.reservation_date)

      // Set button color and text based on the presence of a fine
      const buttonColor = fine > 0 ? 'btn-danger' : 'btn-success';
      const buttonText = fine > 0 ? `Pay Fine` : `No Fine`;

      row.innerHTML = `
          <td class="title">${book.title}</td>
          <td>${book.author}</td>
          <td>${book.genre}</td>
          <td>${book.reservation_date ? book.reservation_date : 'N/A'}</td>
          <td>${book.borrowedDeadline}</td>
          <td>${overdueDays}</td>
          <td>${fine}</td>
          <td><button class="btn ${buttonColor}" onclick="handleBookAction('${book._id}', ${fine})">${buttonText}</button></td>
      `;
      borrowedBooksList.appendChild(row);
  });
}

const searchInput = document.getElementById('search');
searchInput.addEventListener('input', function () {
    const searchTerm = this.value.trim().toLowerCase();
    filterBooks(searchTerm);
});

function filterBooks(searchTerm) {
    const allBooksList = document.getElementById('allBooksList');
    const allBooksRows = allBooksList.querySelectorAll('tr');

    allBooksRows.forEach(row => {
        const title = row.querySelector('.title').innerText.toLowerCase();
        const author = row.querySelectorAll('td')[1].innerText.toLowerCase();
        const genre = row.querySelectorAll('td')[2].innerText.toLowerCase();

        if (title.includes(searchTerm) || author.includes(searchTerm) || genre.includes(searchTerm)) {
            row.style.display = ''; // Show the row
        } else {
            row.style.display = 'none'; // Hide the row
        }
    });
}

function fetchAllBooks() {
    // Fetch all books from the backend
    $.ajax({
        type: 'GET',
        url: 'http://' + hostaddr + ':8081/student/get-all-books',
        contentType: 'application/json',
        headers: {
            'Authorization': 'Basic ' + hash
        },
        success: function (data) {
            displayAllBooks(data);
        },
        error: function () {
            // Handle error
            alert('Error fetching books.');
        }
    });
}

function reserveBook(bookId) {
    // Implement your logic to handle book reservation
    // You can use AJAX to send a reservation request to the backend
    // and update the UI accordingly
    console.log(`Reserving book with ID: ${bookId}`);
    // Add your AJAX call or other reservation logic here
}


function displayAllBooks(allBooks) {
    const allBooksList = document.getElementById('allBooksList');
    // Clear existing borrowed books list items
    allBooksList.innerHTML = '';

    allBooks.forEach(book => {
        const row = document.createElement('tr');

    row.innerHTML = `
    <td class="title">${book.title}</td>
    <td>${book.authors}</td>
    <td>${book.genre}</td>
    <td>${book.totalCopies}</td>
    <td>${book.availableCopies}</td>
    <td><button class="btn btn-primary" onclick="reserveBook('${book.id}')">Reserve</button></td>
    `;

        allBooksList.appendChild(row);
    });
}

$('#updateStudentForm').submit(function (event) {
    event.preventDefault();

    const username = localStorage.getItem("myusername");
    const updatedEmail = $('#email_student').val();
    const updatedPhone = $('#phone_student').val();

    const updatedMember = {
        email: updatedEmail,
        contactNumber: updatedPhone
    };

    $.ajax({
        type: 'PUT',
        url: `http://${hostaddr}:8081/student/update-member/${username}`,
        contentType: 'application/json',
        data: JSON.stringify(updatedMember),
        headers: {
            'Authorization': 'Basic ' + hash
        },
        success: function (data) {
            alert('Member information updated successfully.');
            window.location.reload();
        },
        error: function () {
            // Handle error
            alert('Error updating member information.');
        }
    });
});


// Fetch all books when the page loads
$(document).ready(function () {
    fetchAllBooks();
    const username = localStorage.getItem("myusername");
    $.ajax({
    type: 'GET',
    url: `http://${hostaddr}:8081/student/member-info/${username}`,
    contentType: 'application/json',
    headers: {
        'Authorization': 'Basic ' + hash
    },
    success: function (data) {
        // Handle the member information received in the 'data' variable
        if (data) {
            console.log('Member Information:', data);
            $('#s_name').text(data.name);
            $('#s_id').text(data.memberid);
            $('#s_mail').text(data.email);
            $('#email_student').val(data.email);
            $('#phone_student').val(data.contactNumber);
        } else {
            console.log('Member not found.');
        }
    },
    error: function () {
        // Handle error
        alert('Error fetching member information.');
    }
});
});