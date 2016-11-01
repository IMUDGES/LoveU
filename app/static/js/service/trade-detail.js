function money() {
    $("#up").click(function () {
        $("#Addmoney").val(parseInt($("#Addmoney").val()) + 1);
    });
    $("#down").click(function () {
        if (parseInt($("#Addmoney").val()) > 0) {
            $("#Addmoney").val(parseInt($("#Addmoney").val()) - 1);
        }
    });
}

function comment(avatar, nickname, msg, userid) {
    var data;
    data = '<div class="comment">'
        + '<div class="col-lg-2 col-xs-2">'
        + '<img src="' + avatar + '"> </div>'
        + '<div class="col-lg-2 col-xs-2">'
        + '<p class="big"> ' + nickname + '</div>'
        + '<div class="col-lg-6 col-xs-2">'
        + '<p class="big" >' + msg + '</p></div>'
        + '</div> '
        + '<p class="hidden">' + userid + '</p>';
    return data;
}

function details(page) {
    var url = '../../PHP/Service/PaiService/GetComment.php';
    var id = getCookie('master');
    $.getJSON(url, {
        page: page,
        paiid: id
    }, function (data) {
        var num = data.num;
        var sum = 0;
        var userid;
        var avatar;
        var msg;
        $("#comment")[0].innerHTML = '';
        setInterval(function () {
            if (sum != num) {
                msg = data[sum].Comment;
                userid = data[sum].UserId;
                url = '../../PHP/Service/UserService/GetData.php?userid=' + userid;
                $.getJSON(url, function (data2) {
                    avatar = data2.UserPhoto;
                    msg = comment(avatar, data2.NickName, msg, userid);
                    $("#comment")[0].innerHTML += msg;
                });
                sum++;
            }
        }, 1);
    });
    $("#loading").fadeOut();
}

function Show() {
    $.getJSON('../../PHP/Service/PaiService/Details.php', {
        paiid: getCookie('master')
    }, function (data) {
        $("#msg")[0].innerHTML = ' ' + data.PaiInformation;
        $("#img").attr('src', data.PaiImage);
        setCookie('masterID', data.UserId);
        $("#title")[0].innerHTML = data.PaiTitle;
        $("#DownTime")[0].innerHTML += data.DownTime;
        $("#money")[0].innerHTML += data.PaiMoney + '元';
        $("#Addmoney").val(parseInt(data.PaiMoney) + 1);
        var url = '../../PHP/Service/UserService/GetData.php?userid=' + data.GetUser;
        $.getJSON(url, function (data) {
            $("#GetUser")[0].innerHTML += data.NickName;
        });
        url = '../../PHP/Service/UserService/GetData.php?userid=' + data.UserId;
        $.getJSON(url, function (data) {
            $("#nickname")[0].innerHTML = data.NickName;
        });
    });
}

function submit() {
    var url = '../../PHP/Service/PaiService/comment.php';
    var id = getCookie('master');
    $.post(url, {
        paiid: id,
        comment: $("#input-content").val()
    }, function (data) {
        if (data[0] != '1') {
            $("#word").text(data);
        }
        else {
            location.reload();
        }
    })
}

