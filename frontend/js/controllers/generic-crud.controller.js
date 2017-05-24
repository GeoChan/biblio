(function () {
    'use strict';

    angular
        .module('biblio')
        .controller('GenericCrudController', GenericCrudController);

    GenericCrudController.$inject = ['vm', '$http'];

    /* @ngInject */
    function GenericCrudController(vm, $http) {
        vm.crudApiUrl = vm.crudApiUrl || '';
        vm.crudData = [];
        vm.crudOrder = '';
        vm.crudTotal = 1;
        vm.crudLimit = 10;
        vm.crudPage = 1;
        vm.promise = null;
        vm.getCrudData = getCrudData;

        getCrudData();

        function getCrudData() {
            vm.promise = $http.get(vm.crudApiUrl + '?page=' + vm.crudPage + '&size=' + vm.crudLimit);
            vm.promise.then(complete, failed);

            function complete(response) {
                vm.crudData = response.data.results;
                vm.crudTotal = response.data.count;
            }

            function failed(response) {
            }
        }
    }

})();

