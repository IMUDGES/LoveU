$(document).ready(function () {
    clearCookie('username');
    clearCookie('userid');
    var url = '../PHP/Service/UserService/Login.php';
    $(document).keydown(function(e){
        var curKey = e.which;
        if(curKey == 13){
            $("#login").click();
        }
    });
    $("#login").click(function () {
        var username = $("#username").val();
        var password = $("#password").val();
        $.post(url, {
            username: username,
            password: password
        }, function (data, status) {
            if (data[0] == '1') {
                var url = '../PHP/Service/UserService/Session.php';
                $.getJSON(url, function (data) {
                    var id =data.userid;
                    var name=data.username;
                    setCookie('username',name);
                    setCookie('userid',id);
                    location.href='../index.html';
                });
            }
            else {
                var msg = '<p>' + data + '</p>';
                $("#wrong").innerHTML = msg;
                document.getElementById('wrong').innerHTML = msg;
                $("#alert").click();
            }
        });
    });
});