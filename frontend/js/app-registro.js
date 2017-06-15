(function () {
    'use strict';

    angular
        .module('registro', ['ngMaterial'])
        .component('biblioRegistro', biblioRegistro());

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
        vm.msg_error = '';
        vm.encuesta_activa = false;

        function encuestar() {
            vm.msg_error = '';
            var promise = $http.get('/api/persona/c' + vm.codigo + '/');
            promise.then(completed, failed);

            function completed(result) {
                console.log(result.data);
                vm.encuesta_activa = true;
            }

            function failed() {
                vm.msg_error = 'No existe el estudiante';
            }
        }
    }
})();
