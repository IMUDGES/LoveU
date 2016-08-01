//"use strict";

var app = angular.module('main', ['ngRoute', 'MyService']);
app.controller('Navctrl', ['$scope', function ($scope) {
    $scope.change = function () {
        if ($scope.elem == 'block')
            $('#collapse').click();
    };
    setInterval(function () {
        $scope.elem = getComputedStyle(document.getElementById('collapse')).display;
    }, 500);
}]);
app.controller('MainCtrl', ['$scope', '$rootScope', function ($scope, $rootScope) {

}]);
app.controller('LogCtrl', ['$scope', '$location', 'LogService', '$rootScope',
    function ($scope, $location, LogService, $rootScope) {
        $rootScope.web = '登录 - LoveU 账户';
        $scope.user = LogService.setUser();
        $scope.msg = LogService.setMsg();
        $scope.login = function () {
            LogService.login($scope.user).success(function (data) {
                if (data.state == '1') {
                    setCookie('key', data.SecretKey);
                    $location.path('/');
                }
                else {
                    $scope.msg.ifshow = true;
                    $scope.msg.text = data.msg;
                }
            }).error(function (msg) {
                $scope.msg.text = msg;
            })
        }
    }]);
app.controller('RegCtrl', ['$scope', 'RegistService', '$rootScope', '$location', function ($scope, RegistService, $rootScope, $location) {
    $rootScope.web = '创建一个 LoveU 账号';
    $scope.msg = RegistService.setError();
    $scope.data = RegistService.setUser();
    $scope.vcode = function () {
        RegistService.phone($scope.data.phone).success(function (data) {
            $scope.msg.phone = data;
            $scope.msg.ifphone = false;
        }).error(function (msg) {
            $scope.msg.phone = msg;
            $scope.msg.ifphone = true;
        })
    };
    $scope.regist = function () {
        RegistService.regist($scope.data).success(function (msg) {
            $location.path('/');
        }).error(function (msg) {
            if (msg == 'phone') {
                $scope.msg.phone = "请验证手机号";
                $scope.msg.ifphone = true;
            }
            if (msg == 'pass') {
                $scope.msg.pass1 = "两次密码不一致";
                $scope.msg.ifpass1 = true;
            }
            if (msg == 'pass1') {
                $scope.msg.pass1 = "密码太短";
                $scope.msg.ifpass1 = true;
            }
            if (msg == 'pass2') {
                $scope.msg.pass1 = "密码太长";
                $scope.msg.ifpass1 = true;
            }
            if (msg == 'vcode') {
                $scope.msg.vcode = '验证码错误';
                $scope.msg.ifvcode = true;
            }
            if (msg == 'Unable') {
                alert('Unable to Connect');
            }
        })
    }
    $scope.check = function () {

    }
}]);
app.controller('ScrollCtrl', ['$scope',function ($scope) {
    var myScroll;
    myScroll = new IScroll('#wrapper', {
        mouseWheel: false,
        scrollbars: true
    });
}]);
app.config(['$routeProvider', function ($routeProvider, $scope) {
    $routeProvider
        .when('/', {
            controller: "MainCtrl",
            templateUrl: "views/main.html",
            resolve: {
                key: ["SecretKey", function (SecretKey) {
                    return SecretKey.Get();
                }]
            }
        }).when('/login', {
        controller: "LogCtrl",
        templateUrl: "views/user.login.html"
    }).when('/regist', {
        controller: 'RegCtrl',
        templateUrl: 'views/user.regist.html'
    }).when('/test', {
        controller: 'ScrollCtrl',
        templateUrl: 'views/scroll.html'
    })
}]);
