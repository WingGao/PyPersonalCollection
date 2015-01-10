'use strict';

/* Filters */

angular.module('myApp.filters', []).
    filter('formatTag', ['tag', function (tags) {
        var ts;
        if (!ts) tags.all().then(function (data) {
            ts = data;
        });
        return function (tid) {
            for (var i = 0; i < ts.length; i++) {
                if (ts[i].tid == tid)
                    return ts[i].name;
            }
        };
    }]).filter('range', function () {
        return function (input, total) {
            total = parseInt(total);
            for (var i = 0; i < total; i++)
                input.push(i);
            return input;
        };
    });
;
