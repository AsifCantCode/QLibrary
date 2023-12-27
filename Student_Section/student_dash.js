const sidebarItems = document.querySelectorAll(".sidebar li");
const sections = document.querySelectorAll(".section");
totalFines = 0;

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

hostaddr = "localhost";
localStorage.setItem('host', hostaddr);

$('#loginButton').click(function () {
    const userType = $('#userType').val();
    const id = $('#email').val();
    const password = $('#password').val();
    //const remember = $('#remember').prop('checked');

    // Send login request to the server using jQuery's AJAX

    const requestBody = {
        id: Number(id),
        password: password
    }

    let hash = btoa(id + ":" + password);

});
const hash = localStorage.getItem("myhash")

function getBorrowedBooks() {
    const username = localStorage.getItem("myusername");
    $.ajax({
        type: 'GET',
        url: 'http://' + hostaddr + ':8081/borrowedBooks/' + username,
        contentType: 'application/json',
        headers: {
            'Authorization': 'Basic ' + hash
        },


        success: function (data) {
            displayBorrowedBooks(data);
        },
        error: function () {
        }
    });
}

function fetchAllBorrow(callback) {
    const requestBody = {
        username: localStorage.getItem("myusername"),
    };

    $.ajax({
        type: 'GET',
        url: 'http://' + hostaddr + ':8081/student/get-all-borrow',
        contentType: 'application/x-www-form-urlencoded',
        headers: {
            'Authorization': 'Basic ' + hash
        },
        data: requestBody,
        success: function (data) {
            displayBorrowedBooks(data);
            totalFines = calculateTotalFine(data);
            document.getElementById('totalFine').innerText = totalFines;

            // Call the callback function after the asynchronous operation is complete
            callback(totalFines);
        },
        error: function () {
            // Handle error
        }
    });
}

function getFine(callback) {
    fetchAllBorrow(function (totalFines) {
        callback(totalFines);
    });
}


function calculateFine(reservationDate, borrowedDeadline, finePerDay) {
    const millisecondsPerDay = 24 * 60 * 60 * 1000; // Number of milliseconds in a day

    // Convert reservation date and borrowed deadline to Date objects
    const reservationDateObj = new Date(reservationDate);
    const borrowedDeadlineObj = new Date(borrowedDeadline);

    // If the conversion fails, return 0 fine (or handle it according to your requirements)
    if (isNaN(reservationDateObj) || isNaN(borrowedDeadlineObj)) {
        return 0;
    }

    // Calculate the difference in days
    const overdueDays = Math.floor((borrowedDeadlineObj - reservationDateObj) / millisecondsPerDay);

    // Calculate the fine
    const fine = overdueDays > 0 ? overdueDays * finePerDay : 0;

    return fine;
}

function calculateTotalFine(borrowedBooks) {
    const finePerDay = 5; // Set your fine amount per day here
    let totalFine = 0;

    borrowedBooks.forEach(book => {
        //const fine = calculateFine(book.reservation_date, book.borrowedDeadline, finePerDay);
        //totalFine += fine;
        totalFine += Number(book.fine);
    });

    return totalFine;
}

function displayBorrowedBooks(borrowedBooks) {
    const borrowedBooksList = document.getElementById('borrowedBooksList');
    // Clear existing borrowed books list items
    borrowedBooksList.innerHTML = '';

    borrowedBooks.forEach(book => {
        const row = document.createElement('tr');


        const overdueDays = 'test';
        //const fine = calculateFine(book.reservation_date, book.borrowedDeadline, 5);
        const fine = book.fine;

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
            <td>${book.overdue}</td>
            <td>${fine}</td>
            `;
        //<td><button class="btn ${buttonColor}" onclick="handleBookAction('${book._id}', ${fine})">${buttonText}</button></td>
        borrowedBooksList.appendChild(row);
    });
}

const searchInput = document.getElementById('allSearch');
searchInput.addEventListener('input', function () {
    const searchTerm = this.value.trim().toLowerCase();
    filterBooks(searchTerm);
});

const EsearchInput = document.getElementById('eSearch');
EsearchInput.addEventListener('input', function () {
    const EsearchTerm = this.value.trim().toLowerCase();
    filtereBooks(EsearchTerm);
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

function filtereBooks(searchTerm) {
    const allBooksList = document.getElementById('eBooksList');
    const allBooksRows = allBooksList.querySelectorAll('tr');

    allBooksRows.forEach(row => {
        const eBookid = row.querySelectorAll('td')[0].innerText;
        const eName = row.querySelectorAll('td')[1].innerText.toLowerCase();

        if (eBookid.includes(searchTerm) || eName.includes(searchTerm)) {
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

function reserveBook(username , bookId) {
    // Implement your logic to handle book reservation
    // You can use AJAX to send a reservation request to the backend
    // and update the UI accordingly

    const url = 'http://localhost:8081/student/reserve'; // Replace with your API endpoint URL

    // Data to send in the request body
    const requestData = {
        username: username,
        bookid: bookId
    };

    $.ajax({
        url: 'http://localhost:8081/student/reserve',
        type: 'POST',
        data: requestData,
        success: function(response) {
            
            alert('Book reserved successfully', response);
            
        },

        headers: {
            'Authorization': 'Basic ' + hash
        },
        error: function(jqXHR, textStatus, errorThrown) {
            
            alert('The book is already available', errorThrown);
            
        }
    });



    console.log(`Reserving book with ID: ${bookId}`);
    // Add your AJAX call or other reservation logic here
}


function displayAllBooks(allBooks) {
    const allBooksList = document.getElementById('allBooksList');
    // Clear existing borrowed books list items

    const username = localStorage.getItem("myusername");
    allBooksList.innerHTML = '';

    allBooks.forEach(book => {
        const row = document.createElement('tr');

        row.innerHTML = `
    <td class="title">${book.title}</td>
    <td>${book.authors}</td>
    <td>${book.genre}</td>
    <td>${book.totalCopies}</td>
    <td>${book.availableCopies}</td>
    <td><button class="btn btn-primary tblbtn" onclick="reserveBook('${username}' , '${book.id}')">Reserve</button></td>
    `;

        allBooksList.appendChild(row);
    });
}

function displayEBooks(allBooks) {
    const allBooksList = document.getElementById('eBooksList');
    // Clear existing borrowed books list items
    allBooksList.innerHTML = '';
        allBooks.forEach(book => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td class="title">${book.ebookId}</td>
            <td>${book.ebookFileName}</td>
            <td>${Number(book.ebookPhotoId).toFixed(2)} MB</td>
            <td><button class="btn btn-primary tblbtn" onclick="downloadBook('${book.ebookId}')">Download</button></td>
        `;
        allBooksList.appendChild(row);
    });
}


function fetchAllEBooks() {
    // Fetch all books from the backend
    $.ajax({
        type: 'GET',
        url: 'http://' + hostaddr + ':8081/ebook/get/allebooks',
        contentType: 'application/json',
        headers: {
            'Authorization': 'Basic ' + hash
        },
        success: function (data) {
            console.log(data)
            displayEBooks(data);
        },
        error: function () {
            // Handle error
            alert('Error fetching books.');
        }
    });
}


function downloadBook(ebookId) {
    // Create a hidden anchor element
    const downloadLink = document.createElement('a');

    // Set the download link's href attribute to the ebook download URL
    downloadLink.href = 'http://' + hostaddr + ':8081/ebook/get/' + ebookId;

    // Set the download attribute to specify the filename
    downloadLink.download = `ebook_${ebookId}.pdf`;

    // Simulate a click on the anchor element to trigger the download
    downloadLink.click();
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
            console.log(data);
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