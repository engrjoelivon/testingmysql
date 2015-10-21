
           function myfunction()
           {

             // datatypes
             var numb=0;
             var num;
             var text=" The lenght of your name is: ";
             var str=" i am here now";

             str= prompt("what is your name :");
             alert(text+ str.substring(0,4));


            var addition=function(a )
           {
             try {

        x = Number(a);
        if(x === "") throw "is empty";
        if(isNaN(x)) throw "is not a number";
        if(x > 10) throw "is too high";
        if(x < 5) throw "is too low";
    }
    catch(err) {
        alert(err);

    }



           };

           addition(1);

           }



