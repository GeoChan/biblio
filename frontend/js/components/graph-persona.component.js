(function () {
    'use strict';

    angular
        .module('biblio')
        .component('graphPersona', graphPersona());

    function graphPersona() {
        var template = 'hola mundo';
        var component = {
            template: template,
            controller: GraphPersonaController,
            controllerAs: 'vm'
        };
        return component;
    }

    GraphPersonaController.$inject = ['$mdDialog', 'dialogData'];
    /* @ngInject */
    function GraphPersonaController($mdDialog, dialogData) {
        var vm = this;
    }
})();
