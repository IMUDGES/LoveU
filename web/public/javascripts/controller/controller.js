//"use strict";

var app = angular.module('main', ['ngRoute', 'MyService']);
app.controller('Navctrl',['$scope',function ($scope) {
    $scope.change=function () {
        if($scope.elem=='block')
        $('#collapse').click();
    };
    setInterval(function () {
        $scope.elem=getComputedStyle(document.getElementById('collapse')).display;
    },500);
}]);
app.controller('MainCtrl', ['$scope', '$']);
app.controller('LogCtrl', ['$scope', 'RegistService', 'LogService',
    function ($scope, $rootScope, LogService) {
        $rootScope.web = '登录 - LoveU 账户';
        $scope.user =LogService.setUser();
        $scope.msg=LogService.setMsg();
        $scope.login = function () {
            LogService.login($scope.user).success(function (data) {
                if(data.state=='1')
                setCookie('key', data.SecretKey);
                else {
                    $scope.msg.ifshow=true;
                    $scope.msg.text=data.msg;
                }
            }).error(function (msg) {
                $scope.msg.text = msg;
            })
        }
    }]);
app.controller('RegCtrl',['$scope','RegistService',function ($scope,RegistService) {
    $scope.msg=RegistService.setError();
    $scope.data=RegistService.setUser();
    $scope.vcode=function () {
        RegistService.phone($scope.data.phone).error(function (msg) {

        })
    }
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
    }).when('/regist',{
        controller:'RegCtrl',
        templateUrl:'views/user.regist.html'
    }).when('/test',{
        templateUrl:'views/scroll.html'
    })
}]);
