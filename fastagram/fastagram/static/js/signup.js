(function(){

    var is_check = false;

    $(document).ready(function(){
        var my_pass = $('#firstpw');

        var check_pw = $('#secondpw');
        check_pw.keyup(function(){
            if (my_pass.val() === check_pw.val()) {
                $('#checked').text('correct password').css('font-size', '20px');
                is_check = true;
            } else {
                $('#checked').text('invalid password').css('font-size', '20px');
                is_check = false;
            }
        });
    });
    $(document).ready(function(){
    

        $('#signup').click(function(){

            if(is_check===false){
                alert("password isn't true");
                return false;
            }
        });
        
    });

})();
