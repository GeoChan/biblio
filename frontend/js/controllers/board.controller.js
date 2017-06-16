(function () {
    angular
        .module('biblio')
        .controller('BoardController', BoardController);

    BoardController.$inject = ['$mdSidenav', '$mdToast', '$state', '$http'];

    function BoardController($mdSidenav, $mdToast, $state, $http) {
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
        check();
        vm.data = {
            title: 'Biblioteca',
            user: {
                name: 'Usuario Biblioteca',
                email: 'admin@biblio.com',
                icon: 'face'
            },
            sidenav: {
                sections: [{
                    name: 'Panel de Control',
                    expand: true,
                    actions: [{
                        name: 'Persona',
                        icon: 'person',
                        link: 'persona'
                    }, {
                        name: 'Encuesta',
                        icon: 'description',
                        link: 'encuesta'
                    }, {
                        name: 'Periodo',
                        icon: 'schedule',
                        link: 'periodo'
                    }]
                }, {
                    name: 'Reportes',
                    expand: false,
                    actions: [
                        {
                            name: 'Mejora',
                            icon: 'pie_chart',
                            link: 'mejora'
                        },
                        {
                            name: 'Resultados',
                            icon: 'trending_up',
                            link: 'resultado'
                        }
                    ]
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
        };
        function check() {
            var promise = $http.get('/api/user/current/')
            promise.then(function (result) {
                vm.data.user.name = result.data.username;
                vm.data.user.email = result.data.email;
            }, function () {
                location.href = '/';
            });
        }
    }
})();
