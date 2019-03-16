function setCookie() 
{
    document.cookie = "name=" + document.getElementById("txtName").value;
    window.localStorage.setItem("name", document.getElementById("txtName").value)
}

function getCookie() 
{

    document.getElementById("txtName").value = window.localStorage.getItem("name");
                        
}