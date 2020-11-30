function sign_up() {
    index = $("#signUPIndex").val();
    username = $("#signUPName").val();
    password1 = $("#signUPPassword1").val();
    password2 = $("#signUPPassword2").val();
    // console.log(index,username,password1,password2);
    if (password2!=password1){
        $("#signUpDetail").text("密码不一致");
    }else{
        data = {
            "re":"SigUp",
            "name":username,
            "index":index,
            "password":password1,
        };
        r = uploadData(data);
        if (r!=null){
            if (r["status"]=="success"){
                console.log(r);
                localStorage.setItem('id',r["result"]["id"]);
                localStorage.setItem("statusCode",r["result"]["statusCode"]);
                $("#signUpDetail").text("注册成功！");
                window.location.href = '/';
        }else{
            $("#signUpDetail").text(r["info"]);
        }
        }

    }
}