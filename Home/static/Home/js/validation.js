// validate Password
function checkPass()
{
    var pass1 = document.getElementById('pass1');
    var pass2 = document.getElementById('pass2');
    var message = document.getElementById('confirmMessage');
    var Color = "#ff0000";
    if(pass1.value != pass2.value){
        message.style.color = Color;
        message.innerHTML = "Passwords Do Not Match!"
    }
    else
        message.innerHTML = ""
}
// validate Email
function email_validate(email)
{
    var regMail = /^([_a-zA-Z0-9-]+)(\.[_a-zA-Z0-9-]+)*@([a-zA-Z0-9-]+\.)+([a-zA-Z]{2,3})$/;
    var message = document.getElementById("status");
    var Color = "#ff0000";

        if(regMail.test(email) == false || email=="" || email==null)
        {
        message.style.color = Color;
        message.innerHTML    = "<span>Please enter a valid email</span><br>";
        }
        else
        {
        document.getElementById("status").innerHTML	= "<span> </span>";
        }
}
// validate name
function name_validate(name)
{
    var message = document.getElementById("nameStatus");
    var Color = "#ff0000";

        if(name==="" || name===null)
        {
        message.style.color = Color;
        message.innerHTML  = "<span>Please enter your name</span><br>";
        }
        else
        {
        document.getElementById("nameStatus").innerHTML	= "<span> </span>";
        }
}
// validate address
function add_validate(address)
{
var regAdd = /^(?=.*\d)[a-zA-Z\s\d\/]+$/;

    if(regAdd.test(address) == false)
    {
    document.getElementById("statusAdd").innerHTML	= "<span class='warning'>Address is not valid yet.</span>";
    }
    else
    {
    document.getElementById("statusAdd").innerHTML	= "<span class='valid'>Thanks, Address looks valid!</span>";
    }
}
