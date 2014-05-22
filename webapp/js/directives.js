'use strict';

/* Directives */


angular.module('myApp.directives', []).
    directive('tagsList', ['tag', function (tags) {
        return {
            templateUrl: "views/UI_tags.html",
            restrict: "C",
            scope: {
                value: '=value',
                onChange: '&onChange'
            },
            link: function (scope, elems, attrs) {
                tags.all().then(function (data) {
                    scope.tags = data;
                    if (scope.value && scope.value.length > 0) {
                        for (var i = 0; i < scope.tags.length; i++) {
                            var t = scope.tags[i];
                            if (scope.value.indexOf(t.tid) > -1)t.selected = true;
                        }
                    }
                });
                scope.setTag = function (index) {
                    var tag = scope.tags[index];
                    if (tag.selected) {
                        if (scope.value) {
                            var i = scope.value.indexOf(tag.tid);
                            if (i > -1) scope.value.splice(i, 1);
                        }
                        tag.selected = false;
                    } else {
                        if (scope.value)scope.value.push(tag.tid);
                        tag.selected = true;
                    }

                    var f = scope.onChange();
                    if (f)f(tag);
                }
            }
        }
    }]);
