function creat(avator, nickname, place, datetime, msg, id, deal) {
    var msg = '<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 info">'
        + '<div class="col-lg-4  col-md-4 col-sm-4">'
        + '<img class="img-thumbnail info-img"'
        + 'src="' + avator + '"></div>'
        + '<div class="col-lg-4  col-md-4 col-sm-4 col-xs-4"><h2 class="text-center" id="nickname"> ' + nickname + '</h2></div>'
        + '<div class="col-lg-4  col-md-4 col-sm-4 col-xs-4"><h2 class="text-center" id="place"> ' + place + ' </h2></div>'
        + '<div class="col-lg-4  col-md-4 col-sm-4 col-xs-4"><h2 class="text-center" id="deal"> ' + deal + '</h2></div>'
        + '<div class="col-lg-4  col-md-4 col-sm-4 col-xs-4"><h2 class="text-center" id="datetime"> ' + datetime + ' </h2></div>'
        + '<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12"><h2 class="text-center" id="msg">' + msg + '</h2></div>'
        + '<button class="btn btn-info pull-right big" onclick="date(this)">约</button>'
        + '<p class="hidden" >'+id+'</p> </div>';
    return msg;
}

function date(obj) {
    var foodid = obj.nextElementSibling.innerHTML;
    var url = '../../PHP/Service/FoodService/appoint.php';
    $.post(url, {
        foodid: foodid
    }, function (data) {
        $("#wrong")[0].innerHTML = data;
        $("#alert").click();
    });
}

function submit() {
    var url = '../../PHP/Service/FoodService/Create.php';
    var place = $("#dateplace").val();
    var deal = getData($('input[name="deal"]:checked').val());
    var msg = $("#input-content").val();
    var datetime = $(".form_datetime").val() + ':00';
    var reg = new RegExp("\n", "g");
    msg = msg.replace(reg, '；');
    $.post(url, {
        foodarea: place,
        foodway: deal,
        foodinformation: msg,
        foodtime: datetime
    }, function (data) {
        if (data[0] == '1') {
            setTimeout(function () {
                location.href='../message.html';
            },800);
        }
        else $("#word").text(data);
    })
}

function more(obj) {
    var ms = obj.nextElementSibling.innerHTML;
    setCookie('foodpage', ms);
    location.href = 'foodpage.html';
}

function page(page) {
    var url = '../../PHP/Service/FoodService/Page.php?page=' + page;
    $.ajaxSetup({
        async: false
    });
    $.getJSON(url, function (data, status) {
        var num = data.Num;
        var sum = 0;
        var datetime;
        var userid;
        var foodid;
        var place;
        var deal;
        var msg;
         $("#content")[0].innerHTML = '';
        setInterval(function () {
            if (sum != num) {
                userid = data[sum].UserId;
                datetime = data[sum].FoodTime;
                place = data[sum].FoodArea;
                foodid = data[sum].FoodId;
                deal = data[sum].FoodWay;
                msg = data[sum].FoodInformation;
                url = '../../PHP/Service/UserService/GetData.php?userid=' + data[sum].UserId;
                $.getJSON(url, function (data2) {
                    msg = creat(data2.UserPhoto, data2.NickName, place, datetime, msg, foodid, deal);
                    $("#content")[0].innerHTML += msg;
                });
                sum++;
            }
        }, 1);
    });
    setTimeout(function () {
        $("#loading").fadeOut();
    },300);
}

function show() {
    $.get('../../PHP/Service/FoodService/Total.php', function (data) {
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

