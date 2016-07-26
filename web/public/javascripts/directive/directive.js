app.directive('info', function ($rootScope) {
    return {
        restrict: 'E',
        template: '<ul class="nav navbar-nav">' +
        '<li class="li"><a href="#/">首页</a></li>' +
        '<li class="li" ng-hide="iflogin"><a href="#/login">登录</a></li>' +
        '<li class="li" ng-show="iflogin"><a href="#/profile">我的信息</a></li>' +
        '<li class="li" ng-show="iflogin"><a ng-click="logout()">登出</a></li>' +
        '</ul>',
        replace: true
    };
});