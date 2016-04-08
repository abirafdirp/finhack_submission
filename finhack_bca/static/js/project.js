/* Project specific Javascript goes here. */
var finhacksApp = angular.module('finhacks', [
]);

finhacksApp.run(function($rootScope) {
});

// differentiate angular and django template language
finhacksApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
});


finhacksApp.controller('CountersCtrl', ['$scope', '$filter',
  function($scope, $filter){
    // calculate distance between two latitude and longitude points
    // based on http://stackoverflow.com/a/27943/3390639
    // using haversine formula
    $scope.distance = function(lat1, lon1, lat2, lon2) {
      var p = 0.017453292519943295;    // Math.PI / 180
      var c = Math.cos;
      var a = 0.5 - c((lat2 - lat1) * p)/2 +
        c(lat1 * p) * c(lat2 * p) *
        (1 - c((lon2 - lon1) * p))/2;

      return 12742 * Math.asin(Math.sqrt(a)); // 2 * R; R = 6371 km
    };
    $scope.selectDropdownItem = function(selectedItem){
      $scope.selectedItem = selectedItem;
      angular.forEach($scope.counters, function(counter){
        counter['distance'] = $scope.distance(selectedItem.latitude, selectedItem.longitude, counter.latitude, counter.longitude);
      });
      $scope.counters = $filter('orderBy')($scope.counters, 'distance');
    }
  }
]);