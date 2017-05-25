(function () {
    'use strict';

    angular
        .module('biblio')
        .controller('PiePersona', PiePersona);

    PiePersona.$inject = ['$mdDialog', 'collectedData'];
    /* @ngInject */
    function PiePersona($mdDialog, collectedData) {
        var vm = this;
        vm.data = [];
        vm.close = close;
        vm.options = {
            chart: {
                type: "pieChart",
                height: 300,
                showLabels: true,
                duration: 500,
                labelThreshold: 0.01,
                labelSunbeamLayout: true,
                x: function (d) {
                    return d.key;
                },
                y: function (d) {
                    return d.porcentaje;
                },
                legend: {
                    margin: {
                        top: 5,
                        right: 35,
                        bottom: 5,
                        left: 0
                    }
                }
            }
        };
        init();

        function init() {
            for (var i in collectedData) {
                vm.data.push({
                    descripcion: collectedData[i].descripcion,
                    data: [
                        {
                            key: 'Contestado',
                            porcentaje: collectedData[i].porcentaje
                        },
                        {
                            key: 'Sin Contestar',
                            porcentaje: 100.0 - collectedData[i].porcentaje
                        }
                    ]
                });
            }
        }

        function close() {
            $mdDialog.cancel();
        }
    }
})();

