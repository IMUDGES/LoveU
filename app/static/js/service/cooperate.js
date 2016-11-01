function creat(avatar, nickname, time, money, msg, helpid) {
    var data = '<div class="col-lg-12 col-md-12 col-sm-12  col-xs-12 info"><br><br>'
        + '<div class="col-lg-3  col-md-3 col-sm-3 col-xs-3">'
        + '<img class="img-thumbnail info-img" src="' + avatar + '"></div>'
        + '<div class="col-lg-2  col-md-3 col-sm-3 col-xs-3"><h2 class="text-center">' + nickname + ' </h2></div>'
        + '<div class="col-lg-3  col-md-3 col-sm-3 col-xs-3"><h2 class="text-center"> ' + time + '</h2></div>'
        + '<div class="col-lg-3  col-md-3 col-sm-3 col-xs-3"><h2 class="text-center"> ' + money + ' </h2></div>'
        + ' <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">'
        + '<h2 class="text-center">' + msg + '</h2>'
        + '<button class="btn btn-info pull-right big" onclick="help(this)">帮Ta</button>'
        + '<p class="hidden">' + helpid + '</p> </div> </div>';
    return data;
}

function help(obj) {
    var helpid = obj.nextElementSibling.innerHTML;
    $.post('../../PHP/Service/HelpService/Help.php', {
        helpid: helpid
    }, function (data) {
        if (data[0] == '1') {
            $("#myModalLabel")[0].innerHTML = "成功";
            $("#wrong")[0].innerHTML = '你已经接下了这个委托';
            $("#alert").click();
            setTimeout(function () {
                location.href = '../message.html';
            }, 800);
        }
        else {
            $("#myModalLabel")[0].innerHTML = "失败";
            $("#wrong")[0].innerHTML = data;
            $("#alert").click();
        }
    })
}

function page(page) {
    var url = '../../PHP/Service/HelpService/Page.php?page=' + page;
    $.getJSON(url, function (data, status) {
        var num = data.Num;
        var sum = 0;
        var time;
        var userid;
        var helpid;
        var money;
        var msg;
        $("#content")[0].innerHTML = '';
        setInterval(function () {
            if (sum != num) {
                userid = data[sum].UserId;
                time = data[sum].DownTime;
                helpid = data[sum].HelpId;
                money = data[sum].HelpMoney;
                msg = data[sum].HelpInformation;
                url = '../../PHP/Service/UserService/GetData.php?userid=' + data[sum].UserId;
                $.getJSON(url, function (data2) {
                    msg = creat(data2.UserPhoto, data2.NickName, time, money, msg, helpid);
                    $("#content")[0].innerHTML += msg;
                });
                sum++;
            }
        }, 1);
    });
    setTimeout(function () {
        $("#loading").fadeOut();
    }, 300);
}

function show() {
    $.get('../../PHP/Service/HelpService/Total.php', function (data) {
        page(1);
        if (data[0] != '1') {
            $("#more").removeClass('hidden');
            num = data;
        }
        else {
            $("#more").addClass('hidden');
        }
    })
}

function money() {
    $("#up").click(function () {
        $("#money").val(parseInt($("#money").val()) + 1);
    });
    $("#down").click(function () {
        if (parseInt($("#money").val()) > 0) {
            $("#money").val(parseInt($("#money").val()) - 1);
        }
    });
}

function submit() {
    var url = '../../PHP/Service/HelpService/Create.php';
    var msg = $("#input-content").val();
    var money = $("#money").val();
    var time = $("#time").val() + ':00';
    var reg = new RegExp("\n", "g");
    var password = $("#paypassword").val();
    msg = msg.replace(reg, '；');
    $.post(url, {
        helpmoney: money,
        helpinformation: msg,
        paypassword: password,
        time: time
    }, function (data) {
        if (data[0] == '1') {
            location.reload();
        }
        else if (data == '请完善钱包信息') {
            location.href = '../profile.html';
        }
        else {
            $("#wrong")[0].innerHTML = data;
            $("#alert").click();
        }
    })
}