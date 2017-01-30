(function () {
    angular
        .module('biblio')
        .controller('BoardController', BoardController);

    BoardController.$inject = ['$mdSidenav', '$mdToast', '$state'];

    function BoardController($mdSidenav, $mdToast, $state) {
        var vm = this;
        vm.toggleSidenav = function (menu) {
            $mdSidenav(menu).toggle();
        };
        vm.goto = function (link) {
            $state.go(link);
        };
        vm.toast = function (message) {
            var toast = $mdToast.simple().content('You clicked ' + message).position('bottom right');
            $mdToast.show(toast);
        };
        vm.toastList = function (message) {
            var toast = $mdToast.simple().content('You clicked ' + message + ' having selected ' + vm.selected.length + ' item(s)').position('bottom right');
            $mdToast.show(toast);
        };
        vm.selected = [];
        vm.toggle = function (item, list) {
            var idx = list.indexOf(item);
            if (idx > -1) list.splice(idx, 1);
            else list.push(item);
        };
        vm.data = {
            title: 'Biblioteca',
            user: {
                name: 'Usuario Biblioteca',
                email: 'admin@biblio.com',
                icon: 'face'
            },
            toolbar: {
                buttons: [{
                    name: 'Button 1',
                    icon: 'add',
                    link: 'Button 1'
                }],
                menus: [{
                    name: 'Menu 1',
                    icon: 'message',
                    width: '4',
                    actions: [{
                        name: 'Action 1',
                        message: 'Action 1',
                        completed: true,
                        error: true
                    }, {
                        name: 'Action 2',
                        message: 'Action 2',
                        completed: false,
                        error: false
                    }, {
                        name: 'Action 3',
                        message: 'Action 3',
                        completed: true,
                        error: true
                    }]
                }]
            },
            sidenav: {
                sections: [{
                    name: 'Administracion',
                    expand: true,
                    actions: [{
                        name: 'Persona',
                        icon: 'person',
                        link: 'books'
                    }, {
                        name: 'Encuesta',
                        icon: 'description',
                        link: 'quiz'
                    }, {
                        name: 'Periodo',
                        icon: 'schedule',
                        link: 'quiz'
                    }]
                }, {
                    name: 'Encuesta',
                    expand: false,
                    actions: [{
                        name: 'Encuestas',
                        icon: 'playlist_add_check',
                        link: 'Action 3'
                    }]
                }, {
                    name: 'Reportes',
                    expand: false,
                    actions: [{
                        name: 'Encuestados',
                        icon: 'trending_up',
                        link: 'Action 4'
                    }, {
                        name: 'Resultados',
                        icon: 'pie_chart',
                        link: 'Action 5'
                    }]
                }]
            },
            content: {
                lists: [{
                    name: 'List 1',
                    menu: {
                        name: 'Menu 1',
                        icon: 'settings',
                        width: '4',
                        actions: [{
                            name: 'Action 1',
                            message: 'Action 1',
                            completed: true,
                            error: true
                        }]
                    },
                    items: [{
                        name: 'Item 1',
                        description: 'Description 1',
                        link: 'Item 1'
                    }, {
                        name: 'Item 2',
                        description: 'Description 2',
                        link: 'Item 2'
                    }, {
                        name: 'Item 3',
                        description: 'Description 3',
                        link: 'Item 3'
                    }]
                }]
            }
        }
    }
})();

/*angular.module('App').config(function ($mdThemingProvider) {
 $mdThemingProvider.theme('default').primaryPalette('indigo');
 })*/
