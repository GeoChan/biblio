(function () {
    'use strict';

    angular
        .module('biblio')
        .component('crudEncuesta', crudEncuesta());

    function crudEncuesta() {
        var component = {
            templateUrl: 'templates/encuesta.html',
            bindings: {},
            controller: CrudEncuestaController,
            controllerAs: 'vm',
        };
        return component;
    }

    CrudEncuestaController.$inject = ['$controller'];

    /* @ngInject */
    function CrudEncuestaController($controller) {
        var vm = this;
        vm.crudApiUrl = '/api/encuesta';
        $controller('GenericCrudController', {vm: vm});
    }

})();

