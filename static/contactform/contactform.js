jQuery(document).ready(function($) {
  "use strict";

  //Contact
  $('form.contactForm').submit(function() {
    var f = $(this).find('.form-group'),
      ferror = false,
      emailExp = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;

    f.children('input').each(function() { // run all inputs

      var i = $(this); // current input
      var rule = i.attr('data-rule');

      if (rule !== undefined) {
        var ierror = false; // error flag for current input
        var pos = rule.indexOf(':', 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1, rule.length);
          rule = rule.substr(0, pos);
        } else {
          rule = rule.substr(pos + 1, rule.length);
        }

        switch (rule) {
          case 'required':
            if (i.val() === '') {
              ferror = ierror = true;
            }
            break;

          case 'minlen':
            if (i.val().length < parseInt(exp)) {
              ferror = ierror = true;
            }
            break;

          case 'email':
            if (!emailExp.test(i.val())) {
              ferror = ierror = true;
            }
            break;

          case 'checked':
            if (! i.is(':checked')) {
              ferror = ierror = true;
            }
            break;

          case 'regexp':
            exp = new RegExp(exp);
            if (!exp.test(i.val())) {
              ferror = ierror = true;
            }
            break;
        }
        i.next('.validation').html((ierror ? (i.attr('data-msg') !== undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
      }
    });
    f.children('textarea').each(function() { // run all inputs

      var i = $(this); // current input
      var rule = i.attr('data-rule');

      if (rule !== undefined) {
        var ierror = false; // error flag for current input
        var pos = rule.indexOf(':', 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1, rule.length);
          rule = rule.substr(0, pos);
        } else {
          rule = rule.substr(pos + 1, rule.length);
        }

        switch (rule) {
          case 'required':
            if (i.val() === '') {
              ferror = ierror = true;
            }
            break;

          case 'minlen':
            if (i.val().length < parseInt(exp)) {
              ferror = ierror = true;
            }
            break;
        }
        i.next('.validation').html((ierror ? (i.attr('data-msg') != undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
      }
    });
    if (ferror) return false;
    else var str = $(this).serialize();
    var action = $(this).attr('action');
    if( ! action ) {
      action = 'contactform/contactform.php';
    }
    // $.ajax({
    //   type: "POST",
    //   url: action,
    //   data: str,
    //   success: function(msg) {
    //     // alert(msg);
    //     if (msg == 'OK') {
    //       $("#sendmessage").addClass("show");
    //       $("#errormessage").removeClass("show");
    //       $('.contactForm').find("input, textarea").val("");
    //     } else {
    //       $("#sendmessage").removeClass("show");
    //       $("#errormessage").addClass("show");
    //       $('#errormessage').html(msg);
    //     }
    //
    //   }
    // });

    // Собираем данные из формы
$.getJSON('/api/chat-ids/', function(chat_ids) {
  const telegramMessage =
    "<b>📩 Новое сообщение с сайта</b>\n\n" +
    "<b>👤 Имя:</b> " + $("#name").val() + "\n" +
    "<b>📧 Email:</b> " + $("#email").val() + "\n" +
    "<b>📝 Номер:</b> " + $("#subject").val() + "\n" +
    "<b>💬 Сообщение:</b>\n" + $("textarea[name='Message']").val();

  chat_ids.forEach(chat_id => {
    $.ajax({
      url: "https://api.telegram.org/bot7833910204:AAGamUBw7ujcgEV7LLq8Uxz555-8HR5ZICE/sendMessage",
      method: "POST",
      data: {
        chat_id: chat_id,
        text: telegramMessage,
        parse_mode: "HTML"
      },
      success: function() {
        console.log(`✅ Отправлено в ${chat_id}`);
        $("#sendmessage").fadeIn().delay(4000).fadeOut(); // показываем сообщение об успехе
        $(".contactForm")[0].reset(); // очищаем форму (по желанию)
      },
      error: function(_, __, error) {
        console.error(`❌ Ошибка отправки в ${chat_id}: ${error}`);
      }
    });
  });
});
    return false;
  });

});
