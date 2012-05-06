batadase = (function(){
    batadase.get = function(key) {
      http = new XMLHttpRequest();
      http.open("GET", "http://batadase.com/" + key);
      http.send();
      return http.response;  
    };
    return batadase;
})();
