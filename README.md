# bump.github.io


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>User-Specific Data</title>
  <script src="https://alcdn.msauth.net/browser/2.18.0/js/msal-browser.min.js"></script>
</head>
<body>
  <h2>Welcome to Your Dashboard</h2>
  <div id="user-info"></div>
  <table id="attendance-table">
    <thead>
      <tr>
        <th>Mentor</th>
        <th>Email</th>
        <th>Meeting Attendance</th>
        <!-- Other columns as needed -->
      </tr>
    </thead>
    <tbody>
      <!-- Dynamic content here -->
    </tbody>
  </table>

  <script>
    // Initialize MSAL.js
    const msalConfig = {
      auth: {
        clientId: 'YOUR_CLIENT_ID',  // Your Azure AD client ID
        authority: 'https://login.microsoftonline.com/common',
        redirectUri: window.location.href
      }
    };

    const msalInstance = new msal.PublicClientApplication(msalConfig);

    // Check if user is logged in
    msalInstance.handleRedirectPromise().then((response) => {
      if (response) {
        // User is logged in
        displayUserData(response.account);
      } else {
        msalInstance.loginRedirect({ scopes: ["user.read"] });
      }
    }).catch((error) => {
      console.error(error);
    });

    function displayUserData(account) {
      // Show user info
      const userInfo = document.getElementById("user-info");
      userInfo.innerHTML = `Hello, ${account.username}`;

      // Example: Filter data based on user's email
      fetch('path/to/your/data.json')
        .then(response => response.json())
        .then(data => {
          const filteredData = data.filter(item => item.Email === account.username);
          displayData(filteredData);
        });
    }

    function displayData(filteredData) {
      const tableBody = document.getElementById("attendance-table").getElementsByTagName("tbody")[0];
      filteredData.forEach(row => {
        const tr = document.createElement("tr");
        Object.keys(row).forEach(key => {
          const td = document.createElement("td");
          td.textContent = row[key];
          tr.appendChild(td);
        });
        tableBody.appendChild(tr);
      });
    }
  </script>
</body>
</html>
