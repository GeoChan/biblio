(function () {
    angular
        .module('biblio')
        .config(function ($stateProvider) {
            var quiz = {
                name: 'quiz',
                url: '/quiz',
                template: '<biblio-wrapper title="pansoncito"><h2>el gordis me la come</h2></biblio-wrapper>'
            };
            var books = {
                name: 'books',
                url: '/books',
                template: '<biblio-wrapper><h2>enterita</h2></biblio-wrapper>'
            };
            $stateProvider.state(quiz);
            $stateProvider.state(books);
        });
})();