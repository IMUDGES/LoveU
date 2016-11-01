function comment(avatar, nickname, msg, userid) {
    var data;
    if (CheckUser()) {
        data = '<div class="comment">'
            + '<div class="col-lg-2 col-md-2 col-sm-2 col-xs-2">'
            + '<img src="' + avatar + '"> </div>'
            + '<div class="col-lg-2 col-md-2 col-sm-2 col-xs-2">'
            + '<p class="big"> ' + nickname + '</div>'
            + '<div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">'
            + '<p class="big" >' + msg + '</p></div>'
            + '<div class="col-lg-2  col-md-2 col-sm-2 col-xs-2 send">'
            + '<button class="btn btn-info big" onclick="send(this)">送给Ta</button>'
            + '<p class="hidden">' + userid + '</p>'
            + '</div> </div>';
    }
    else {
        data = '<div class="comment">'
            + '<div class="col-lg-2 col-md-2 col-sm-2 col-xs-2">'
            + '<img src="' + avatar + '"> </div>'
            + '<div class="col-lg-2 col-md-2 col-sm-2 col-xs-2">'
            + '<p class="big"> ' + nickname + '</div>'
            + '<div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">'
            + '<p class="big" >' + msg + '</p></div>'
            + '</div> '
            + '<p class="hidden">' + userid + '</p>';
    }
    return data;
}

function details(page) {
    var url = '../../PHP/Service/GiveService/GetComment.php';
    var id = getCookie('master');
    $.getJSON(url, {
        page: page,
        giveid: id
    }, function (data) {
        var num = data.num;
        var sum = 0;
        var userid;
        var avatar;
        var msg;
        $("#comment")[0].innerHTML = '';
        setInterval(function () {
            if (sum != num) {
                msg = data[sum].GetInformation;
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

function submit() {
    var url = '../../PHP/Service/GiveService/Get.php';
    var id = getCookie('master');
    $.post(url, {
        giveid: id,
        getinformation: $("#input-content").val()
    }, function (data) {
        if (data[0] != '1') {
            $("#word").text(data);
        }
        else {
            location.reload();
        }
    })
}

function send(obj) {
    var id = obj.nextElementSibling.innerHTML;
    var giveid = getCookie('master');
    $.post('../../PHP/Service/GiveService/Select.php', {
        giveid: giveid,
        getuser: id
    }, function (data) {
        if (data[0] == '1') {
            $("#alert").click();
        }
    })
}

function CheckUser() {
    var userid = getCookie('userid');
    var id = getCookie('masterID');
    if (userid == id) {
        $("#com").addClass('hidden');
        return 1;
    }
    else return 0;
}
