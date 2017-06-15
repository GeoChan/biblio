(function () {
    'use strict';

    angular
        .module('registro', ['ngMaterial'])
        .controller('RegistroController', RegistroController);

    RegistroController.$inject = ['$http'];

    function RegistroController($http) {
        var vm = this;
        vm.encuestar = encuestar;
        vm.codigo = null;
        vm.msg_error = '';

        function encuestar() {
            var promise = $http.get('/api/persona/c' + vm.codigo + '/');
            promise.then(completed, failed);

            function completed(result) {
                console.log(result.data);
            }

            function failed() {
                vm.msg_error = 'No existe el estudiante';
            }
        }
    }
})();
