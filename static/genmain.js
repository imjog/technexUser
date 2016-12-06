var data = [
{
parentEvent : 'robonex',
events:[
'chut',
'land'
],
max:[
4,5
]
},
{
parentEvent : 'chutkeChantre',
events:[
'bhanseKeLund',
'ghodeKeTatte'
],
max:[
2,3
]
}
];
function findWithAttr(array, attr, value) {
	
    for(var i = 0; i < array.length; i += 1) {
        if(array[i][attr] === value) {
            return i;
        }
    }
    return -1;
}

var app = angular.module('evnt', ['ngRoute']);

app.config(function ($routeProvider) {
             
            $routeProvider.when('/eventReg/', {
 templateUrl: '/static/dash/teamregister.html',
 controller: 'evnt-control',
                
            }).when('/profile/', {
               
                               templateUrl:'/static/profile.html',
                
            }).otherwise({
                redirectTo: "/"
            });

    });

app.controller('evnt-control', ['$scope', '$window', '$http' , function($scope, $window,$http) {
   console.log("hi");
  $scope.parentEvent = '';
  $scope.max=0;
  $scope.a = [];
  $scope.options = $window.data;
  $scope.counter = 0;
  $scope.members = [];
  $scope.user;
  $scope.leader = document.getElementById('userEmail').value;
  $scope.parentEventIndex = function(){
  	return findWithAttr($scope.options,'events',$scope.parentEvent);
  };
  $scope.addMember = function(){
  	if($scope.counter < $scope.max)
  	$scope.members.push($scope.counter++);
  console.log($scope.a);
  	};
  $scope.removeMember = function(z){
    console.log(z);
  	$scope.members.splice(z,1);
  	$scope.a.splice(z,1);
  	$scope.counter--;
  };
  $scope.update = function(){

  	try{ 
  	$scope.max = $scope.options[$scope.parentEventIndex()].max[$scope.parentEvent.indexOf($scope.selectedevent)];
  	$scope.a  = new Array($scope.max);
    //     while($scope.members.length!=0)
    // {
    //     $scope.members.pop();    
    // }
    $scope.members=[];
    $scope.counter=0;
  	return false;
  }
  catch(err){
  	$scope.max = 0;$scope.counter = 0;
  	return false;
  }
  };
  $scope.submitForm = function(event)
  {
     var c = new Array();
     var i;
     for(i=0;i<$scope.counter;i++)
     {
       c.push($scope.a[i]);
     }
     data = {
      "eventSlug":$scope.selectedevent,
      "teamName":$scope.teamName,
      "members":c,
      "teamLeaderEmail":'bikram.bharti99@gmail.com'
     }
   console.log(data);
     
    $http({
      method: 'POST',
      url : '/events/register/',
      data : data
    })
    .success(function(data){
        console.log(data);
    })
  };


  }]);


    $(document).ready(function(){

console.log("hi");
   $('.team-reg-submit').on("click",function(){
   //    var x=$(".abcd");
   //    var y=true;
   //    var team_name=$(".teamName").val();
   //    console.log(x);
   //    console.log(y);

   // angular.element(document.getElementById('body')).scope().submitForm();
   console.log("hi");
   });


});