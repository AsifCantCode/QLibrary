
hostaddr="localhost";
localStorage.setItem('host', hostaddr);

$('#loginButton').click(function() {
    const username = $('#username').val();
    const password = $('#password').val();
    //const remember = $('#remember').prop('checked');

    // Send login request to the server using jQuery's AJAX

    const requestBody = {
        username : username,
        password : password
    }

    let hash = btoa(username + ":" + password);
    $.ajax({
        type: 'POST',
        url: 'http://'+hostaddr+':8081/login/member',
        contentType: 'application/x-www-form-urlencoded',
        data: requestBody,
        headers:{
            'Authorization': 'Basic ' + hash
        },

        
        success: function(data) {
            localStorage.setItem("mysession" , data);
            localStorage.setItem("myhash" , hash);
            alert('Login Successful ' + data);
            window.location.href = "student_dash.html";
        },
        error: function() {
            // Handle login error
            alert('Login failed. Please check your credentials.');
        }
    });
});