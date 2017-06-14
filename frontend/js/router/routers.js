(function () {
    angular
        .module('biblio')
        .config(function ($stateProvider) {
            var persona = {
                name: 'persona',
                url: '/persona',
                template: '<crud-persona></crud-persona>'
            };
            var encuesta = {
                name: 'encuesta',
                url: '/encuesta',
                template: '<crud-encuesta></crud-encuesta>'
            };
            var periodo = {
                name: 'periodo',
                url: '/periodo',
                template: '<crud-periodo></crud-periodo>'
            };
            var resultado = {
                name: 'resultado',
                url: '/resultado',
                template: '<rept-resultado></rept-resultado>'
            };
            $stateProvider.state(persona);
            $stateProvider.state(encuesta);
            $stateProvider.state(periodo);
            $stateProvider.state(resultado);
        });
})();