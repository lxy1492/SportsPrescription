function getSport(name) {
    var s=null;
    $.ajax({
        url:"/prescription/sportsList.html/",
        data:{re:"getsport",name:name},
        dataType:"json",
        async:false,
        success:function (data) {
            // console.log(data);
            if (data["status"]=="success"){
                s = data["result"];
            }else{
                alert(data["info"]);
            }

        }
    });
    return s
}

function selectSport() {
    $(".sportInfo").empty();
    var name = $("#select_Sport").val();
    // alert(name);
    var s = getSport(name);
    // console.log(s);
    if (s!=null){
        p = document.createElement("p");
        p.className = "belong";
        var t = "";
        for(var i=0;i<s["belong"].length;i++){
            if (i>0){
                t = t+"  ;  "
            }
            t = t+s["belong"][i];
        }
        p.innerText = "所属课程："+t;
        pt = document.createElement("p");
        pt.className = 'sportsTime';
        pt.innerText = "训练时长  "+s["sportsTime"];
        detail = document.createElement("ul");
        for(var key in s["detail"]){
            if(key!="细节图示"){
                li = document.createElement("li");
                dp = document.createElement("p");
                dp.className = "detailinfo";
                t = key+"  -  "+s["detail"][key]+";";
                dp.innerText = t;
                li.appendChild(dp);
                detail.appendChild(li);
            }
        }
        div = document.createElement("div");
        div.className = "detail";
        img = document.createElement("img");
        img.className = "sportImage";
        img.setAttribute("align",'center');
        div.appendChild(p);
        div.appendChild(pt);
        div.appendChild(detail);
        if (s["image"]!=null){
                    img.setAttribute("src",s["image"]);

                }else{
            img.setAttribute("src","/static/image/needImage.jpg");
        }
        div.appendChild(img);
        $(".sportInfo").append(div);
        // console.log(s["effect"]);
        // console.log(s);
        if (s["frequency"]!=null){
            $("#frequency").val(s["frequency"]);
        }else{
            $("#frequency").val("");
        }
        if (s["strength"]!=null){
            $("#strength").val(s["strength"]);
        }else{
            $("#strength").val("");
        }
        if (s["sportsTime"]!=null){
            $("#sportTime").val(s["sportsTime"]);
        }else{
            $("#sportTime").val(s[""]);
        }
        setEffectCheckStatus(s["effect"]);
        setTargetCheckStatus(s["target"]);
    }
}


function setEffect(id) {
    c = $(id).is(":checked");
    var status = c;
    var name = $("#select_Sport").val();
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
    var name = $("#select_Sport").val();
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

function reName() {
    newName = $("#rename").val();
    oldName = $("#select_Sport").val();
    data = {"re":"rename","newname":newName,"oldname":oldName};
    $.ajax({
        url:"/prescription/sportsList.html/",
        data:data,
        dataType:"json",
        success:function (data) {
            if(data["status"]!="success"){
                            alert(data["info"]);
                        }
        }
    })
}

function setStrength() {
    strength = $("#strength").val();
    sport = $("#select_Sport").val();
    data = {"re":"setStrength","strength":strength,"sport":sport};
    $.ajax({
        url:"/prescription/sportsList.html/",
        data:data,
        dataType:"json",
        success:function (data) {
            if(data["status"]!="success"){
                alert(data["info"]);
            }
        }
    });
}

function setSportTime() {
    time_ = $("#sportTime").val();
    sport = $("#select_Sport").val();
    data = {"re":"setSportTime","time":time_,"sport":sport};
    $.ajax({
        url:"/prescription/sportsList.html/",
        data:data,
        dataType:"json",
        success:function (data) {
            if(data["status"]!="success"){
                alert(data["info"]);
            }
        }
    });
}

function setFrequency() {
    frequency = $("#frequency").val();
    sport = $("#select_Sport").val();
    data = {"re":"setFrequency","frequency":frequency,"sport":sport};
    $.ajax({
        url:"/prescription/sportsList.html/",
        data:data,
        dataType:"json",
        success:function (data) {
            if(data["status"]!="success"){
                alert(data["info"]);
            }
        }
    });
}
