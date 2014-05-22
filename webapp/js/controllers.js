'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
    .controller('ItemAllCtrl', ['$scope', '$routeParams', 'item', 'tag', function ($scope, $routeParams, itemFac, tags) {
        itemFac.all.query({}, function (data) {
            $scope.items = data;

        });
        $scope.itemUpdate = function (index) {
            itemFac.update.save($scope.items[index], function (data) {
                $scope.items[index] = data;
            });
        }
        $scope.itemDel = function (index) {
            var id = $scope.items[index].id;
            itemFac.delete.get({id: id}, function (data) {
                if (data.err_code == 0) {
                    $scope.items.splice(index, 1);
                    $scope.$apply();
                }
            });
        }

        tags.all().then(function (ts) {
            $scope.tags = ts;
        });
    }])
    .controller('ItemAddCtrl', ['$scope', '$routeParams', '$location', 'item', 'tag', function ($scope, $routeParams, $location, itemFac, tags) {
        var sites = {
            manga: [
                {name: 'jbook', surl: 'https://www.google.com.hk/search?newwindow=1&q=%s+site%3Awww.jbook.co.jp'},
                {name: 'MyAnimeList', surl: 'https://www.google.com.hk/search?newwindow=1&q=%s+site%3Amyanimelist.net/manga'}
            ]
        };
        $scope.item = {type: $routeParams.type, tags: [], score: 0};
        $scope.searchs = sites[ $routeParams.type];
        $scope.search = function () {
            var csites = $('.input-search:checked');
            csites.each(function (index, item) {
                if ($scope.item.title) var a = window.open(item.getAttribute('value').replace('%s', $scope.item.title), "",
                        "top=0,left=" + index * 600 + ",width=600,height=800,location=yes,menubar=no,resizable=yes,scrollbars=yes,status=no,toolbar=no");
            });
        }
        $scope.fetch = function (url) {
            var btn = $('#btn-add-fetch')[0];
            btn.disabled = true;
            btn.innerText = "Fetching...";
            $.getJSON(apiHost + 'item/fetch', {url: url}, function (data) {
                btn.disabled = false;
                btn.innerText = "Fetch";
                $scope.item.author = data.author;
                $scope.item.img = data.img;
                $scope.$apply();
            });
        }

        tags.all().then(function (ts) {
            $scope.tags = ts;
        });

        $scope.setTag = function (tag) {
            if (tag.selected) {
                $scope.item.tags.push(tag.tid);

            } else {
                var i = $scope.item.tags.indexOf(tag.tid);
                if (i > -1) $scope.item.tags.splice(i, 1);
            }
        }
        $scope.save = function () {
            itemFac.create.save($scope.item, function (data) {
                $location.path('/item/all');
            });

        }
    }])
    .controller('MyCtrl2', ['$scope', function ($scope) {

    }]);
