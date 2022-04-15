$(function(){ 
        $("#typed").typed({
            strings: ["Good Guy", "Not a Bad Programmer", "Full Stack Web Developer"],
            typeSpeed: 90,
            backDelay: 1000,
            loop: false,
            // defaults to false for infinite loop
            loopCount: false,
            resetCallback: function() { newTyped(); }
        });
        $(".reset").click(function(){
            $("#typed").typed('reset');
        });

    });
    function newTyped(){ /* A new typed object */ }