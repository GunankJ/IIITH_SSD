function passwordHandler() {
    var password = document.getElementById('svrpass').value;
    var cfmpassword = document.getElementById('cfmpass').value;
    console.log("pass called");
    if(password != cfmpassword){
        alert("Please enter matching password in confirm password field.");
        return false;
    }else
        return true;
}

function usernameValidationHandler() {
    var usrName = document.getElementById("svrname").value;
    var number = /[0-9]/.test(usrName);
    var upperCase = /[A-Z]/.test(usrName);

    if(number && upperCase)
        document.getElementById("err-usrname").innerHTML = "";
    else
        document.getElementById("err-usrname").innerHTML = "Username must contain at least one Uppercase and at least one Numeric character";
        
}

function dragstartHandler(event){
    event.dataTransfer.setData("MyDraggedElementId", event.target.id);
}

function dragoverHandler(event){
    event.preventDefault();
}

function dropHandler(event){
    event.preventDefault();

    var memberId = event.dataTransfer.getData("MyDraggedElementId");
    event.target.appendChild(document.getElementById(memberId));
}