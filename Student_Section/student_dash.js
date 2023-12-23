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

windows.onload = () => {
  const id = 1;
  $.ajax({
    type: 'GET',
    url: 'http://'+hostaddr+':8081/borrowedBooks/'+ id,
    contentType: 'application/json',
    headers:{
        'Authorization': 'Basic ' + hash
    },

    
    success: function(data) {
        displayBorrowedBooks(data);
    },
    error: function() {
        // Handle login error
        alert('Login failed. Please check your credentials.');
    }
});
}

function displayBorrowedBooks(borrowedBooks) {
  const borrowedBooksList = document.getElementById('borrowedBooksList');
  // Clear existing borrowed books list items
  borrowedBooksList.innerHTML = '';

  borrowedBooks.forEach(book => {
      const row = document.createElement('tr');

      // Calculate overdue days and fines
      const borrowedDeadline = new Date(book.borrowedDeadline);
      const randomInteger = Math.floor(Math.random() * 10);
      const today = new Date();
      if(randomInteger%2!=0){
          today.setDate(today.getDate() - 10);
      }
      else{
          today.setDate(today.getDate() + 10);
      }
      const overdueDays = Math.max(0, Math.floor((today - borrowedDeadline) / (1000 * 60 * 60 * 24)));
      const fine = calculateFine(borrowedDeadline,randomInteger);

      // Set button color and text based on the presence of a fine
      const buttonColor = fine > 0 ? 'btn-danger' : 'btn-success';
      const buttonText = fine > 0 ? `Pay Fine & Return` : `Return`;

      row.innerHTML = `
          <td class="title">${book.title}</td>
          <td>${book.author}</td>
          <td>${book.genre}</td>
          <td>${book.reservation_date}</td>
          <td>${new Date(book.borrowedDeadline).toLocaleDateString()}</td>
          <td>${overdueDays}</td>
          <td>${fine}</td>
          <td><button class="btn ${buttonColor}" onclick="handleBookAction('${book._id}', ${fine})">${buttonText}</button></td>
      `;
      borrowedBooksList.appendChild(row);
  });
}