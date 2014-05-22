'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
    .controller('ItemAllCtrl', ['$scope', '$routeParams', 'item', 'tag', function ($scope, $routeParams, itemFac, tags) {
        itemFac.all.query({}, function (data) {
            $scope.items = data;
        });
    }])
    .controller('ItemAddCtrl', ['$scope', '$routeParams', 'item', 'tag', function ($scope, $routeParams, itemFac, tags) {
        var sites = {
            manga: [
                {name: 'jbook', surl: 'https://www.google.com.hk/search?newwindow=1&q=%s+site%3Awww.jbook.co.jp'},
                {name: 'MyAnimeList', surl: 'https://www.google.com.hk/search?newwindow=1&q=%s+site%3Amyanimelist.net/manga'}
            ]
        };
        $scope.item = {};
        $scope.item.type = $routeParams.type;
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
        $scope.item.tags = [];
        $scope.setTag = function (index) {
            var tag = $scope.tags[index];
            if (tag.selected) {
                var i = $scope.item.tags.indexOf(tag.tid);
                if (i > -1) $scope.item.tags.splice(i, 1);
                tag.selected = false;
            } else {
                $scope.item.tags.push(tag.tid);
                tag.selected = true;
            }
        }
        $scope.save = function () {
            itemFac.create.save($scope.item, function (data) {
                console.log(data);
            });

        }
    }])
    .controller('MyCtrl2', ['$scope', function ($scope) {

    }]);
