(function () {
    'use strict';

    angular
        .module('biblio')
        .component('crudPersona', crudPersona());

    function crudPersona() {
        var component = {
            templateUrl: 'templates/persona.html',
            bindings: {},
            controller: CrudPersonaController,
            controllerAs: 'vm',
        };
        return component;
    }

    CrudPersonaController.$inject = ['$controller'];

    /* @ngInject */
    function CrudPersonaController($controller) {
        var vm = this;
        vm.crudApiUrl = '/api/persona';
        vm.config = {
            component: '<graph-persona></graph-persona>',
            provider: function(){
                return 'hola';
            }
        };
        $controller('GenericCrudController', {vm: vm});
    }

})();

