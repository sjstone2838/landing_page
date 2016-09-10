(function() {  
    function MainCtrl ($http) {

        var vm = this;
        var apiUrl = 'http://127.0.0.1:8000/api/'; 

        vm.showPreliminaryForm = true;
        vm.showDetailForm = false;
        vm.showSuccessMessage = false;
        vm.showErrorMessage = false;

        vm.closeMessage = function(){
            console.log("close");
            vm.showPreliminaryForm = true;
            vm.showDetailForm = false;
            vm.showSuccessMessage = false;
            vm.showErrorMessage = false;
        }

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
        }

        function createRegistrant(data){
            $http.post(apiUrl + 'registrants', data)
            .success(function(){
                vm.showDetailForm = true;
            })
            .error(function(response){
                vm.showErrorMessage = true;
            })
            .finally(function(){
                vm.showPreliminaryForm = false;
            });
        }

        function updateRegistrant(registrantID, data){
            $http.put(apiUrl + 'registrants/' + registrantID, data)
            .success(function(){
                vm.showSuccessMessage = true;
            })
            .error(function(response){
                vm.showErrorMessage = true;
            })
            .finally(function(){
                vm.showDetailForm = false;
            });
        }


    }

    angular.module('app')
    .controller('MainCtrl', ['$http', MainCtrl])
    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);

})();
