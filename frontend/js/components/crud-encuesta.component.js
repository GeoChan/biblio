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
        $controller('GenericCrudController', {vm: vm});
    }
})();

