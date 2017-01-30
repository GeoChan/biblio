(function () {
    'use strict';

    angular
        .module('biblio')
        .directive('biblioWrapper', biblioWrapper);

    biblioWrapper.$inject = [];

    /* @ngInject */
    function biblioWrapper() {
        var template = '<div class="md-whiteframe-z2">' +
                '<md-toolbar class="md-table-toolbar-tools">' +
                    '<div class="md-toolbar-tools">' +
                        '<span>{{ vm.title }}</span>' +
                        '<div flex></div>' +
                        '<md-button class="md-icon-button">' +
                            '<md-icon md-font-library="material-icon">more_vert</md-icon>' +
                        '</md-button>' +
                    '</div>' +
                '</md-toolbar>' +
                '<md-content ng-transclude></md-content>' +
            '</div>';

        var directive = {
            bindToController: true,
            controller: BiblioWrapperController,
            controllerAs: 'vm',
            link: link,
            restrict: 'EA',
            scope: {
                title: '@'
            },
            transclude: true,
            template: template
        };
        return directive;

        function link(scope, element, attrs) {

        }
    }

    BiblioWrapperController.$inject = [];

    /* @ngInject */
    function BiblioWrapperController() {

    }

})();

