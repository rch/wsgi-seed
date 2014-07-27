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


function AsideDemoCtrl ($scope) {
    $scope.aside = {
        title:"Settings",
        content:"<br/>"
    }
}

angular.module("admin.ngApp")
    .controller("AsideDemoCtrl", AsideDemoCtrl);
