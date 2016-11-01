function creat(nickname, avatar, datetime, place, msg, id) {
    var data;
    data = '<div class="col-lg-6 col-md-12 col-sm-12  col-xs-12 info">'
        + '<div class="col-lg-4  col-md-6 col-sm-6 col-xs-6">'
        + '<img class="img-thumbnail info-img" ' + 'src="' + avatar + '"></div>'
        + '<div class="col-lg-4 col-md-6 col-sm-6 col-xs-6"><h2 class="text-center">' + nickname + '</h2></div>'
        + '<div class="col-lg-4 col-md-6 col-sm-6 col-xs-6">'
        + '<h2 class="text-center">' + datetime + '</h2>'
        + '</div>'
        + '<div class="col-lg-4 col-md-6 col-sm-6 col-xs-6">'
        + '<h2 class="text-center">' + place + '</h2>'
        + '</div>'
        + '<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">'
        + '<h3 class="text-center">' + msg + '</h3>'
        + ' <button class="btn btn-info big pull-right" onclick="date(this)">约</button>'
        + '<p class="hidden">' + id + '</p>'
        + '</div></div>';
    return data;
}

function date(obj) {
    var runid = obj.nextElementSibling.innerHTML;
    var url = '../../PHP/Service/RunService/appoint.php';
    $.post(url, {
        runid: runid
    }, function (data) {
        $("#wrong")[0].innerHTML = data;
        $("#alert").click();
    });
}

function show() {
    var sum = 1;
    var num = 1;
    var choose = getCookie('choose');
    if (choose == 'run') {
        $.get('../../PHP/Service/RunService/Total.php', function (data) {
            show1(1);
            if (data[0] != '1') {
                $("#more").removeClass('hidden');
                num = data;
            }
            else {
                $("#more").addClass('hidden');
            }
        });
    }
    else {
        $.get('../../PHP/Service/XueService/Total.php', function (data) {
            show2(1);
            if (data[0] != '1') {
                $("#more").removeClass('hidden');
                num = data;
            }
            else {
                $("#more").addClass('hidden');
            }
        });
    }
    setTimeout(function () {
        $("#loading").fadeOut();
    }, 300);
}

function show1(page) {
    var url = '../../PHP/Service/RunService/Page.php?page=' + page;
    $.ajaxSetup({
        async: false
    });
    $.getJSON(url, function (data, status) {
        var num = data.Num;
        var sum = 0;
        var datetime;
        var msg;
        var userid;
        var runid;
        var place;
        $("#content")[0].innerHTML = '';
        setInterval(function () {
            if (sum != num) {
                userid = data[sum].UserId;
                datetime = data[sum].RunTime;
                place = data[sum].RunArea;
                msg = data[sum].RunInformation;
                runid = data[sum].RunId;
                url = '../../PHP/Service/UserService/GetData.php?userid=' + data[sum].UserId;
                $.getJSON(url, function (data2) {
                    msg = creat(data2.NickName, data2.UserPhoto, datetime, place, msg, runid);
                    $("#content")[0].innerHTML += msg;
                });
                sum++;
            }
        }, 1);
    });
}

function show2(page) {
    var url = '../../PHP/Service/XueService/Page.php?page=' + page;
    $.ajaxSetup({
        async: false
    });
    $.getJSON(url, function (data, status) {
        var num = data.Num;
        var sum = 0;
        var datetime;
        var msg;
        var place;
        var userid;
        var xueid;
        $("#content2")[0].innerHTML = '';
        setInterval(function () {
            if (sum != num) {
                userid = data[sum].UserId;
                datetime = data[sum].XueTime;
                msg = data[sum].XueInformation;
                place = data[sum].XueArea;
                xueid = data[sum].XueId;
                url = '../../PHP/Service/UserService/GetData.php?userid=' + data[sum].UserId;
                $.getJSON(url, function (data2) {
                    msg = creat(data2.NickName, data2.UserPhoto, datetime, place, msg, xueid);
                    $("#content2")[0].innerHTML += msg;
                });
                sum++;
            }
        }, 1)
    });
}

function submit() {
    var choose = getCookie('choose');
    var url;
    var msg;
    var datetime;
    var place;
    msg = $("#input-content").val();
    var reg = new RegExp("\n", "g");
    msg = msg.replace(reg, '；');
    datetime = $("#datetime").val();
    place = $("#dateplace").val();
    datetime += ':00';
    if (choose == 'run') {
        url = '../../PHP/Service/RunService/Create.php';
        $.post('../../PHP/Service/RunService/Create.php', {
            runtime: datetime,
            runinformation: msg,
            runarea: place
        }, function (data) {
            if (data[0] == '1') {
                setTimeout(function () {
                    location.href = '../message.html';
                }, 800);
            }
            else {
                $("#word").text(data);
            }
        });
    }
    else {
        url = '../../PHP/Service/XueService/Create.php';
        $.post(url, {
            xuetime: datetime,
            xueinformation: msg,
            xuearea: place
        }, function (data) {
            if (data[0] == '1')
                location.reload();
            else {
                $("#word").text(data);
            }
        });
    }
}

