function error(error_message='Warning: something wont wrong, try again !') {
    let alertPopupHtml=`
    <link href="../css/alerts.css" rel="stylesheet">           
    <div class="alert hide">
        <span class="fas fa-exclamation-circle"></span>
        <span class="msg">${error_message}</span>
        <div class="close-btn">
        <span class="fas fa-times"></span>
        </div>
    </div>`

    let content=document.querySelector("#main");
    let alertPopup=document.createElement('div');
    alertPopup.className="alertPopup";
    alertPopup.innerHTML=alertPopupHtml;
    content.appendChild(alertPopup);

    $('.alert').addClass("show");
        $('.alert').removeClass("hide");
        $('.alert').addClass("showAlert");
        setTimeout(function(){
            $('.alert').removeClass("show");
            $('.alert').addClass("hide");
        },5000);
        
        $('.close-btn').click(function(){
        $('.alert').removeClass("show");
        $('.alert').addClass("hide");
        });
};

function send_plant(plant){
    console.log(plant );
    let data={'plant':plant};
    $.ajax({
        'url':'/chosing-plant',
        'method': 'POST',
        'contentType': 'application/json',
        'dataType':'json',
        'data': JSON.stringify(data),
        'sucess':function(data){
            if ('error' in data) error(dara['error']);
        },
        'error': error()
    });
};