(function () {
   angular
       .module('biblio')
       .config(function ($stateProvider) {
           var quiz ={
               name: 'quiz',
               url: '/quiz',
               template:'<h2>el gordis me la come</h2>'
           };
           var books ={
               name: 'books',
               url: '/books',
               template:'<h2>enterita</h2>'
           };
            $stateProvider.state(quiz);
            $stateProvider.state(books);
       });
})();