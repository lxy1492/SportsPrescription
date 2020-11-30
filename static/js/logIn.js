function logIn() {
    var index = $("#logInIndex").val();
    var password = $("#logInPassword").val();
    data = {
        "re":"logIn",
        "index":index,
        "password":password,
    };
    var r=uploadData(data,"/user/sigIn/");
    if (r!=null){
        if(r["status"]=="success"){
            id = r["result"]["id"];
            var status = r["result"]["status"];
            localStorage.setItem("id",id);
            localStorage.setItem("statusCode",status);
            window.location.href = "/";
        }else {
            $("#logInDetail").text(r["info"]);
        }
    }
}