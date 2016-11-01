function setCookie(name, value, expiredays) {
    var c_time = new Date();
    c_time.setDate(c_time.getDate() + expiredays);
    document.cookie = name + '=' + escape(value) + ((expiredays == null) ?
            "" : ";expires=" + c_time.toUTCString()) + ";path=/";
}

function getCookie(name) {
    if (document.cookie.length > 0) {
        var c_start = document.cookie.indexOf(name + '=');
        if (c_start != -1) {
            c_start += name.length + 1;
            var c_end = document.cookie.indexOf(';', c_start);
            if (c_end == -1)
                c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return '';
}

function  clearCookie(name){
    setCookie(name,'',-1);
}

function resetCookie(){
    var url = 'http://loveu.iheshulin.com:9999/LoveUniversity/PHP/Service/UserService/Session.php';
    $.getJSON(url, function (data) {
        var id=data.userid;
         var id_0= getCookie('userid');
        if(id_0!=id){
            alert("Watch Out!!");
            setCookie('userid',id);
        }
        setCookie('userid',id);
        setCookie('username',data.username);
    })
}

function logOut() {
    clearCookie('username');
    clearCookie('userid');
   // url = 'http://loveu.iheshulin.com:9999/LoveUniversity/PHP/Service/UserService/Logout.php';
    url='http://127.0.0.1/LoveUniversity/PHP/Service/UserService/Logout.php';
    $.get(url);
    location.reload();
}


function getData(data) {
    if (data == '' || data == null)
        return '';
    else  return data;
}