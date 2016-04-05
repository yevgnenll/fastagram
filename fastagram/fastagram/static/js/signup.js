(function(){
    
    $(document).ready(function(){

        var my_pass = $('#firstpw');
        var check_pw = $('#secondpw');
        var chk_label = $('#checked');
        var signup = $('#signup');

        check_pw.keyup(function(){
            if (my_pass.val() === check_pw.val()) {
                chk_label.text('correct password');                
                signup.prop('disabled', false);
            } else {
                chk_label.text('invalid password').css('font-size', '20px').css('color','#ff1744');

                signup.prop('disabled', true);
            }
        });
    });

})();
