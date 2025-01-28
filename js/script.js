 this.__apiBase = apiBase || 'https://api.github.com';
  this.__auth = {
     token: auth.token,
     username: auth.username,
     password: auth.password
  };
  if (auth.token) {
     this.__authorizationHeader = 'token ' + auth.token;
  } else if (auth.username && auth.password) {
     this.__authorizationHeader = 'Basic ' + Base64.encode(auth.username + ':' + auth.password);
  }
