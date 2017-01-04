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
var workdata=[
{
  workshop: 'Internet of things',
  max: 3
},
{
  workshop: 'Industrial Automation -PLC & SCADA',
  max: 1
},
{
  workshop: 'Data Mining',
  max: 1
},
{
  workshop: 'Digital Marketing',
  max: 1
},
{
  workshop: '3 D Printing',
  max: 1
},
{
  workshop: 'Swarm Robotics',
  max: 1
},
{
  workshop: 'Bridge Design',
  max: 1
},
{
  workshop: 'Android App Development',
  max: 1
},
{
  workshop: 'Sixth sense Technology',
  max: 1
},
{
  workshop: 'automobiles',
  max: 1
},
{
  workshop: 'Ethical Hacking',
  max: 1
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
            })

            .when('/eventReg/:param1/:param2',
              {
                templateUrl: '/static/dash/teamregister.html',
                controller: 'evnt-control',
              }

            )

            

           .when('/startupreg/',{
                   templateUrl:'/static/startupreg.html',
                   controller:'startup-cont'
            })
            .when("/",{
                  templateUrl:'/static/profile.html',
                  controller:'profileEdit',
              })
            .when("/dashhome/",{
                templateUrl: '/static/dashhome.html',
              }).when("/workshopreg/",{
                templateUrl: '/static/workshopreg.html',
                controller: 'workshop-cont',
              })
            .when('/workshopreg/:param1/',
              {
                templateUrl: '/static/workshopreg.html',
                controller: 'workshop-cont',
              }

            )
            
            .otherwise({
                redirectTo: "/"
            });

    });

app.controller('evnt-control', ['$scope', '$window', '$http' ,'$routeParams', function($scope, $window,$http,$routeParams) {
   console.log("hi");
   var param1 = $routeParams.param1;
   var param2 = $routeParams.param2;

   console.log(param1+'  '+param2);
  $scope.parentEvent = '';

  $scope.max=0;
  $scope.a = [];
  $scope.options = $window.data;
  $scope.parentEventIndex = function(){
    return findWithAttr($scope.options,'events',$scope.parentEvent);
  };
  if (param1){
    $scope.parentEvent = $.grep($scope.options,function(n,i){ return n.parentEvent == param1})[0].events;
    $scope.selectedevent = param2;
    $scope.max = $scope.options[$scope.parentEventIndex()].max[$scope.parentEvent.indexOf($scope.selectedevent)];
  }
  $scope.counter = 0;
  $scope.members = [];
  $scope.user;
  $scope.leader = document.getElementById('userEmail').value;
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
          location.reload(true);
          window.location.assign("#profile");
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
        console.log("skjdjfi");
        console.log($scope.teamArray.length);
        $scope.employeeArray = profileData.getStaffArray();
        $scope.profileEmail = document.getElementById('userEmail').value;
        
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

        $scope.deleteTeam = function(index)
        {
      $http({
      method: 'POST',
      url : '/events/teamDelete/',
      data : {"identifier":$scope.teamArray[index].teamId}
    })
    .success(function(data){
        console.log(data);
        if(data.status==1)
        {
          $scope.teamArray.splice(index,1);
        }
        if(data.status==0)
        {
           console.log('Could not be Deleted!!!');
        }
    });
        };

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
            console.log($scope.editObject.name);
            makeimg($scope.editObject.name);
            $("#user_name").html($scope.editObject.name);
           // location.reload(true);
           // window.location.assign("#profile");  
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
           location.reload(true);
           window.location.assign("#profile");
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



app.controller('startup-cont', ['$scope', '$window', '$http' , function($scope, $window,$http) {
  $scope.a = [];
  $scope.options = $window.data;
  $scope.counter = 0;
  $scope.members = [];
  $scope.user;
  $scope.ideas="";
  $scope.teamName="";
  $scope.leader = document.getElementById('userEmail').value;
  $scope.parentEventIndex = function(){
    return findWithAttr($scope.options,'events',$scope.parentEvent);
  };
  $scope.addMember = function(){
    $scope.members.push($scope.counter++);
    };
  $scope.removeMember = function(z){
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
   $scope.membervalid= function(data)
   {
     var id=data.trim();
    var tid=id.length==7 && id.substring(0,2)=="TX" && !isNaN(parseInt(id.substring(2)));
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
       console.log("////");
       console.log(tid);
      var email=re.test(id)
       return (email || tid);  
   }
  $scope.submitForm = function(event)
  {

     var x=true;
     console.log($scope.teamName);
     if($scope.teamName=="")
     {
      $("#teamName").addClass("input-error");
      x=false;
      console.log("empty");
     }
     if(x)
     {
       if($scope.ideas=="")
       {
        $("#ideas").addClass("input-error");
        x=false;
       }
     }
     if(x)
     {
      if($scope.leader=="")
      {
        $("#team-leader").addClass("input-error");
        x=false;
      }
     }
     if(x)
     {
      if(!$scope.membervalid($("#team-leader").val()))
      {
        $("#team-leader").addClass("parsley-error");
        $("#team-leader-invalid").show();
        x=false;
      }
     }
     var z=$(".abcd");
     var z1=$(".parsley-errors-list");
     if(x)
     {
       var i;
       
       for(i=0;i<z.length;i++)
       {
          if($(z[i]).val()=="")
          {
            $(z[i]).addClass("input-error")
            x=false;
          }

       }
     }
     if(x)
     {
       var i;
       for(i=0;i<z.length;i++)
       {
        if(!$scope.membervalid($(z[i]).val()))
        {
          $(z[i]).addClass("parsley-error");
          $(z1[i+1]).show();
          x=false;
        }
       }
     }
      
      if(x)
      {
             $(".team-reg-submit").html("Submitting. Please Wait!");
             data={
              "idea": $scope.ideas,
              "teamName":$scope.teamName,
              "memberMails":$scope.a,
              "teamLeader":$scope.leader
             }
             $http({
              method:'POST',
              url:'/startupregister/',
              data: data
             }).success(function(data){
              $(".team-reg-submit").html("Submit");
              console.log(data);
                if(data.status==0)
                {
                   $("#error-message-display").html(data.error);
                   $("#error-message").show();
                   
                }
                if(data.status==1)
                {
                   
                   window.location.assign("#profile");
                   location.reload(true);
                }
             });


      }
  };
  

  }]);
app.controller('workshop-cont', ['$scope', '$window', '$http','$routeParams' , function($scope, $window,$http,$routeParams) {
   var param1 = $routeParams.param1;
   //var param2 = $routeParams.param2;
  $scope.max=0;
  $scope.a =[];
  $scope.options = $window.workdata;
  $scope.workshop='';
  $scope.teamName="";
  $scope.counter = 0;
  $scope.members = [];
  if (param1){
    $scope.workshopObject = $.grep($scope.options,function(n,i){ return n.workshop == param1})[0];
    $scope.workshop = param1;
    $scope.max = $scope.workshopObject.max;
  }
  $scope.leader = document.getElementById('userEmail').value;
    $scope.membervalid= function(data)
   {
     var id=data.trim();
    var tid=id.length==7 && id.substring(0,2)=="TX" && !isNaN(parseInt(id.substring(2)));
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
       console.log("////");
       // console.log(tid);
      var email=re.test(id)
       return (email || tid);  
   }
    $scope.workshopIndex = function(){
      console.log($scope.options);
      console.log($scope.workshop);
      // console.log($scope.options);
    return findWithAttr($scope.options,'workshop',$scope.workshop);
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
      console.log($scope.max);

    try{ 
    $scope.max = $scope.options[$scope.workshopIndex()].max;
    console.log($scope.workshopIndex());
    $scope.a  = new Array($scope.max-1);
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
  $scope.removeerror = function(z){
     var x=document.getElementsByClassName("abcd");
     var y=document.getElementsByClassName("parsley-errors-list");
     $(x[z]).removeClass("parsley-error");
     $(x[z]).removeClass("input-error");
     $(y[z+1]).hide();
   };
  $scope.submitForm = function(event)
  {
    // console.log($scope.a);
    console.log($scope.teamName);
    var x=true;
    if(x)
    {
       // console.log($scope.workshop);
      if($scope.workshop =="" || $scope.workshop==null)
        {x=false;
          $("#parentevent").addClass("input-error");
        }
    }
    if(x)
    {
       if($scope.max!=1)
       {
        if($scope.teamName=="")
        {
           x=false;
          $("#teamName").addClass("input-error");
           }
       }

    }
     if(x)
     {
      if($scope.leader=="")
      {
        $("#team-leader").addClass("input-error");
        x=false;
      }
     }
     if(x)
     {
      if(!$scope.membervalid($("#team-leader").val()))
      {
        $("#team-leader").addClass("parsley-error");
        $("#team-leader-invalid").show();
        x=false;
      }
     }
     var z=$(".abcd");
     var z1=$(".parsley-errors-list");
     if(x)
     {
       var i;
       
       for(i=0;i<z.length;i++)
       {
          if($(z[i]).val()=="")
          {
            $(z[i]).addClass("input-error")
            x=false;
          }

       }
     }
     if(x)
     {
       var i;
       for(i=0;i<z.length;i++)
       {
        if(!$scope.membervalid($(z[i]).val()))
        {
          $(z[i]).addClass("parsley-error");
          $(z1[i+1]).show();
          x=false;
        }
       }
     }
     if(x)
     {
       console.log($scope.a);
       data={
        'workshopSlug':$scope.workshop,
        'teamName': $scope.teamName,
        'teamLeaderEmail': $scope.leader,
        'members':$scope.a
       }
        $http({
              method:'POST',
              url:'/workshopRegister/',
              data: data
             }).success(function(data){
              $(".team-reg-submit").html("Submit");
              console.log(data);
                if(data.status==0)
                {
                   $("#error-message-display").html(data.error);
                   $("#error-message").show();
                   
                }
                if(data.status==1)
                {
                   
                   window.location.assign("#profile");
                   location.reload(true);
                }
             });
     }

  }

}]);





