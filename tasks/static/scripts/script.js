$(document).ready(function () {
    let baseURL = 'http://127.0.0.1:8000/';
    let filter = $('#filter');
    let deleteBtn = $('.delete-btn');
    let searchBtn = $('.search-bnt');
    let searchForm = $('#search-form');

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

    $(filter).change(function () {
        let filter = $(this).val();
        window.location.href = baseURL + '?filter=' + filter;
    })
});
