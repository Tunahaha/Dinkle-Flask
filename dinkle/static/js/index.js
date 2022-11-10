$('#login').click(
function(){
$.ajax({
    type:'GET',
    url:'/index',
    dataType:'json',
    success: () => {
        console.log('Hi');
      },

})})