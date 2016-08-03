//"use strict";

var app = angular.module('main', ['ngRoute', 'MyService', 'directs']);
app.controller('Navctrl', ['$scope', 'SecretKey','$interval','$timeout', function ($scope, SecretKey,$interval,$timeout) {
    $scope.iflogin = function () {
        return SecretKey.ifKey();
    };
    $scope.change = function () {
        if ($scope.elem == 'block')
            $('#collapse').click();
    };
    $timeout(function () {
        $interval(function () {
            $scope.elem = getComputedStyle(document.getElementById('collapse')).display;
        }, 500);
    }, 100);
}]);
app.controller('MainCtrl', ['$scope', '$rootScope', '$location', function ($scope, $rootScope, $location) {
    $rootScope.web = 'LoveU | 主页';
    $scope.tofood = function () {
        $location.path('/food');
    };
    $scope.torun= function () {
        $location.path('/run');
    };
    $scope.topai = function () {
        $location.path('/auction');
    };
    $scope.tosend = function () {
        $location.path('/send');
    };
    $scope.tohelp = function () {
        $location.path('/mutual');
    };
    $scope.tojwxt = function () {
        $location.path('/jwxt');
    }
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
app.controller('RegCtrl', ['$scope', 'RegistService', '$rootScope', '$location',
    function ($scope, RegistService, $rootScope, $location) {
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
        };
        $scope.check = function () {

        }
    }]);
app.controller('ScrollCtrl', ['$scope', function ($scope) {
    var myScroll;
}]);
app.controller('FoodCtrl',['$scope','$rootScope','foodlist',function ($scope, $rootScope,foodlist) {
    $rootScope.web='LoveU - food';
    $scope.list=foodlist;
    /*$scope.accept=function (index) {
        $('#btn'+foodlist[index].FoodId).click();
    }*/
}]);
app.controller('RunCtrl',['$scope','$rootScope','runlist',function ($scope,$rootScope,runlist) {
    $rootScope.web='LoveU - run';
    $scope.list=runlist;
}]);
app.controller('AuctionCtrl',['$scope','$rootScope','auctionlist',function ($scope,$rootScope,auctionlist) {
    $rootScope.web='LoveU - auction';
    $scope.list=auctionlist;
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
    }).when('/food', {
        controller: 'FoodCtrl',
        templateUrl: 'views/food.html',
        resolve:{
            foodlist:['FoodService',function (FoodService) {
                return FoodService.foodlist();
            }]
        }
    }).when('/run',{
        templateUrl:'views/run.html',
        controller:'RunCtrl',
        resolve:{
            runlist:['RunService',function (RunService) {
                return RunService.runlist();
            }]
        }
    }).when('/auction',{
        templateUrl:'views/auction.html',
        controller:'AuctionCtrl',
        resolve:{
            auctionlist:['AuctionService',function (AuctionService) {
                return AuctionService.auctionlist();
            }]
        }
    })
        .when('/test',{
        templateUrl:"views/test.html"
    })
}]);
