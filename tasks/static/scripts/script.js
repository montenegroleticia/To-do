$(document).ready(function () {
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('.search-bnt');
    var searchForm = $('#search-form');

    $(deleteBtn).on('click', function (e) {

        e.preventDefault();

        var deleteLink = $(this).attr('href');
        var result = confirm('Do you want to delete this task?');

        if (result) {
            window.location.href = deleteLink;
        }
    });

    $(searchBtn).on('click', function () {
        searchForm.submit();
    });
});
