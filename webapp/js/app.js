'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
    'ngRoute',
    'ngResource',
    'myApp.filters',
    'myApp.services',
    'myApp.directives',
    'myApp.controllers'
]).
    config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/item/add/:type', {templateUrl: 'views/item_add.html', controller: 'ItemAddCtrl'});
        $routeProvider.when('/item/all/:type/:sort/:page', {templateUrl: 'views/item_all.html', controller: 'ItemAllCtrl'});
        $routeProvider.otherwise({redirectTo: '/item/all/all/newest/0'});
    }]);
