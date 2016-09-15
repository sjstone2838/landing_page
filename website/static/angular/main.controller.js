(function() {  
    function MainCtrl ($http, $location, $anchorScroll) {

        var vm = this;

        var protocol = $location.$$protocol;
        var host = $location.$$host;
        var port = $location.$$port;
        var apiUrl = protocol + '://' + host + ':' + port + '/api/'; 

        vm.showPreliminaryForm = true;
        vm.showLoginForm = false;
        vm.showDetailForm = false;
        vm.showRegisterSuccessMessage = false;
        vm.showRegisterErrorMessage = false;
        vm.showLoginErrorMessage = false;

        vm.login = function(){
            vm.showLoginErrorMessage = true;
            console.log('here');
        };

        vm.scrollTo = function(id) {
          console.log(id);
          $location.hash(id);
          console.log($location);
          $anchorScroll();
        };

        vm.submit = function(email){
            $http.get(apiUrl + 'registrants?search=' + email)
            .then(function(response) {
                
                var data = JSON.stringify({
                    first_name: vm.firstName,
                    last_name: vm.lastName,
                    email: vm.email, 
                    industry: vm.industry,
                    employee_count: vm.employeeCount,
                    annual_hires: vm.annualHires
                });
        
                if(response.data.count === 1){
                    registrantID = response.data.results[0].id;
                    updateRegistrant(registrantID, data)
                }
                else {
                    createRegistrant(data)
                }
            });
        };

        vm.closeMessage = function(){
            vm.showPreliminaryForm = true;
            vm.showDetailForm = false;
            vm.showRegisterSuccessMessage = false;
            vm.showRegisterErrorMessage = false;
            clearRegistrantData();
        };

        function createRegistrant(data){
            $http.post(apiUrl + 'registrants', data)
            .success(function(){
                vm.showDetailForm = true;
            })
            .error(function(response){
                vm.showRegisterErrorMessage = true;
            })
            .finally(function(){
                vm.showPreliminaryForm = false;
            });
        }

        function updateRegistrant(registrantID, data){
            $http.put(apiUrl + 'registrants/' + registrantID, data)
            .success(function(){
                vm.showRegisterSuccessMessage = true;
            })
            .error(function(response){
                vm.showRegisterErrorMessage = true;
            })
            .finally(function(){
                vm.showDetailForm = false;
            });
        }

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
