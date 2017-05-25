(function () {
    'use strict';

    angular
        .module('biblio')
        .controller('PieEncuesta', PieEncuesta);

    PieEncuesta.$inject = ['$mdDialog', 'collectedData'];
    /* @ngInject */
    function PieEncuesta($mdDialog, collectedData) {
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
                    return d.label;
                },
                y: function (d) {
                    return d.value;
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
                    enunciado: collectedData[i].enunciado,
                    data: [
                        {
                            label: 'SI',
                            value: collectedData[i].escala.Si
                        },
                        {
                            label: 'NO',
                            value: collectedData[i].escala.No
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

