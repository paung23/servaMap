const getCookie = name => {
    let cookieValue = null;
    if (document.cookie && document.cookie != '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};
const csrftoken = getCookie('csrftoken');

const csrfSafeMethod = method => {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

$.ajaxSetup({
    crossDomain: false,
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        }
    }
});

const follow = (self, account_id, adder_id) => {
    const className = 'active';
    $.ajax('/users/' + account_id + '/follow/' + adder_id, {
        type: 'POST',
        data: {},
        success: () => {
            if (!$(self).hasClass(className)) {
                $(self).addClass(className);
            } else {
                $(self).removeClass(className);
            }
        },
        error: (error) => {
            console.log(error);
            alert('error: ' + error);
        }
    });
};

$(function(){
    $('div.initials').each(element => {
        const dom = $($('div.initials')[element]);
        if(!dom) return;
        const account_id = dom.attr('account_id');
        if(!account_id || account_id === '') return;
        dom.addClass(getProfileColor(account_id));
    });
});

$(document).ready(function() {
    if(!!$('#hiddenCurrent').val() && $('#hiddenCurrent').val() == 'true') {
        $('#isCurrent').prop('checked', true);
    }
})

const shareLocation = () => {
    $.ajax({
            type:'POST',
            url: '/sharelocation',
            data:{
                user_location_latitude: userlat,
                user_location_longitude: userlng,
            },
            success: function(data){
            }
        }
    )
}

///Phyo: This will be useful if we only have addresses instead of lats and longs. But the geocode api is expensive so let's not use it until we need
/**
const convertAddressToCoordinate = (address) => {
    const url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
        + address
        + '&key=AIzaSyCFTuHFFPfi7q74Wokg76xp14SV_VfKNAk';

    $.ajax({
        type: 'GET',
        url: url,
        success: (results) => {
            console.log(results)
        },
        error: (error) => {
            console.log(error);
        }
    })
} */