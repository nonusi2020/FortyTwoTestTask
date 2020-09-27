$(function() {
    var ajaxOptions = {
        target: "#result",
        dataType: "json",
        beforeSubmit: function() {
            $("update_contact :input").prop("disabled", true);
        },
        success: function(data) {
            $("#result").addClass("alert-success").text("Contact " + data.name + "  updated successfully");
            $("#id_photo").val("");
            $("#id_photo-clear").prop("checked", false);
        },
        error: function(data) {
            var errors = 'Please Check these errors <br>';
            var i = 1;
            for (datos in data.responseJSON) {
                errors += i + '. ' + datos + ':' + data.responseJSON[datos] + '<br>';
                i = i + 1;
            }
            $('#result1').addClass("alert-danger").show().html(errors);
            $("#result").addClass("alert-danger").text("Changes not saved");
        }
    };

    $("#id_photo-clear").on("click", function() {
        if ($("#id_photo-clear").is(":checked")) {
            $("#photo_url").attr("src", "");
            $("#id_photo").val("");

        }
    });

    function resetErrors() {
        $("#result1").removeClass("alert-danger").text("");
        $("#result").removeClass("alert-danger alert-success").text("");
    }

    $("#update_contact").on("submit", function(e) {
        e.preventDefault();
        resetErrors();
        $(this).ajaxSubmit(ajaxOptions)
    });

    options = {
        custom: {
            dateofbirth: function($el) {
                console.debug("inside dob validation" + $el.val());
                var isDate = !!Date.parse($el.val()),
                    curDate = new Date(new Date().setHours(0, 0, 0, 0));
                var inputValue = new Date($el.val());
                var result = inputValue > curDate;
                if (!isDate) {
                    return "Date is invalid!!.";
                }
                if (result) {
                    return "Date is invalid!.";
                }
            }
        }
    };

    $("form").validator(options);

    $("#id_dateofbirth").datepicker({
        changeMonth: true,
        changeYear: true,
        dateFormat: "yy-mm-dd",
        yearRange: "1900:2100"
    });

    $("#id_photo").on("change", function(e) {
        var input = this;
        if (input.files && input.files[0]) {
            console.debug("inside first if")
            var reader = new FileReader(),
                picture = $(".picture");

            reader.onload = function(e) {
                console.debug("reader.onload")
                picture.css("max-width", 200);
                picture.css("max-height", 200);
                $("#photo_url").attr("src", e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    });
});