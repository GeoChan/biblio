(function () {
    'use strict';

    angular
        .module('biblio')
        .component('crudEncuesta', crudEncuesta());

    function crudEncuesta() {
        var component = {
            templateUrl: 'templates/encuesta.html',
            controller: CrudEncuestaController,
            controllerAs: 'vm'
        };
        return component;
    }

    CrudEncuestaController.$inject = ['$controller'];

    /* @ngInject */
    function CrudEncuestaController($controller) {
        var vm = this;
        vm.crudApiUrl = '/api/encuesta_activa';
        vm.config = {
            templateUrl: 'templates/pie-encuesta.html',
            controller: 'PieEncuesta as vm'
        };
        $controller('GenericCrudController', {vm: vm});
    }
})();

