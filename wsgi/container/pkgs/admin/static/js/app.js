"use strict";

function MainCtrl () {
  
}

angular
  .module('admin.ngApp', ['ngAnimate', 'ngSanitize', 'mgcrea.ngStrap'])
  .controller('MainCtrl', MainCtrl)
  .config(["$asideProvider", function($asideProvider) {
            angular.extend(
                $asideProvider.defaults,{container:"body",html:!0}
            );
    }]);


function AsideCtrl ($scope) {
    $scope.aside = {
        title:"Settings",
        content:"<br/>"
    }
}

angular.module("admin.ngApp")
    .controller("AsideCtrl", AsideCtrl);

function TypeaheadCtrl ($scope, $http) {
    $scope.selectedContent = "Content";
    $scope.selectedTags = "Tags";
    $scope.selectedTitle = "";
    $scope.getEntries = function(viewValue) {
        var args = {title: viewValue};
        return $http.get('/admin/entries.json?', {params: args}).then(
            function(e) {
                return e.data.entries
            });
    };
}

angular.module("admin.ngApp")
    .controller("TypeaheadCtrl", TypeaheadCtrl);

            