(function(){

    var is_check = true;

    $(document).ready(function(){
        var my_pass = $('#firstpw');
        var check_pw = $('#secondpw');
        var chk_label = $('#checked');

        check_pw.keyup(function(){
            if (my_pass.val() === check_pw.val()) {
                chk_label.text('correct password').removeClass('check_user_data');
                is_check = false; 
            } else {
                chk_label.text('invalid password').addClass('check_user_data');
                is_check = true;
            }
        });
    });

    $(document).ready(function(){
        $('#signup').click(function(){
            if(is_check){
                $('#signup').disabled = true;
            }
        });
        
    });
})();
