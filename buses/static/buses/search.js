$(document).ready(function(){
    var csrf_token =  $('input[name=csrfmiddlewaretoken]').val();

    $("#id_source").on('keyup click',function(){
        var source = $(this).val();

        if(source != ''){
            $.ajax({
                type: 'POST',
                url: '/ajax/stoppage/',
                //contentType: 'application/json',
                data: {
                    'stoppage': source,
                    'csrfmiddlewaretoken': csrf_token
                },
                dataType: 'json',
                success: function(data){
                    var stoppages = data.data;
                    var len = stoppages.length;
                    var inner = '';

                    for(i = 0; i < len; i++){
                        inner += '<li>' + stoppages[i].name + '</li>';
                    }

                    $("#source-results").html(inner);
                },
                failure: function(data){
                    alert('Error!');
                }
            });
        }
        else{
            $("#source-results").html('');
        }
    });

    $("#id_destination").on('keyup click',function(){
        var destination = $(this).val();

        if(destination != ''){
            $.ajax({
                type: 'POST',
                url: '/ajax/stoppage/',
                //contentType: 'application/json',
                data: {
                    'stoppage': destination,
                    'csrfmiddlewaretoken': csrf_token
                },
                dataType: 'json',
                success: function(data){
                    var stoppages = data.data;
                    var len = stoppages.length;
                    var inner = '';

                    for(i = 0; i < len; i++){
                        inner += '<li>' + stoppages[i].name + '</li>';
                    }

                    $("#destination-results").html(inner);
                },
                failure: function(data){
                    alert('Error!');
                }
            });
        }
        else{
            $("#destination-results").html('');
        }
    });

    // on() method because li elements are dynamically created
    $("#source-results").on('click', 'li', function(){
        $("#id_source").val( $(this).html() );
        $("#source-results").html('');
    });

    // on() method because li elements are dynamically created
    $("#destination-results").on('click', 'li', function(){
        $("#id_destination").val( $(this).html() );
        $("#destination-results").html('');
    });

    $("#search-form").submit( function(e){
        e.preventDefault();
        
        var source = $("#id_source").val();
        var destination = $("#id_destination").val();

        $.ajax({
            type: 'POST',
            url: '/ajax/search/',
            //contentType: 'application/json',
            data: {
                'source': source,
                'destination': destination,
                'csrfmiddlewaretoken': csrf_token
            },
            dataType: 'json',
            success: function(data){
                
                var inner;
                
                if(data.error == 1){
                    $("#search-results").html('');
                    $("#error").html('<div class="error-item mt-5">Source not found! Try again.</div>');
                }
                else if(data.error == 2){
                    $("#search-results").html('');
                    $("#error").html('<div class="error-item mt-5">Destination not found! Try again.</div>');
                }
                else if(data.error == 3){
                    $("#search-results").html('');
                    $("#error").html('<div class="error-item mt-5">Source and destination not found! Try again.</div>');
                }
                else if(data.error == 4){
                    $("#search-results").html('');
                    $("#error").html('<div class="error-item mt-5">Enter valid data!</div>');
                }
                else{
                    $("#error").html('');
                    var buses = data.data;
                    var len = buses.length;

                    if(len > 0){
                        var i;
                        inner = '<h4 class="text-center mt-5 mb-4">Search Results</h4>';
                        for(i = 0; i < len; i++){
                            inner += '<a href="/bus/' + buses[i].pk + '"class="buslist-item text-center">' +
                                '<p class="buslist-name">' + buses[i].name + '</p>' +
                                '<p class="buslist-route">(' + buses[i].start + ' - ' + buses[i].stop + ')</p></a>';
                        }
                    }
                    else{
                        inner = '<h4 class="text-center mt-5">No bus to show</h4>';
                    }

                    $("#search-results").html(inner);
                }
            },
            failure: function(data){
                alert('Error!');
            }
        });
    });
    
    $(document).click( function(e){
        var sl = $("#source-results");
        var dl = $("#destination-results");
        var si = $("#id_source");
        var di = $("#id_destination");

        // if the target of the click isn't the container nor a descendant of the container
        // also if the corresponding input isn't the target
        if (!sl.is(e.target) && sl.has(e.target).length === 0 && !si.is(e.target)){
            sl.html('');
        }
        if (!dl.is(e.target) && dl.has(e.target).length === 0 && !di.is(e.target)){
            dl.html('');
        }
    });
});