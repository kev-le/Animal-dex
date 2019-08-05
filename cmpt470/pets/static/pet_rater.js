// taken from https://codepen.io/depy/pen/vEWWdw
$(document).ready(function(){

    /* 1. Visualizing things on Hover - See next part for action on click */
    $('#stars li').on('mouseover', function(){
        var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on

        // Now highlight all the stars that's not after the current hovered star
        $(this).parent().children('li.star').each(function(e){
        if (e < onStar) {
            $(this).addClass('hover');
        }
        else {
            $(this).removeClass('hover');
        }
        });

    }).on('mouseout', function(){
        $(this).parent().children('li.star').each(function(e){
        $(this).removeClass('hover');
        });
    });


    /* 2. Action to perform on click */
    $('#stars li').on('click', function(){
        var onStar = parseInt($(this).data('value'), 10); // The star currently selected
        var stars = $(this).parent().children('li.star');

        for (i = 0; i < stars.length; i++) {
        $(stars[i]).removeClass('selected');
        }

        for (i = 0; i < onStar; i++) {
        $(stars[i]).addClass('selected');
        }

        // JUST RESPONSE (Not needed)
        var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
        var msg = "";
        if (ratingValue > 1) {
            msg = "Thanks! You rated this " + ratingValue + " stars.";
        }
        else {
            msg = "We will improve ourselves. You rated this " + ratingValue + " stars.";
        }
        responseMessage(msg);

        // POST RESPONSE AJAX
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                // if not safe, set csrftoken
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            type: 'post',
            url: "{% url 'rate' %}",
            data: {
                'rating': JSON.stringify(ratingValue),
                'petId' : "{{ pet.id }}"
            },
            dataType: 'json',
            success: function (res, status) {
                // alert(res);
                // alert(status);
            },
            error: function (res) {
                // alert(res.status);
            }
        });

    });


});


function responseMessage(msg) {
    $('.success-box').show(200);
    $('.success-box').fadeIn(300);
    $('.success-box div.text-message').html("<span>" + msg + "</span>");
}
