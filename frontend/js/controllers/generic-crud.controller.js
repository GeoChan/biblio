(function () {
    'use strict';

    angular
        .module('biblio')
        .controller('GenericCrudController', GenericCrudController);

    GenericCrudController.$inject = ['vm', '$http', '$mdDialog'];

    /* @ngInject */
    function GenericCrudController(vm, $http, $mdDialog) {
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
            vm.launchDialog = launchDialog;

            function complete(response) {
                vm.crudData = response.data.results;
                vm.crudTotal = response.data.count;
            }

            function failed(response) {
            }

            function launchDialog(config, data) {
                config.clickOutsideToClose = true;
                var dialog_complete = config.complete || empty;
                var dialog_failed = config.failed || empty;
                config.failed = config.complete = undefined;
                config.fullscreen = true;
                config.escToClose = true;
                config.locals = {
                    collectedData: data
                };
                var promise = $mdDialog.show(config);
                promise.then(dialog_complete, dialog_failed);
                function empty() {
                    return undefined;
                }
            }
        }
    }

})();

