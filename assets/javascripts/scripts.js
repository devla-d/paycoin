jQuery(document).ready(function() {
      /* csrf token */
      function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        headers: {
            "X-CSRFToken": csrftoken
        }
    });

    /*------------------
        Preloader
    --------------------*/
    $( window ).on( "load" , function() {
        $( "#preloader" ).delay( 2000 ).fadeOut("slow");
    });

        // Get all dropdowns on the page that aren't hoverable.
        const dropdowns = document.querySelectorAll('.dropdown:not(.is-hoverable)');

        if (dropdowns.length > 0) {
        // For each dropdown, add event handler to open on click.
        dropdowns.forEach(function(el) {
            el.addEventListener('click', function(e) {
            e.stopPropagation();
            el.classList.toggle('is-active');
            });
        });

        // If user clicks outside dropdown, close it.
        document.addEventListener('click', function(e) {
            closeDropdowns();
        });
        }

        /*
        * Close dropdowns by removing `is-active` class.
        */
        function closeDropdowns() {
        dropdowns.forEach(function(el) {
            el.classList.remove('is-active');
        });
        }

        // Close dropdowns if ESC pressed
        document.addEventListener('keydown', function (event) {
        let e = event || window.event;
        if (e.key === 'Esc' || e.key === 'Escape') {
            closeDropdowns();
        }
        });
  



        /*    $('.registerform').on('submit',(e)=>{
            e.preventDefault();

           

            $("#ajax-loader").toggle();

            var formdata = {
                fullname : $('#id_fullname').val(),
                username : $('#id_username').val(),
                email : $('#id_email').val(),
                password1 : $('#id_password').val(),
                password2 : $('#id_password2').val(),
            }
            console.log(formdata)
            $.ajax({
                type: "POST",
                url: "/register/",
                data: formdata,
                beforeSend: function() {
                    
                },
                success: function(data) {
                    
                     console.log(data)
                     if (data.error) {
                        bulmaToast.toast({
                            message: `Error`  ,
                            type: 'is-danger',
                            dismissible: true,
                            position: 'bottom-right',
                            animate: { in: 'fadeIn', out: 'fadeOut' },
                            duration: 8000,
                            pauseOnHover: true,
                            forceDestroy  : true
                    
                        })
                     }
     
                },
                complete: function() {
                     $("#ajax-loader").toggle();
                    
                },
            }); */



        
        
        
        
        
        
 }); 