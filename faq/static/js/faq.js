$(function() {
    $('#btn_back').click(function() {
        console.log('111')
        history.back(-1);
    });

    $('#btn_manual').click(function() {
        window.open("https://github.com/kkoonz/django-helpdesk/wiki");
    });
});