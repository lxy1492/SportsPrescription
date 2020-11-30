function uploadData(data,url) {
    var r=null;
    $.ajax({
        url:url,
        data:data,
        dataType : "json",
        async:false,
        success:function (back) {
            r = back
        }
    });
    return r
}

function checklogIn() {
    var s = false;
    id = localStorage.getItem("id");
    status = localStorage.getItem("statusCode");
    data = {
        "re":"checkLogStatus",
        "id":id,
        "status":status,
    };
    r = uploadData(data,"/user/sigIn/");
    if (r!=null){
        if(r["status"]=="success"){
            s = true
        }else{
            // window.location.href="/user/sigIn/";
        }
    }
    return s
}