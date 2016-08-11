var app=angular.module('directs',[]);

app.directive('load',['$rootScope',function ($rootScope) {
    return{
        link:function (scope, element, attrs) {
            element.addClass('hide');
            $rootScope.$on('$routeChangeStart',function () {
                $rootScope.web='加载中';
                element.removeClass('hide');
                $("html,body").animate({scrollTop:0},10);
                $rootScope.loading='load-body';
            });
            $rootScope.$on('$routeChangeSuccess',function () {
                element.addClass('hide');
                $rootScope.loading='';
            })
        }
    }
}]);