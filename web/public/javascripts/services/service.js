var services = angular.module('MyService', []);
var root_url = 'http://127.0.0.1:5000/';

services.factory('LoginService', ['$q', '$http',
    function ($q, $http) {
        return {
            login: function (logdata) {
                var delay = $q.defer();
                if (logdata.user.length == 0)
                    delay.reject('用户名不能留空');
                if (logdata.pass.length == 0)
                    delay.reject('密码不能留空');
                $http.post(root_url+'login').success(function (iflogin) {
                        delay.resolve(iflogin);
                    }
                ).error(function () {
                    delay.reject('Unable to connect');
                })
            }
        }
    }
]);

