(function () {
    'use strict';

    angular
        .module('registro')
        .component('biblioRegistroPregunta', biblioRegistroPregunta());

    function biblioRegistroPregunta() {
        var template = '<md-button class="md-raised" ng-if="!vm.responder" ng-click="vm.responder=true">' +
            'Responder' +
            '</md-button>' +
            '<span ng-if="vm.responder && !vm.gracias">' +
            '<md-button class="md-primary md-raised" ng-click="vm.respuesta(\'1\')" ng-disabled="vm.enviando">SI</md-button>' +
            '<md-button class="md-warn md-raised" ng-click="vm.respuesta(\'2\')" ng-disabled="vm.enviando">NO</md-button>' +
            '</span>' +
            '<span ng-if="vm.gracias" class="gracias">Gracias Por Tu Respuesta!!</span>';
        var component = {
            template: template,
            controller: BiblioRegistroPreguntaController,
            controllerAs: 'vm',
            bindings: {
                pregunta: '<',
                persona: '<',
                periodo: '<'
            }
        };
        return component;
    }

    BiblioRegistroPreguntaController.$inject = ['$http'];
    function BiblioRegistroPreguntaController($http) {
        var vm = this;
        vm.responder = false;
        vm.gracias = false;
        vm.respuesta = respuesta;
        vm.enviando = false;
        vm.$onInit = init;

        function init() {
            for (var i in vm.persona.registros) {
                var registro = vm.persona.registros[i];
                if (registro.pregunta == vm.pregunta) {
                    vm.responder = vm.gracias = true;
                }
            }
        }

        function respuesta(escala) {
            vm.enviando = true;
            var data = {
                pregunta: vm.pregunta,
                persona: vm.persona.url,
                periodo: vm.periodo,
                escala: escala
            };
            var promise = $http.post('/api/registro/', data);
            promise.then(completed, failed);

            function completed() {
                vm.gracias = true;
            }

            function failed(data) {
                console.log(data);
            }
        }
    }
})();