$(function() {
    $('#btn_back').click(function() {
        console.log('111')
        history.back(-1);
    });

    $('#btn_manual').click(function() {
        window.open("https://github.com/kkoonz/django/wiki/%EB%B0%94%EB%A1%9C-%EC%93%B0%EB%8A%94-%EC%9E%A5%EA%B3%A0");
    });
});