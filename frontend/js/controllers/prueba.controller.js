(function(){
    angular
        .module('biblio')
        .controller('prueba', prueba);

    function prueba(){
        this.hola = "hola juan carlos";
    }
})();