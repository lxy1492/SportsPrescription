function getCourse(name) {
    data = {"re":"getCoursesList","name":name};
    var r=null;
    $.ajax({
        url:"/prescription/coursesList.html/",
        dataType:"json",
        data:data,
        async:false,
        success:function (data) {
            if(data["status"]=="success"){
                r = data["result"];
            }else{
                alert(data["info"]);
            }
        }
    });
    return r;
}

function getCoursesList() {
    obj_ = $(".selectCourse").val();
    // console.log(obj_);
    var data = getCourse(obj_);
    // console.log(data);
    var description = document.createElement("p");
    description.innerText = data["description"];
    // var difficulty = document.createElement("p");
    // difficulty.innerText = data["difficulty"];
    select = document.createElement("select");
    select.id = "select_Sport";
    select.setAttribute("onchange","selectSport()");
    for(var i=0;i<data["Sports"].length;i++){
        op = document.createElement("option");
        t = document.createElement("p");
        t.className = "selectP";
        t.innerText = data["Sports"][i]["name"];
        op.appendChild(t);
        select.appendChild(op);
    }
    $(".selectSports").empty();
    $('.selectSports').append(select);
    $(".descriptionP").empty();
    $('.descriptionP').append(description);
    $(".difficultyP").text("难度指数："+data["difficulty"]);
    $(".effectAndtarget").fadeIn();
    selectSport();
}