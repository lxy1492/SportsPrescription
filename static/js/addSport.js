
function setEffect(id) {
    c = $(id).is(":checked");
    var status = c;
    var name = $("#inputName").val();
    var val = $(id).data("effect");
    data = {"re":"setEffect","type":status,"name":name,"target":val};
    // console.log(data);
    $.ajax({
        url:"/prescription/sportsList.html/",
        data:data,
        dataType:"json",
        success:function (data) {
            if (data['status']=="success"){
                setEffectCheckStatus(data["result"]["effect"]);
            }else{
                alert(data["info"]);
            }
        }
    });
}

function setTarget(id) {
    c = $(id).is(":checked");
    var status = c;
    var name = $("#inputName").val();
    var val = $(id).data("target");
    data = {"re":"setTarget","type":status,"name":name,"target":val};
    // console.log(data);
    $.ajax({
        url:"/prescription/sportsList.html/",
        data:data,
        dataType:"json",
        success:function (data) {
            // console.log(data);
            if (data['status']=="success"){
                setTargetCheckStatus(data["result"]["target"]);
            }else{
                alert(data["info"]);
            }
        }
    });
}


function setEffectCheckStatus(e) {
    var inputs = document.getElementsByClassName("checkEffect");
    for(var i=0;i<inputs.length;i++){
        var val = inputs[i].getAttribute("data-effect");
        if (e.indexOf(val)>=0){
            // inputs[i].setAttribute("checked","checked");
            $(inputs[i]).prop("checked",true);
        }else{
            // inputs[i].removeAttribute("checked");
            $(inputs[i]).prop("checked",false);
        }
    }
}

function setTargetCheckStatus(e) {
    var inputs = document.getElementsByClassName("checkTarget");
    for(var i=0;i<inputs.length;i++){
        var val = inputs[i].getAttribute("data-target");
        if (e.indexOf(val)>=0){
            // inputs[i].setAttribute("checked","checked");
            $(inputs[i]).prop("checked",true);
        }else{
            // inputs[i].removeAttribute("checked");
            $(inputs[i]).prop("checked",false);
        }
    }
}
