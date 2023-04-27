function search() {
    var req = new XMLHttpRequest();
    var result = document.getElementById('resultat');
    req.onreadystatechange = function()
    {
      console.log(this);
      if(this.readyState == 4 && this.status == 200) {
        console.log(req.response);
        result.innerHTML = req.response;
      } else {
        result.innerHTML = "Recherche en cours  , Veuillez patienter.";
      }
    }
    req.open('POST', '../cgi-bin/search.py', true);
    req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    req.send("nom="+document.getElementById('nom').value + "&prenom="+document.getElementById("prenom").value+"&annee_bac="+document.getElementById("annee_bac").value + "&email="+document.getElementById("email").value);
  }
