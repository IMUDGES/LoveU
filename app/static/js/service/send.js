function creat(nickname, avatar, msg, id) {
    var data = '<div class="col-lg-12 col-md-12 col-sm-12  col-xs-12 long" onclick="detail(this)">'
        + '<div class="col-lg-3 col-md-3 col-sm-3  col-xs-3 ">'
        + '<img class="info-img img-thumbnail" src="' + avatar + '"></div>'
        + '<div class="col-lg-2 col-md-2 col-sm-2   col-xs-2 text-center">'
        + '<h2 class="text-center">' + nickname + '</h2></div>'
        + '<div class="col-lg-7 col-md-7 col-sm-7  col-xs-7 ">'
        + '<h2 class="text-center">' + msg + '</h2></div></div>'
        + '<p class="hidden">' + id + '</p>';
    return data;
}

function show(page){
    var url='../../PHP/Service/GiveService/Page.php?page='+page;
    $.ajaxSetup({
        async: false
    });
    $.getJSON(url, function (data) {
        var num=data.Num;
        var sum=0;
        var userid;
        var nickname;
        var avator;
        var msg;
        var id;
        $("#content")[0].innerHTML='';
        setInterval(function () {
            if(sum!=num){
                id=data[sum].GiveId;
                msg=data[sum].GiveInformation;
                userid=data[sum].UserId;
                avator=data[sum].GiveImage;
                url = '../../PHP/Service/UserService/GetData.php?userid=' + data[sum].UserId;
                $.getJSON(url, function (data2) {
                    msg = creat(data2.NickName, avator, msg, id);
                    $("#content")[0].innerHTML += msg;
                });
                sum++;
            }
        },1);
    })
}

function page(){
    var sum = 1;
    var num = 1;
    $.get('../../PHP/Service/GiveService/Total.php', function (data) {
        show(1);
        if (data[0] != '1') {
            $("#more").removeClass('hidden');
            num = data;
        }
        else {
            $("#more").addClass('hidden');
        }
    });
}

function photo() {
    $("#file0").change(function () {
        setCookie('status', '1');
        var objUrl = getObjectURL(this.files[0]);
        console.log("objUrl = " + objUrl);
        if (objUrl) {
            $("#img0").attr("src", objUrl);
        }
        // $("#file0").slideUp('fast');
        //$("#img0").slideDown('fast');
    });
    //建立一個可存取到該file的url
    function getObjectURL(file) {
        var url = null;
        if (window.createObjectURL != undefined) { // basic
            url = window.createObjectURL(file);
        } else if (window.URL != undefined) { // mozilla(firefox)
            url = window.URL.createObjectURL(file);
        } else if (window.webkitURL != undefined) { // webkit or chrome
            url = window.webkitURL.createObjectURL(file);
        }
        return url;
    }
}

function detail(obj){
    var id=obj.nextElementSibling.innerHTML;
    setCookie('master',id);
    location.href='details.html';
}

function submit() {
    $.post('../../PHP/Service/GiveService/Create.php', {
        giveinformation: $("#input-content").val()
    }, function (data) {
        if(data[0]=='1'){
            setTimeout(function () {
                location.href='../message.html';
            },800);
        }
        else
        $("#word").text(data);
    })
}

function doUpload() {
    //url
    var status = getCookie('status');
    if (status == '1') {
        var formData = new FormData($("#form1")[0]);
        $.ajax({
            url: '../../PHP/Service/GiveService/UP.php',
            type: 'POST',
            data: formData,
            async: false,
            cache: false,
            contentType: false,
            processData: false,
            success: function (data) {
                if (data == '请完善个人信息')
                    $("#word").text(data);
                else {
                    submit();
                }
            },
            error: function (returndata) {
                alert(returndata);
            }
        });
    }
}

