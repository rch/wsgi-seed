"use strict";

function MainCtrl () {
  
}

angular
  .module('mgcrea.ngStrapDocs', ['ngAnimate', 'ngSanitize', 'mgcrea.ngStrap'])
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

angular.module("mgcrea.ngStrapDocs")
    .controller("AsideDemoCtrl", AsideDemoCtrl);
