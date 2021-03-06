﻿(function () {
    'use strict';

    angular
        .module('app')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', 'AuthenticationService', 'FlashService'];
    function LoginController($location, AuthenticationService, FlashService) {
        var vm = this;

        vm.login = login;

        (function initController() {
            // reset login status
            AuthenticationService.ClearCredentials();
        })();

        function login() {
            vm.dataLoading = true;

            AuthenticationService.Login(vm.username, vm.password)
            .then(function(success){
                console.log(success.data.token);
                AuthenticationService.SetCredentials(vm.username, vm.password, success.data.token);
                $location.path('/');
            }, function(error){
                console.log(error);
                FlashService.Error('Wrong username or password');
                    
            })
            .finally(function(){
                vm.dataLoading = false;
            });

        };
    }

})();
