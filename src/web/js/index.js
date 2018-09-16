homepage = true;

document.addEventListener("DOMContentLoaded", function() {
    $("#page2").hide();
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#out').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imgInp").change(function(){
        readURL(this);
        sendImg(this.files[0]);
        if (homepage===true) {

            goToPicPage();
        }

    });

    function sendImg(pic) {
        formdata = new FormData();
        if (formdata) {
            formdata.append("image", pic);
            jQuery.ajax({
                url: "destination_ajax_file.php",
                type: "POST",
                data: formdata,
                processData: false,
                contentType: false,
                success:function(data){
                    //Assuming i receive an array of .jpg images here

                }
            });
        }
        /*
        $.ajax({
            type: "POST",
            url: url,
            data: data,
            success: success,
            dataType: dataType
        });
        */
    }

    function goToPicPage() {
        $("#startPic").hide();
        $("#page2").show();

    }

    function createColorSelectors() {
        var t = $.template('<div><img src="${url}" />${name}</div>');

        $(selector).append( t , {
            url: jsonObj.url,
            name: jsonObj.name
        });
    }


    //input.files[0]
});



