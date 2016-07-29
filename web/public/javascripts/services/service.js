var services = angular.module('MyService', []);
var root_url = 'http://183.175.12.178:5000/';

services.factory('LogService', ['$q', '$http',
    function ($q, $http) {
        return {
            login: function (logdata) {
                var delay = $q.defer();
                var promise = delay.promise;
                promise.success = function (fn) {
                    promise.then(fn);
                    return promise;
                };
                promise.error = function (fn) {
                    promise.then(null, fn);
                    return promise;
                };
                if (logdata.name.length != 11) {
                    delay.reject('请填写正确的手机号码');
                    return promise;
                }
                if (!logdata.pass.length > 0) {
                    delay.reject('请填写密码');
                    return promise;
                }
                $http.post(root_url + 'login', {
                    UserPhone: logdata.name,
                    PassWord: md5_s(logdata.pass)
                }).success(function (iflogin) {
                    delay.resolve(iflogin);
                }).error(function () {
                    delay.reject('Unable to connect');
                });
                return promise;
            },
            setUser: function () {
                return {
                    name: '',
                    pass: ''
                };
            },
            setMsg: function () {
                return {
                    ifshow: true,
                    text: '测试'
                };
            }
        }
    }
]);
services.factory('RegistService', ['$q', '$http',
    function ($q, $http) {
        var phone = '';
        var code=false;
        return {
            regist: function (regdata) {
                var delay = $q.defer();
                var promise = delay.promise;
                promise.success = function (fn) {
                    promise.then(fn);
                    return promise;
                };
                promise.error = function (fn) {
                    promise.then(null, fn);
                    return promise;
                };
                this.phone(regdata.phone).success(function () {
                    $http.post(root_url + 'register3', {}).success(function (data) {

                    });
                }).error()
            },
            phone: function (number) {
                var delay = $q.defer();
                var promise = delay.promise;
                promise.success = function (fn) {
                    promise.then(fn);
                    return promise;
                };
                promise.error = function (fn) {
                    promise.then(null, fn);
                    return promise;
                };
                $http.post(root_url + 'register1', {}).success(function (data) {
                    if (data.msg == '1') {
                        phone = number;
                        delay.resolve(phone);
                    }
                    else if (data.msg == '2')
                        delay.reject('手机号已被注册');
                    else
                        delay.reject("验证手机号失败");
                    return promise;
                })
            },
            setError: function () {
                return {
                    ifphone: false,
                    phone: '测试msg',
                    ifvcode: false,
                    vcode: '验证码错误',
                    ifpass: false,
                    pass: '密码长度错误',
                    ifpass1: false,
                    pass1: '两次密码不一致'
                }
            }
        }
    }]);
services.factory('SecretKey', [function () {
    var key = '';
    return {
        Set: function (value) {
            key = value;
        },
        Get: function () {
            key = getCookie('key');
            return getCookie('key');
        }
    }
}]);

