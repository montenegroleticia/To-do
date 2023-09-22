$(document).ready(function () {
    var deleteBtn = $('.delete-btn');

    $(deleteBtn).on('click', function (e) {

        e.preventDefault();

        var deleteLink = $(this).attr('href');
        var result = confirm('Do you want to delete this task?');

        if (result) {
            window.location.href = deleteLink;
        }
    });
})
