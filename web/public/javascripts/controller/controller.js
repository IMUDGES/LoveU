//"use strict";

var app = angular.module('main', ['ngRoute', 'ngImgCrop', 'MyService', 'directs']);
app.controller('Navctrl', ['$scope', 'SecretKey', '$interval', '$timeout', '$location',
    function ($scope, SecretKey, $interval, $timeout, $location) {
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
        $scope.logout = function () {
            SecretKey.destory();
            $scope.change();
            $location.path('/');
        }
    }]);
app.controller('MainCtrl', ['$scope', '$rootScope', '$location', function ($scope, $rootScope, $location) {
    $rootScope.web = 'LoveU | 主页';
    $scope.tofood = function () {
        $location.path('/food');
    };
    $scope.torun = function () {
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
                    $location.path('/');
                }
                else {
                    $scope.msg.ifshow = true;
                    $scope.msg.text = data.msg;
                }
            }).error(function (msg) {
                $scope.msg.ifshow = true;
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
app.controller('ProfileCtrl', ['$scope', '$rootScope', 'data', 'ProfileService', function ($scope, $rootScope, data, ProfileService) {
    $scope.data = data;
    $rootScope.web = data.NickName + '的个人中心';
    data.NickNameCopy = data.NickName;
    $scope.msg = ProfileService.SetMsg();
    $scope.form = ProfileService.SetForm();
    /*基础信息部分*/
    $scope.update = function () {
        ProfileService.Update($scope.data).error(function (msg) {
            alert(msg);
        })
    };
    $scope.ChangeAvatar = function () {
        $scope.msg.ifavatar = true;
    };
    $scope.file = function () {
        $('#fileInput').click();
    };
    $scope.upload = function () {
        ProfileService.SetAvatar($scope.myCroppedImage).success(function (msg) {
            if (msg.state == '1') {
                $scope.data.UserPhoto = $scope.myCroppedImage;
                $scope.msg = ProfileService.SetMsg();
            }
        })
    };
    $scope.myImage = '';
    $scope.myCroppedImage = '';
    var handleFileSelect = function (evt) {
        var file = evt.currentTarget.files[0];
        var reader = new FileReader();
        reader.onload = function (evt) {
            $scope.$apply(function ($scope) {
                $scope.myImage = evt.target.result;
                $scope.msg.croped = true;
            });
        };
        reader.readAsDataURL(file);
    };
    angular.element(document.querySelector('#fileInput')).on('change', handleFileSelect);
    /*教务系统部分*/
    $scope.jwxt = function () {
        ProfileService.Jwxt($scope.form).success(function (data) {
            location.reload();
            $scope.data.isjwxt = true;
        }).error(function (msg) {
            $scope.msg.jwxt = msg;
        })
    };
    /*钱包部分*/
    $scope.charge = function () {
        ProfileService.Charge($scope.form).success(function () {
            $scope.data.money = parseInt($scope.form.Money) + parseInt($scope.data.money);
            $scope.form.Money = '';
            $scope.msg.ifpay = false;
        }).error(function (msg) {
            $scope.msg.pay = msg;
            $scope.msg.ifpay = true;
        });
    };
    $scope.GetVcode = function () {
        ProfileService.GetVcode();
    };
    $scope.SetPass = function () {
        ProfileService.CreatPay($scope.form).success(function () {
            location.reload();
        }).error(function (msg) {
            $scope.msg.pay = msg;
            $scope.msg.ifpay = true;
        });
    }
}]);

app.controller('FoodCtrl', ['$scope', '$rootScope', 'foodlist', 'FoodService', function ($scope, $rootScope, foodlist, FoodService) {
    $rootScope.web = 'LoveU - food';
    $scope.list = foodlist.fooddata;
    //翻页部分
    $scope.page = FoodService.SetPage();
    if(parseInt(foodlist.num)!=10){
        $scope.page.Old=false;
    }
    $scope.ifpage = function (bool) {
        if (bool) return 'btn-click';
        else return 'btn-default';
    };
    $scope.ifLast = function () {
        if ($scope.page.Last) return "更新的";
        else return "已显示最新消息";
    };
    $scope.ifOld = function () {
        if ($scope.page.Old) return "更早的";
        else return "没有更多的消息了";
    };
    $scope.LastPage = function () {
        if (parseInt($scope.page.Num)!=1) {
            $scope.page.Num = parseInt($scope.page.Num) -1;
            if(parseInt($scope.page.Num)==1){
                $scope.page.Last=false;
            }
            FoodService.foodlist($scope.page.Num).success(function (data) {
                $scope.list=data.fooddata;
                $scope.page.Old=true;
            });
            $("html,body").animate({scrollTop:0},100);
        }
    };
    $scope.OldPage = function () {
        if ($scope.page.Old) {
            $scope.page.Num = parseInt($scope.page.Num) +1;
            FoodService.foodlist($scope.page.Num).success(function (data) {
                $scope.page.Last=true;
                $scope.list=data.fooddata;
                if(parseInt(data.num)!=10){
                    $scope.page.Old=false;
                }
            }).error(function (msg) {
                alert(msg);
            });
            $("html,body").animate({scrollTop:0},100);
        }
    };

    $scope.accept = function (index) {
        alert($scope.list[index].FoodId);
    };
    $scope.person={};
    $scope.SexInfo= function (bool) {
        if(bool==1) return "♂";
        if(bool==2) return '♀';
        else return 'Hiden';
    };
    $scope.more= function (index) {
        FoodService.GetOtherData($scope.list[index].UserId).success(function (data) {
            $scope.person=data.data;
            $scope.data=$scope.list[index];
            $('#myModal').modal('toggle');
        });

    }
    $scope.accept= function () {
        alert("sd");
    }
}]);
app.controller('RunCtrl', ['$scope', '$rootScope', 'runlist', function ($scope, $rootScope, runlist) {
    $rootScope.web = 'LoveU - run';
    $scope.list = runlist;
}]);
app.controller('AuctionCtrl', ['$scope', '$rootScope', 'auctionlist', function ($scope, $rootScope, auctionlist) {
    $rootScope.web = 'LoveU - auction';
    $scope.list = auctionlist;
}]);

app.controller('TestCtrl', function ($scope, $http) {
    $scope.myImage = '';
    $scope.myCroppedImage = '';
    $scope.testImage = '';
    var dataURItoBlob = function (dataURI) {
        var binary = atob(dataURI.split(',')[1]);
        var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
        var array = [];
        for (var i = 0; i < binary.length; i++) {
            array.push(binary.charCodeAt(i));
        }
        return new Blob([new Uint8Array(array)], {type: mimeString});
    };
    var formDataObject = function (data) {
        var fd = new FormData();
        angular.forEach(data, function (value, key) {
            fd.append(key, value);
        });
        return fd;
    };
    $scope.upload = function () {
        var blob = dataURItoBlob($scope.myCroppedImage);
        $http({
            method: 'POST',
            url: 'http://183.175.12.178:5000/test',
            headers: {
                'Content-Type': undefined
            },
            data: {
                file: blob
            },
            transformRequest: formDataObject
        })
    };
    var handleFileSelect = function (evt) {
        var file = evt.currentTarget.files[0];
        var reader = new FileReader();
        reader.onload = function (evt) {
            $scope.$apply(function ($scope) {
                $scope.myImage = evt.target.result;
            });
        };
        reader.readAsDataURL(file);
    };
    angular.element(document.querySelector('#fileInput')).on('change', handleFileSelect);
});


app.config(['$routeProvider', function ($routeProvider, $scope) {
    $routeProvider.when('/', {
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
    }).when('/profile', {
            templateUrl: 'views/profile.html',
            controller: 'ProfileCtrl',
            resolve: {
                data: ['ProfileService', '$location', function (ProfileService, $location) {
                    return ProfileService.GetData().success(function (data) {
                        return data;
                    }).error(function (data) {
                        if (data == 'error') {
                            alert('验证用户失败，请重新登录');
                            $location.path('/login');
                        }
                    })
                }]
            }
        })
        .when('/food', {
            controller: 'FoodCtrl',
            templateUrl: 'views/food.html',
            resolve: {
                foodlist: ['FoodService', '$location', function (FoodService, $location) {
                    return FoodService.foodlist(1).success(function (data) {
                        return data;
                    }).error(function (status) {
                        alert(status);
                        $location.path('/');
                    })
                }]
            }
        }).when('/run', {
        templateUrl: 'views/run.html',
        controller: 'RunCtrl',
        resolve: {
            runlist: ['RunService', function (RunService) {
                return RunService.runlist();
            }]
        }
    }).when('/auction', {
            templateUrl: 'views/auction.html',
            controller: 'AuctionCtrl',
            resolve: {
                auctionlist: ['AuctionService', function (AuctionService) {
                    return AuctionService.auctionlist();
                }]
            }
        })
        .when('/test', {
            controller: 'TestCtrl',
            templateUrl: "views/test.html"
        })
}]);
