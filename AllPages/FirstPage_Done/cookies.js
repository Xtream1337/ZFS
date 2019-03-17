function setCookie() 
{
    document.cookie = "name=" + document.getElementById("txtName").value;

}

function getCookie() 
{
    var cookiesArray = document.cookie.split("; ");
        
        for (var i = 0; i < cookiesArray.length; i++) 
        {
            var nameValueArray = cookiesArray[i].split("=");
                if (nameValueArray[0] == "name") 
                    {
                        document.getElementById("txtName").value = nameValueArray[1];
                    }
         }   
}