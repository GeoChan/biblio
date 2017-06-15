(function () {
    'use strict';

    angular
        .module('biblio')
        .component('crudPeriodo', crudPeriodo());

    function crudPeriodo() {
        var component = {
            templateUrl: 'templates/periodo.html',
            controller: CrudPeriodoController,
            controllerAs: 'vm'
        };
        return component;
    }

    CrudPeriodoController.$inject = ['$controller'];

    /* @ngInject */
    function CrudPeriodoController($controller) {
        var vm = this;
        vm.crudApiUrl = '/api/periodo/';
        $controller('GenericCrudController', {vm: vm});
    }
})();

