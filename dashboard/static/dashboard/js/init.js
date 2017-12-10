$(document).ready(
    function(){
        var socket = new WebSocket("ws://" + window.location.host + "/dashboard/");
        socket.onopen = function() {
            socket.send("init");
        };
        socket.onmessage = function(e) {
            $('#thermometer .scale').height(41 + 2 * e.data);
            $('#temperature span').text(e.data);
            console.info('Температура: ' + e.data + ' по Цельсию');
        };
        // Click by reset
        $('#reset').on('click', function(){
            socket.send("init");
        });
    }
);