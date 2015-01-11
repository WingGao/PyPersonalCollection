'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
    .controller('ItemAllCtrl', ['$scope', '$routeParams', '$location', 'item', 'tag',
        function ($scope, $routeParams, $location, itemFac, tags) {
            $scope.sort = $routeParams.sort;
            $scope.type = $routeParams.type;
            $scope.nowPage = $routeParams.page;
            $scope.stags = [];
            itemFac.all.get({
                type: $routeParams.type,
                sort: $routeParams.sort,
                page: $routeParams.page - 1
            }, function (data) {
                $scope.items = data.items;
                $scope.maxPage = data.pages;
            });
            $scope.itemUpdate = function (index) {
                itemFac.update.save($scope.items[index], function (data) {
                    $scope.items[index] = data;
                });
            };
            $scope.itemDel = function (index) {
                var id = $scope.items[index].id;
                itemFac.delete.get({id: id}, function (data) {
                    if (data.err_code == 0) {
                        $scope.items.splice(index, 1);
                        $scope.$apply();
                    }
                });
            };

            tags.all().then(function (ts) {
                $scope.tags = ts;
            });

            $scope.nav = function (type, sort, page) {
                var t = $routeParams.type;
                var s = $routeParams.sort;
                var p = $routeParams.page;
                if (type)t = type;
                if (sort)s = sort;
                if (page)p = page;
                $location.path('/item/all/' + t + "/" + s + "/" + p);
            };
            function combineTags(tis) {
                return tis.join(',');
            }

            $scope.searchByTags = function () {
                itemFac.all.query({type: $routeParams.type, sort: $routeParams.sort, tags: combineTags($scope.stags)},
                    function (data) {
                        $scope.items = data;
                    });
            };
            $scope.checkTags = function (tags) {
                for (var i = 0; i < $scope.stags.length; i++) {
                    if (tags.indexOf($scope.stags[i]) == -1)return false;
                }
                return true;
            };
        }])
    .controller('ItemAddCtrl', ['$scope', '$routeParams', '$location', 'item', 'tag', function ($scope, $routeParams, $location, itemFac, tags) {
        var sites = {
            manga: [
                {
                    name: 'jbook',
                    surl: 'https://www.google.co.jp/search?newwindow=1&q=%s+site%3Awww.jbook.co.jp',
                    def: true
                },
                {
                    name: 'dmm',
                    surl: 'https://www.google.co.jp/search?newwindow=1&q=%s+site%3Awww.dmm.co.jp%2Fdc%2Fbook%2F',
                    def: false
                },
                {
                    name: 'MyAnimeList',
                    surl: 'https://www.google.co.jp/search?newwindow=1&q=%s+site%3Amyanimelist.net/manga',
                    def: false
                }
            ],
            av: [
                {
                    name: 'dmm',
                    surl: 'http://www.dmm.co.jp/mono/dvd/-/detail/=/cid=%s/',
                    def: true
                }
            ]
        };
        $scope.item = {type: $routeParams.type, tags: [], score: 0};
        $scope.searchs = sites[$routeParams.type];
        $scope.search = function () {
            var csites = $('.input-search:checked');
            csites.each(function (index, item) {
                if ($scope.item.title) var a = window.open(item.getAttribute('value').replace('%s', $scope.item.title.trim()), "",
                    "top=0,left=" + index * 600 + ",width=600,height=800,location=yes,menubar=no,resizable=yes,scrollbars=yes,status=no,toolbar=no");
            });
        };

        $scope.fetch = function (url) {
            var btn = $('#btn-add-fetch')[0];
            btn.disabled = true;
            btn.innerText = "Fetching...";

            if ($routeParams.type == 'av' && url == undefined) {
                $scope.item.url = 'http://www.dmm.co.jp/mono/dvd/-/detail/=/cid=%s/'.replace('%s', $scope.item.title.trim());
                url = $scope.item.url;
            }

            $.getJSON(apiHost + 'item/fetch', {url: url}, function (data) {
                $scope.item.title = data.title;
                $scope.item.author = data.author;
                $scope.item.img = data.img;
                $scope.$apply();
            }).always(function () {
                btn.disabled = false;
                btn.innerText = "Fetch";
            });
        };

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
            }, function (error) {
                $scope.error = "Save Failed!";
            });

        }
    }])
    .controller('LoginCtrl', ['$scope', '$http', '$location', function ($scope, $http, $location) {
        $http.get('/user/check').success(function (res) {
            if (res.is_login) {
                $location.path('/item/all/all/newest/1')
            } else {
                window.location.href = '/user/login?next=/webapp/index.html'
            }
        })
    }]);
