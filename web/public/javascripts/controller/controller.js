//"use strict";

var app = angular.module('main', ['ngRoute', 'MyService']);
app.controller('MainCtrl', ['$scope', '$']);
app.controller('LogCtrl', ['$scope', 'RegistService', 'LogService',
    function ($scope, $rootScope, LogService) {
        $rootScope.web = '登录 - LoveU 账户';
        $scope.user =LogService.setUser();
        $scope.msg=LogService.setMsg();
        $scope.login = function () {
            LogService.login($scope.user).success(function (data) {
                setCookie('key', data.SecretKey);
            }).error(function (msg) {
                $scope.msg.text = msg;
            })
        }
    }]);
app.controller('RegCtrl',['$scope','RegistService',function ($scope,RegistService) {
    $scope.msg=RegistService.setError();
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
    })
}]);
