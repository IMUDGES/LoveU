function short(image, title, time, id) {
    var data = '<div class="col-lg-12 col-md-12 col-sm-12  col-xs-12 long" onclick="detail(this)">'
        + '<div class="col-lg-3  col-md-3 col-sm-3  col-xs-3">'
        + '<img class="img-thumbnail info-img" src="' + image + '"> </div>'
        + '<div class="col-lg-6  col-md-6 col-sm-6 col-xs-6"><h2  > ' + title + '</h2></div>'
        + '<div class="col-lg-3  col-md-3 col-sm-3 col-xs-3"><h3  >下架时间： ' + time + '</h3></div></div>'
        + '<p class="hidden">' + id + '</p>';
    return data;
}

function creat(avatar, nickname, time, money, msg, helpid) {
    var data = '<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 info">'
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

function detail(obj) {
    var id = obj.nextElementSibling.innerHTML;
    setCookie('master', id);
    location.href='details.html';
}

function page(page) {
    var url = '../../PHP/Service/PaiService/Page.php?page=' + page;
    $.getJSON(url, function (data, status) {
        var num = data.Num;
        var sum = 0;
        var time;
        var id;
        var image;
        var msg;
        $("#content")[0].innerHTML = '';
        setInterval(function () {
            if (sum != num) {
                image = data[sum].PaiImage;
                time = data[sum].DownTime;
                id = data[sum].PaiId;
                msg = data[sum].PaiTitle;
                msg = short(image, msg, time, id);
                $("#content")[0].innerHTML += msg;
                sum++;
            }
        }, 1);
    });
    setTimeout(function () {
        $("#loading").fadeOut();
    }, 300);
}

function show() {
    $.get('../../PHP/Service/PaiService/Total.php', function (data) {
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
            setTimeout(function () {
                location.href='../message.html';
            },800);
        }
        else {
            $("#wrong")[0].innerHTML = data;
            $("#alert").click();
        }
    })
}