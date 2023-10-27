function validate() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  if (username == "admin" && password == "123") {
    fetch('/adminpage')
      .then(function(response) {
        if (response.ok) {
          window.location.href = "/adminpage";
        } else {
          alert("Failed to load admin page.");
        }
      })
      .catch(function(error) {
        console.error("Error:", error);
        alert("Failed to load admin page.");
      });
  } else {
    alert("Login failed");
  }
}
