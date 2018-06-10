$(function() {

    $(document).on("click", ".upvote-link", function(e){
        var self = $(this);
        $.ajax({
            type: "POST",
            url: "/product/vote/",
            data: {
                pid: self.data('id'),
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
            },
            success: function(response) {
                var errcode = response.errcode;
                var message = response.message;
                var data = response.data;
                if (errcode === 200) {
                    var $vote = self.find(".vote-count");
                    $vote.text(data.vote_count);
                    self.addClass("upvote-active");
                } else if (errcode === 401) {
                    window.location.href = '/auth/github/';
                } else {
                    alert(message);
                }
            },
            error: function(err) {
                alert(err);
            }
        });
    });

});