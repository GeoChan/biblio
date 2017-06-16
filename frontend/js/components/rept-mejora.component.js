(function () {
    'use strict';

    angular
        .module('biblio')
        .component('reptMejora', reptMejora());

    function reptMejora() {
        var component = {
            templateUrl: 'templates/mejora.html',
            controller: ReptMejoraController,
            controllerAs: 'vm'
        };
        return component;
    }

    ReptMejoraController.$inject = ['$http'];
    /* @ngInject */
    function ReptMejoraController($http) {
        var vm = this;
        vm.encuesta_activa = [];

        init();

        function init() {
            var promise = $http.get('/api/encuesta_activa/');
            promise.then(completed, failed);
        }

        function completed(result) {
            for (var i in result.data.results) {
                var encuesta = result.data.results[i];
                var encuesta_data = {
                    chart: {
                        caption: encuesta.descripcion,
                        startingangle: "120",
                        showlabels: "0",
                        showlegend: "1",
                        enablemultislicing: "0",
                        slicingdistance: "15",
                        showpercentvalues: "1",
                        showpercentintooltip: "0",
                        plottooltext: "$datavalue ecuestas $label",
                        theme: "fint",
                        exportenabled: "1",
                        exportatclientside: "1"
                    },
                    data: encuesta.reporte_mejora
                };
                vm.encuesta_activa.push(encuesta_data);
            }
        }

        function failed() {

        }
    }
})();

