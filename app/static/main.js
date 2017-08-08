

$(document).ready(function() {

    // initial page size
    let browserWidth = $(window).width();
    let percentFromTop = 0.45
    let desiredMargin = browserWidth * percentFromTop;
    // console.log('Starting WIDTH: ', browserWidth);
    // console.log('Starting MARGIN: ', desiredMargin);

    // as page size changes
    $(window).on('resize', function(){
        if($(this).width() != browserWidth){
            browserWidth = $(this).width();
            desiredMargin = $(this).width() * percentFromTop;
            // console.log('WIDTH: ', browserWidth);
            // console.log('MARGIN: ', desiredMargin);
            location.reload();
        }
    });
    $('#logo_spacing').css('margin-top', desiredMargin);
});
