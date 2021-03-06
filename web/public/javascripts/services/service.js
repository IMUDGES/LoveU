var services = angular.module('MyService', []);
var root_url = 'http://183.175.14.250:5000/';
//var root_url = 'http://183.175.12.157:5000/';
//var root_url = 'http://183.175.12.178:5000/';
/*var delay = $q.defer();
 var promise = delay.promise;
 promise.success = function (fn) {
 promise.then(fn);
 return promise;
 };
 promise.error = function (fn) {
 promise.then(null, fn);
 return promise;
 };*/
var transform = function (data) {
    return $.param(data);
};

var postCfg = {
    headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
    transformRequest: transform
};

services.factory('LogService', ['$q', '$http', 'SecretKey',
    function ($q, $http, SecretKey) {
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
                }, postCfg).success(function (iflogin) {
                    //       setCookie('key', data.SecretKey);
                    if (iflogin.state == '1') {
                        SecretKey.Set(iflogin.SecretKey);
                        SecretKey.Phone(logdata.name);
                    }
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
                    ifshow: false,
                    text: '测试'
                };
            }
        }
    }
]);
services.factory('RegistService', ['$q', '$http',
    function ($q, $http) {
        var save = '';
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
                if (save.length !== 11) {
                    delay.reject('phone');
                    return promise;
                }
                if (regdata.pass.length < 6) {
                    delay.reject('pass1');
                    return promise;
                }
                if (regdata.pass.length > 18) {
                    delay.reject('pass2');
                    return promise;
                }
                if (regdata.pass != regdata.pass1) {
                    delay.reject('pass');
                    return promise;
                }
                $http.post(root_url + 'register3', {
                    UserPhone: regdata.phone,
                    PassWord: md5_s(regdata.pass),
                    NickName: regdata.nick,
                    CheckCode: regdata.vcode
                }, postCfg).success(function (data) {
                    if (data.state == '1')
                        delay.resolve('成功');
                    else
                        delay.reject('vcode');
                }).error(function (data) {
                    delay.reject('Unable');
                });
                return promise;
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
                if (number.length != 11) {
                    delay.reject('请填写正确的手机号码');
                    return promise;
                }
                $http.post(root_url + 'register1', {
                    UserPhone: number
                }, postCfg).success(function (data) {
                    if (data.state == '1') {
                        save = number;
                        delay.resolve(data.msg);
                    } else
                        delay.reject('手机号已被注册');
                });
                return promise;
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
            },
            setUser: function () {
                return {
                    phone: '',
                    vcode: '',
                    nick: '',
                    pass: '',
                    pass1: ''
                }
            }
        }
    }]);
services.factory('ProfileService', ['$q', '$http', 'SecretKey', '$timeout', function ($q, $http, SecretKey, $timeout) {
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
    return {
        SetMsg: function () {
            return {
                ifavatar: false,
                croped: false,
                jwxt: '验证教务系统以获取更多支持',
                pay: 'test',
                ifpay: false
            }
        },
        SetForm: function () {
            return {
                Jwxt: '',
                Pass: '',
                Money: '',
                PayPass: '',
                Vcode: ''
            }
        },
        GetData: function () {
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
            if (SecretKey.Get().length == 0 || SecretKey.GetPhone().length == 0) {
                delay.reject("error");
                return promise;
            }
            $timeout(function () {
                delay.reject('网络错误');
            }, 2000);
            $http.post(root_url + 'mydata', {
                UserPhone: SecretKey.GetPhone(),
                SecretKey: SecretKey.Get()
            }, postCfg).success(function (data) {
                delay.resolve(data.data)
            }).error(function () {
                delay.reject("Unable to Connect");
            });
            return promise;
        },
        Update: function (data) {
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
            if (data.NickNameCopy.length <= 0) {
                delay.reject('nick');
                return promise;
            }
            $http.post(root_url + 'changemydata', {
                UserPhone: SecretKey.GetPhone(),
                SecretKey: SecretKey.Get(),
                NickName: data.NickNameCopy,
                UserSex: data.UserSex
            }, postCfg).success(function (data) {
                if (data.state == '1')
                    delay.resolve(data);
                else
                    delay.reject(data.msg);
            }).error(function () {
                delay.reject('Unable to Connect');
            });
            return promise;
        },
        SetAvatar: function (img) {
            var blob = dataURItoBlob(img);
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
            $http({
                method: 'POST',
                url: root_url + 'Userphoto',
                headers: {
                    'Content-Type': undefined
                },
                data: {
                    file: blob,
                    UserPhone: SecretKey.GetPhone(),
                    SecretKey: SecretKey.Get()
                },
                transformRequest: formDataObject
            }).success(function (data) {
                delay.resolve(data);
            }).error(function () {
                delay.reject('上传失败，请稍后重试');
            });
            return promise;
        },
        Jwxt: function (form) {
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
            if (form.Jwxt.length != 10 || form.Jwxt.length == 0) {
                delay.reject('输入的学号有误');
                return promise;
            }
            if (form.Pass.length == 0) {
                delay.reject("请输入密码");
                return promise;
            }
            $http.post(root_url + 'upjwxtservice', {
                UserPhone: SecretKey.GetPhone(),
                SecretKey: SecretKey.Get(),
                JwxtNumber: form.Jwxt,
                JwxtPassword: form.Pass
            }, postCfg).success(function (data) {
                if (data.state == '1')
                    delay.resolve(data);
                else
                    delay.reject(data.msg);
            }).error(function () {
                delay.reject('Unable to Connect');
            });
            return promise;
        },
        Charge: function (form) {
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
            if (form.Money.length == 0 || isNaN(form.Money)) {
                delay.reject('请输入正确的数字');
                return promise;
            }
            $http.post(root_url + 'recharge', {
                UserPhone: SecretKey.GetPhone(),
                SecretKey: SecretKey.Get(),
                Money: form.Money
            }, postCfg).success(function (data) {
                if (data.state == '1') {
                    delay.resolve();
                }
                else {
                    delay.reject(data.msg);
                }
            }).error(function () {
                delay.reject('Unable to Connect');
            });
            return promise;
        },
        GetVcode: function () {
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
            $http.post(root_url + 'sendcheck', {
                UserPhone: SecretKey.GetPhone(),
                SecretKey: SecretKey.Get()
            }, postCfg).error(function () {
                delay.reject('验证手机号失败');
            });
            return promise;
        },
        CreatPay: function (form) {
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
            $http.post(root_url + 'setpsw', {
                UserPhone: SecretKey.GetPhone(),
                SecretKey: SecretKey.Get(),
                CheckCode: form.Vcode,
                PayPassword: md5_s(form.PayPass)
            }, postCfg).success(function (data) {
                if (data.state == '1') {
                    delay.resolve();
                }
                else {
                    delay.reject(data.msg);
                }
            }).error(function () {
                delay.reject('Unable to Connect');
            });
            return promise;
        }
    }
}]);

services.factory('FoodService', ['$q', '$http', '$timeout', function ($q, $http, $timeout) {
    return {
        foodlist: function (page) {
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
            $timeout(function () {
                delay.reject('网络错误');
            }, 3000);
            $http.get(root_url + 'food?page='+page).success(function (data) {
                if(data.num!=0)  delay.resolve(data);
                else delay.reject('0');
            }).error(function () {
                delay.reject('Unable to connect');
            });
            return promise;
        },
        SetPage: function () {
            return {
                Last:false,
                Num:1,
                Old:true
            }
        },
        GetOtherData: function (UserId) {
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
            $http.get(root_url+'data',{
                params: {UserId:UserId}
            } ).success(function (data) {
                 delay.resolve(data);
            }).error(function () {
                delay.reject("Unable to Connect");
            });
            return promise;
        },
        Accept: function () {

        }
    }
}]);
services.factory('RunService', ['$q', '$http', '$timeout', function ($q, $http, $timeout) {
    return {
        runlist: function () {
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
            $timeout(function () {
                delay.reject('网络错误');
            }, 3000);
            $http.get(root_url + 'run?page=1').success(function (data) {
                delay.resolve(data.rundata);
            }).error(function () {
                delay.reject('Unable t connect');
            });
            return promise;
        }
    }
}]);
services.factory('AuctionService', ['$q', '$http', function ($q, $http) {
    return {
        auctionlist: function () {
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
            $http.get(root_url + 'pai?page=1').success(function (data) {
                delay.resolve(data.paidata);
            }).error(function () {
                delay.reject('Unable t connect');
            });
            return promise;
        }
    }
}]);
services.factory('SecretKey', function () {
    var key = '';
    var phone = '';
    return {
        Set: function (value) {
            key = value;
            setCookie('key', value, 3600);
        },
        Get: function () {
            if (key.length > 0)
                return key;
            else
                return getCookie('key');
        },
        Phone: function (number) {
            phone = number;
            setCookie('Phone', number, 3600);
        },
        GetPhone: function () {
            return getCookie('Phone');
        },
        ifKey: function () {
            return (getCookie('key').length > 0);
        },
        destory: function () {
            clearCookie('key');
            clearCookie('Phone');
            key = '';
            phone = '';
        }
    }
});

