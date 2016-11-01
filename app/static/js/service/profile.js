function data() {
    var url = '../PHP/Service/UserService/Data.php';
    $.getJSON(url, function (data) {
        var Name = getData(data.PersonalData.UserName);
        document.title = Name + '的个人资料';
        if (data.PersonalData.TrueName != null && data.PersonalData.UserGrade != null && data.PersonalData.JwxtNumber != null && data.PersonalData.UserMajor != null)
            $("#user").addClass('hidden');
        $("#nickname")[0].innerHTML += data.PersonalData.NickName;
        $("#username")[0].innerHTML += Name;
        $("#truename")[0].innerHTML += getData(data.PersonalData.TrueName);
        if (getData(data.PersonalData.UserSex)[0] == '1')
            $("#sex")[0].innerHTML += '男';
        else  $("#sex")[0].innerHTML += '女';
        $("#mobile")[0].innerHTML += phone(data.PersonalData.UserPhone);
        $("#grade")[0].innerHTML += getData(data.PersonalData.UserGrade);
        $("#content")[0].innerHTML = $("#profile")[0].innerHTML;
        $("#head").attr('src', data.PersonalData.UserPhoto);
        $("#head0").attr('src', data.PersonalData.UserPhoto);
        var msg;
        if (data.sign == '0') {
            msg = '<br><br><br><br><br><br><br>'
                + '<div class="container col-lg-8 col-md-12 col-sm-12 col-xs-12 text-center">'
                + '<div class="input-group-lg  ">'
                + '<div class="input-group input-group-lg">'
                + '<span class="input-group-addon ">支付密码</span>'
                + '<input class="form-control" type="password" id="password1" placeholder="请输入6位纯数字"> </div> <br>'
                + '</div><br>'
                + ' <input class="btn btn-success big pull-right" type="button" value="提交" onclick="setPay()"></div>';
        }
        else {
            msg = '<br><br><br><br><br>'
                + '<div class="container col-lg-8 col-md-12 col-sm-12 col-xs-12 text-center">'
                + '<div class="jumbotron"><h3 id="money">我的余额：' + getData(data.money) + '</h3></div><br><br><br>'
                + '<div class="input-group-lg ">'
                + '<div class="input-group input-group-lg">'
                + '<span class="input-group-addon">原支付密码</span>'
                + '<input class="form-control" type="password" id="password1"> </div> <br>'
                + '<div class="input-group input-group-lg">'
                + '<input class="form-control" type="password" id="password2">'
                + ' <span class="input-group-addon">新支付密码</span> </div> </div><br>'
                + ' <input class="btn btn-success big pull-right" type="button" value="提交" onclick="updatepay()"></div>';
        }
        $("#payset")[0].innerHTML = msg;
    });

    function phone(val) {
        var phone;
        phone = val[0] + val[1] + val[2] + '****' + val[7] + val[8] + val[9] + val[10];
        return phone;
    }

}

function getData(data) {
    if (data == '' || data == null)
        return '';
    else  return data;
}

function improve() {
    var url = '../PHP/Service/UserService/Data.php';
    var msg;
    $.ajaxSetup({
        async: false
    });
    $.getJSON(url, function (data) {
        msg = ' <div class="container col-lg-8 col-md-12 col-sm-12 col-xs-12 text-center">'
            + '<div class="input-group-lg ">'
            + '<br><br><br><br><br><br><br>'
            + '<div class="input-group input-group-lg">'
            + '<div class="input-group-addon btn btn-default">昵称</div>'
            + '<input type="text" class="form-control nob " id="nick" value="' + data.PersonalData.NickName + '"><br> </div> <br>'
            + '<div class="input-group input-group-lg">'
            + '<input type="text" class="form-control " id="true" readonly value="' + getData(data.PersonalData.TrueName) + '">'
            + '<div class="input-group-addon btn btn-default" >姓名</div> </div> <br>'
            + '<div class="input-group input-group-lg">'
            + '<div class="input-group-addon btn btn-default">学号</div>'
            + '<input type="text" class="form-control" id="Jwxt" ><br> </div> <br>'
            + '<div class="input-group input-group-lg">'
            + '<input type="password" class="form-control" id="Jwxtpass" >'
            + '<div class="input-group-addon btn btn-default">教务系统密码</div> </div> <br><br><br><br>'
            + '<button class="btn btn-success big pull-right" id="submit" onclick="msg()">保存</button> </div> </div> </div>';
    });
    return msg;
}


function setPay() {
    var password = $("#password1").val();
    $.post('../PHP/Service/UserService/Paypassword.php', {
        paypassword: password
    }, function (data) {
        if (data[0] == '1') {
            location.reload();
        }
        else alert(data);
    });
}

function updatepay() {
    var password1 = $("#password1").val();
    var password2 = $("#password2").val();
    $.post('../PHP/Service/UserService/ModifyPaypassword.php', {
        oldpaypassword: password1,
        newpaypassword: password2
    }, function (data) {
        if (data[0] == '1') {
            location.reload();
        }
        else alert(data);
    });
}

function msg() {
    var url = '../PHP/Service/UserService/Modify.php';
    var nickname = $("#nick").val();
    var Jwxt = $("#Jwxt").val();
    var Jwxtpass = $("#Jwxtpass").val();
    $.post(url, {
        nickname: nickname,
        jwxtnumber: Jwxt,
        jwxtpassword: Jwxtpass
    }, function (data) {
        if (data[0] == '1') {
            location.reload();
        }
        else alert(data);
    });
}

$(document).ready(function () {
    $.ajaxSetup({
        async: false
    });
    $("#userInfo").click(function () {
        $("#content")[0].innerHTML = $("#profile")[0].innerHTML;
    });
    $("#userHead").click(function () {
        $("#content").load("avator.html")
    });
    $("#userData").click(function () {
        $("#content")[0].innerHTML = improve();
    });
    $("#payData").click(function () {
        $("#content")[0].innerHTML = $("#payset")[0].innerHTML;
    });
    data();
});