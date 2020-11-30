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