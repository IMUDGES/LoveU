var app=angular.module('directs',[]);

app.directive('load',['$rootScope',function ($rootScope) {
    return{
        link:function (scope, element, attrs) {
            element.addClass('hide');
            $rootScope.$on('$routeChangeStart',function () {
                $rootScope.web='加载中';
                element.removeClass('hide');
            });
            $rootScope.$on('$routeChangeSuccess',function () {
                element.addClass('hide');
            })
        }
    }
}]);
