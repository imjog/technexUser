var data = [
{
parentEvent: 'ascension',
events:['momentum', 'la-trajectoire', 'daeroglisseur', 'drone-tech'],
max:[5,5,5,5]
},
{
parentEvent: 'modex',
events:['open-simulation', 'open-hardware', 'open-software'],
max:[5,5,5,]
},
{
parentEvent: 'pahal',
events:['greenx', 'vision', 'swachch', 'sampann', 'aagaz'],
max:[5,5,5,5,5]
},
{
parentEvent: 'supernova',
events:['scientists-utopia', 'astrophotography', 'astroquiz', 'exploring-interstellar',],
max:[5,5,5,5,]
},
{
parentEvent: 'creatrix',
events:['minimize', 'iso', 'collage', 'avant-garde', 'animaze', '2d'],
max:[5,5,5,5,5,5]
},
{
parentEvent: 'riqueza',
events:['analiticity', 'bulls-floor', 'krackat', 'manthan', 'conundrum'],
max:[5,5,5,5,5,5]
},
{
parentEvent: 'byte-the-bits',
events:['mlware', 'international-coding-marathon', 'appathon', 'capture-the-flag'],
max:[5,5,5,1]
},
{
parentEvent: 'extreme-engineering',
events:['bridgeit', 'goldbergs-alley', 'axelerate', 'hydracs'],
max:[5,5,5,5]
},
{
parentEvent: 'robonex',
events:['robowars', 'pixelate', 'hurdlemania', 'mazeXplorer'],
max:[5,5,5,5]
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

var app = angular.module('evnt', []);

app.controller('evnt-control', ['$scope', '$window', function($scope, $window) {
  $scope.parentEvent = '';
  $scope.max=0;
  $scope.a = [];
  $scope.options = $window.data;
  $scope.counter = 0;
  $scope.members = [];
  $scope.parentEventIndex = function(){
  	return findWithAttr($scope.options,'events',$scope.parentEvent);
  };
  $scope.addMember = function(){
  	if($scope.counter < $scope.max)
  	$scope.members.push($scope.counter++);
  
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

  }]);
