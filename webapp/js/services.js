'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('myApp.services', [])
    .factory('tag', ['$resource', "$q", function (res, q) {
        var tags;

        function get() {

        }

        function all() {
            var defer = q.defer();
            if (!tags) {
                res(apiHost + 'tag/all')
                    .query({}, function (data) {
                        tags = data;
                        defer.resolve(tags);
                    });
            } else defer.resolve(tags);
            return defer.promise;
        }

        return{
            all: all
        }
    }]).factory('item', ['$resource', "$q", function (res, q) {
        function createItem() {
            return res(apiHost + "item/add");
        }

        return {
            create: res(apiHost + "item/add"),
            delete: res(apiHost + "item/delete"),
            update: res(apiHost + "item/update"),
            all: res(apiHost + "item/all")
        }
    }]);
