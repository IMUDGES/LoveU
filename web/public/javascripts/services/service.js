var services = angular.module('MyService', []);
var root_url = 'http://127.0.0.1:5000/';

services.factory('LoginService', ['$q', '$http',
    function ($q, $http) {
        return {
            login: function (logdata) {
                var delay = $q.defer();
                var promise=delay.promise;
                $http.post(root_url+'login', {
                    UserPhone: logdata.name,
                    PassWord: logdata.pass
                }).success(function (iflogin) {
                    delay.resolve(iflogin);
                }).error(function () {
                    delay.reject('Unable to connect');
                });
                promise.success = function (fn) {
                    promise.then(fn);
                    return promise;
                };
                promise.error = function (fn) {
                    promise.then(null, fn);
                    return promise;
                };
                return promise;

            }
        }
    }
]);

