function alertsmsg(){
   $.ajax({
       url:"controllers/alerts.php",
       success: function(data){
         let info = data.trim();
        if ( info == "unverified" ){
         
          toastr.success('Your email and ID card needs to be verified, check your email for Verification and upload your ID card', 'Verification Needed!', {timeOut: 5000, progressBar:true, closeHtml:'<i class="fa fa-user></i>"'});
                
             
      }else if(info == "welcome"){
       
            

      }  
    }
  }) 
}

function imageupload() {

toastr.success('ID card upload Failed, please try again', 'ID Card Upload Failed!', {timeOut: 5000, progressBar:true, closeHtml:'<i class="fa fa-user></i>"'});
                

}
