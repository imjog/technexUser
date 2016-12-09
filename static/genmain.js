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

var app = angular.module('evnt', ['ngRoute']);

app.config(function ($routeProvider) {
             
            $routeProvider.when('/eventReg/', {
 templateUrl: '/static/dash/teamregister.html',
 controller: 'evnt-control',
                
            }).when('/profile/', {
               
                               templateUrl:'/static/profile.html',
                               controller:'profileEdit',
                
            }).when('/changepassword/',{
              templateUrl:'/static/changepassword.html',
              controller:'changepass'
            }).when('/startupreg/',{
                   templateUrl:'/static/startupreg.html'
            }).
            otherwise({
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
   
   $scope.removeerror = function(z){
     var x=document.getElementsByClassName("abcd");
     var y=document.getElementsByClassName("parsley-errors-list");
     $(x[z]).removeClass("parsley-error");
     $(x[z]).removeClass("input-error");
     $(y[z+1]).hide();
   };
  $scope.update = function(){

  	try{ 
  	$scope.max = $scope.options[$scope.parentEventIndex()].max[$scope.parentEvent.indexOf($scope.selectedevent)];
  	$scope.a  = new Array($scope.max);
        while($scope.members.length!=0)
    {
        $scope.members.pop();    
    }
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
     $(".team-reg-submit").html("Submitting. Please Wait!")
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
      "teamLeaderEmail":$scope.leader
     }
   console.log(data);
     
    $http({
      method: 'POST',
      url : '/events/register/',
      data : data
    })
    .success(function(data){
        console.log(data);
        if(data.status==1)
        {
           $scope.parentEvent='robonex';
          $scope.parentEvent='-- Select Parent Event --';
          $(".team-reg-submit").html("Submit");
          $("#error-message").css('background','green')
          $("#error-message-display").html("Team successfully Registered");
          $("#error-message").show();
        }
        if(data.status==0)
        {
           $("#error-message").css('background','#e88a83')
          $("#error-message-display").html(data.error);
          $("#error-message").show();
          $(".team-reg-submit").html("Submit");
        }
    })
  };


  }]);

app.controller("profileEdit",function($scope, profileData,$http){

        $scope.editIndex = -1;
        $scope.editObject =   {
            name: "",
                technexId: "",
                college: "",
                year: "",
                city: "",
                email: "",
                mobile: ""
        };
        $scope.teamArray = profileData.getTeamData();
        $scope.employeeArray = profileData.getStaffArray();
        $scope.position = function(data){
          var x=parseInt(data);
          switch(x)
          {
            case 1:
            return "Freshmen";
            case 2:
            return "Sophomore";
            case 3:
            return "Junior";
            case 4:
            return "Senior";
            case 5:
            return "Senior";
            default:
            return "Student";
          }
        }

        //edit button click
        $scope.editingPerson = function(personIndex){
            $scope.editObject = angular.copy($scope.employeeArray[personIndex]);
            $scope.editIndex = personIndex;
        };
        $scope.rmcls = function(){
          $("input").removeClass("parsley-error");
          $(".parsley-errors-list").hide();
          $("errormsg").hide();

        } 

        //cancelEdit
        $scope.cancelEdit = function(){
            $scope.editIndex = -1;

        };

        //saveEdit
        $scope.saveEdit = function(personIndex){
          console.log(personIndex);
          var cdata = JSON.stringify($scope.editObject);
          console.log(cdata);
          var y=true;
             if(y)
             {
              if($("#forname").val()=="")
              {
                $("#forname").addClass("parsley-error");
                y=false;
              }
                if($("#forcollege").val()=="")
                {
                   $("#forcollege").addClass("parsley-error");
                y=false;
                }
                if($("#forcollegeyear").val()=="" || (isNaN(parseInt($("#forcollegeyear").val()))))
                {
                  $("#forcollegeyear").addClass("parsley-error");
                  y=false;  
                }
                if(!(isNaN(parseInt($("#forcollegeyear").val()))))
                {
                   var x=parseInt($("#forcollegeyear").val());
                  if(x>5 || x<1)
                  {
                    $("#forcollegeyear").addClass("parsley-error");
                    $("#collegeyearerr").show();
                    y=false;
                  }
                }
                if($("#forcity").val()=="")
                {
                  $("#forcity").addClass("parsley-error");
                  y=false;
                }
                if($("#formobile").val()=="")
                {
                  $("#formobile").addClass("parsley-error");
                  y=false;
                }
                if($("#formobile").val()!="")
                {
                  num=$("#formobile").val();
                  if((num.length!==10) || (isNaN(parseInt(num))) || (parseInt(num).toString().length  != num.length))
                   {
                       
                       $("#formobile").addClass("parsley-error");
                       $("#mobileerr").show();
                       y=false;
                   }

                }



             }
              
           if(y)
           {   
              $http({
      method: 'POST',
      url : '/updateProfile/',
      data : cdata
    })
    .success(function(data){
        console.log(data);
        if(data.status==1)
        {
            profileData.updateInfo(personIndex, $scope.editObject);
            $scope.editIndex = -1;   
        }
        if(data.status==0)
        {
           console.log('Could not save Data!!!');
        }
    });
            
         }   
        };
    });

app.controller("changepass",function($scope,$http){

  $scope.oldpass="";
  $scope.newpass="";
  $scope.cnewpass="";

   $scope.submit = function(){
    var y=true;
    if($scope.oldpass=="")
    {
      $("#old-pass").addClass("input-error"); 
      y=false; 
    }
    if(y)
    {
      if($scope.newpass=="")
      {
        $("#new-pass").addClass("input-error");
        y=false;
      }
     }
     if(y)
     {
      if($scope.cpass=="")
      {
        $("#confirm-new-pass").addClass("input-error");
        y=false;
      }
     }
     if(y)
     {
      if($scope.cnewpass!=$scope.newpass)
      {
        $("#confirm-new-pass").addClass("parsley-error");
        $("#pass-match-error").show();
        y=false;
      }
     }
     if(y)
     {
       data={
        "oldPass":$scope.oldpass,
       "newPass":$scope.newpass
     };
       $http({
        method: 'POST',
        url: '/resetpassword/',
        data: data
       }).success(function(data){
        if(data.status==1)
        {
          
        }
        if(data.status==0)
          {

            $("#resetpasserr").html(data.error);
            $("#resetpasserrmsg").show();
          }
       });

     }

    }
});

