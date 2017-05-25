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

            function launchDialog(config) {
                var template = '<md-dialog flex>' +
                    (config.component || '(No Template)') +
                    '</md-dialog>';
                var dialog = {
                    template: template,
                    clickOutsideToClose: true,
                    resolve: {
                        dialogData: config.provider || empty
                    }
                };
                var promise = $mdDialog.show(dialog);
                promise.then(config.complete || empty, config.failed || empty);
                function empty() {
                    return undefined;
                }
            }
        }
    }

})();

