(function () {
    'use strict';

    angular
        .module('biblio')
        .component('crudPersona', crudPersona());

    function crudPersona() {
        var component = {
            templateUrl: 'templates/persona.html',
            controller: CrudPersonaController,
            controllerAs: 'vm'
        };
        return component;
    }

    CrudPersonaController.$inject = ['$controller'];
    /* @ngInject */
    function CrudPersonaController($controller) {
        var vm = this;
        vm.crudApiUrl = '/api/persona/';
        vm.config = {
            templateUrl: 'templates/pie-persona.html',
            controller: 'PiePersona as vm'
        };
        $controller('GenericCrudController', {vm: vm});
    }
})();

