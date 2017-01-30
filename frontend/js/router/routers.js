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
            $stateProvider.state(persona);
            $stateProvider.state(encuesta);
            $stateProvider.state(periodo);
        });
})();