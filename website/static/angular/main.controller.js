(function() {  
    function MainCtrl ($http, $location, $anchorScroll) {

        var vm = this;
                console.log("byes")


        var protocol = $location.$$protocol;
        var host = $location.$$host;
        var port = $location.$$port;
        var apiUrl = protocol + '://' + host + ':' + port + '/api/'; 

        vm.registrantForm = 'preliminaryForm';
        vm.showLoginForm = false;
        vm.showLoginErrorMessage = false;

        vm.login = function(){
            vm.showLoginErrorMessage = true;
        };

        vm.scrollTo = function(id) {
          $location.hash(id);
          $anchorScroll();
        };

        vm.submit = function(){
            var data = JSON.stringify({
                first_name: vm.firstName,
                last_name: vm.lastName,
                email: vm.email, 
                industry: vm.industry,
                employee_count: vm.employeeCount,
                annual_hires: vm.annualHires
            });

            $http.post(apiUrl + 'registrants', data)
            .success(function(){
                if (vm.registrantForm === 'detailForm'){
                    vm.registrantForm = 'successMessage';
                }
                else if (vm.registrantForm === 'preliminaryForm'){
                    vm.registrantForm = 'detailForm';
                } 
            })
            .error(function(response){
                vm.registrantForm = 'errorMessage';;
            });
        };

        vm.closeMessage = function(){
            clearRegistrantData();
            vm.registrantForm = 'preliminaryForm';
        };

        function clearRegistrantData(){
            vm.firstName = '';
            vm.lastName = '';
            vm.email = '';
            vm.industry = '';
            vm.employeeCount = '';
            vm.annualHires   = '';
        }
    }

    angular.module('app')
    .controller('MainCtrl', ['$http', '$location', '$anchorScroll', MainCtrl])
    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);

})();
