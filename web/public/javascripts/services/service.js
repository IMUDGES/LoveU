var services = angular.module('MyService', []);
var root_url = 'http://127.0.0.1:5000/';

services.factory('LoginService', ['$q', '$http',
    function ($q, $http) {
        return {
            login: function (logdata) {
                var delay = $q.defer();
                var promise=delay.promise;
                promise.success = function (fn) {
                    promise.then(fn);
                    return promise;
                };
                promise.error = function (fn) {
                    promise.then(null, fn);
                    return promise;
                };
                if(!logdata.name.length>0||!logdata.name.length<=11){
                    delay.reject('请填写正确的手机号码');
                    return promise;
                }
                if(!logdata.pass.length>0){
                    delay.reject('请填写密码');
                    return promise;
                }
                $http.post(root_url+'login', {
                    UserPhone: logdata.name,
                    PassWord: logdata.pass
                }).success(function (iflogin) {
                    delay.resolve(iflogin);
                }).error(function () {
                    delay.reject('Unable to connect');
                });
                return promise;
            }
        }
    }
]);
services.factory('SecretKey',[function () {
    var key='';
    return{
        Set:function (value) {
            key=value;
        },
        Get:function () {
            key=getCookie('key');
            return key;
        }
    }
}]);

