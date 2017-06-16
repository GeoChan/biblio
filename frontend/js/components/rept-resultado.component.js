(function () {
    'use strict';

    angular
        .module('biblio')
        .component('reptResultado', reptResultado());

    function reptResultado() {
        var component = {
            templateUrl: 'templates/resultados.html',
            controller: ReptResultadoController,
            controllerAs: 'vm'
        };
        return component;
    }

    ReptResultadoController.$inject = ['$http'];
    /* @ngInject */
    function ReptResultadoController($http) {
        var vm = this;
        vm.data_si = [];
        vm.data_no = [];

        init();

        function init() {
            var promise = $http.get('/api/encuesta_activa/');
            promise.then(completed, failed);
        }

        function completed(result) {
            for (var i in result.data.results) {
                var encuesta = result.data.results[i];
                var encuesta_data_si = {
                    chart: {
                        theme: "carbon",
                        caption: encuesta.descripcion,
                        xAxisName: "Preguntas",
                        pYAxisName: "Respuestas Negativas (Si)",
                        sYAxisname: "Porcentaje Acumulativo",
                        showValues: "0",
                        showXAxisLine: "1",
                        showLineValues: "1",
                        exportenabled: "1",
                        exportatclientside: "1"
                    },
                    data: []
                };
                var encuesta_data_no = {
                    chart: {
                        theme: "zune",
                        caption: encuesta.descripcion,
                        xAxisName: "Preguntas",
                        pYAxisName: "Respuestas Positivas (No)",
                        sYAxisname: "Porcentaje Acumulativo",
                        showValues: "0",
                        showXAxisLine: "1",
                        showLineValues: "1",
                        exportenabled: "1",
                        exportatclientside: "1"
                    },
                    data: []
                };
                for (var j in encuesta.cobertura_respuesta) {
                    var pregunta = encuesta.cobertura_respuesta[j];
                    encuesta_data_si.data.push({
                        label: pregunta.enunciado,
                        value: pregunta.escala.Si
                    });
                    encuesta_data_no.data.push({
                        label: pregunta.enunciado,
                        value: pregunta.escala.No
                    });
                }
                vm.data_si.push(encuesta_data_si);
                vm.data_no.push(encuesta_data_no);
            }
        }

        function failed() {

        }
    }
})();

