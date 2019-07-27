$(document).ready(function () {
    // Init
    $('.loader').hide();
    $('#result').hide();


    $('#btn-search').click(function () {
        var city = $("#search").val();
        var data = {"city": city};

        // Show loading animation
        $(this).hide();
        $('#result').hide();
        $('.loader').show();

        $.ajax({
            type: 'POST',
            url: '/search',
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            dataType: 'html',
            cache: false,
            processData: false,
            async: true,
            success: function (response) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').html(response);
                $('#btn-search').show();
            },
            error: function (response) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').html("<div><p>Try Again Later</p></div>");
                $('#btn-search').show();

            },
        });
    });

});
