(function () {
    'use strict';

    angular
        .module('registro', ['ngMaterial'])
        .component('biblioRegistro', biblioRegistro())
        .config(config);

    config.$inject = ['$httpProvider'];
    function config($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }

    function biblioRegistro() {
        var component = {
            templateUrl: '/board/templates/registro.html',
            controller: RegistroController,
            controllerAs: 'vm'
        };
        return component;
    }

    RegistroController.$inject = ['$http'];

    function RegistroController($http) {
        var vm = this;
        vm.encuestar = encuestar;
        vm.codigo = null;
        vm.persona = null;
        vm.msg_error = '';
        vm.encuesta_activa = null;
        vm.periodo_activo = null;

        function encuestar() {
            vm.msg_error = '';
            var promise = $http.get('/api/persona/c' + vm.codigo + '/');
            promise.then(completed, failed);

            function completed(result) {
                vm.persona = result.data;

                var promise_encuesta = $http.get('/api/encuesta_activa/');
                promise_encuesta.then(encuesta_completed, encuesta_failed);
                var promise_periodo = $http.get('/api/periodo/active/');
                promise_periodo.then(periodo_completed, periodo_failed);

                function encuesta_completed(result) {
                    vm.encuesta_activa = result.data.results;
                }

                function encuesta_failed() {
                }

                function periodo_completed(result) {
                    vm.periodo_activo = result.data;
                }

                function periodo_failed() {

                }
            }

            function failed() {
                vm.msg_error = 'No existe el estudiante';
            }
        }
    }
})();
