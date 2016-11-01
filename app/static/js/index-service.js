function Loaded() {
    if (getCookie('userid')) {
        resetCookie();
    }
    var user = getCookie('username');
    if (user == null || user == '') {
        var msg = " <ul class=\"nav pull-right navbar-nav\" id=\"user\">" +
            " <li><a> <span class=\"glyphicon glyphicon-search\"></span></a></li>" +
            " <li><a onclick=\"location.href='../login.html'\">登录</a></li>" +
            "<li><a onclick=\"location.href='../regist.html'\">注册</a></li> </ul>";
        document.getElementById('user').innerHTML = msg;
    }
    else {
        document.getElementById('username').innerHTML = user + "<span class=\"caret\"></span>"
    }
}

function getData(data) {
    if (data == '' || data == null)
        return '';
    else  return data;
}

$(document).ready(function () {
    $("#header").headroom({
        "tolerance": 5,
        "offset": 200,
        "classes": {
            "initial": "animated",
            "pinned": "swingInX",
            "unpinned": "swingOutX"
        }
    });
    Loaded();
})