homepage = true;
picAndColor = {

}

document.addEventListener("DOMContentLoaded", function() {
    $("#page2").hide();
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function(e) { //This event is triggered each time the reading operation is successfully completed.
                //alert(e.target.result);
                $('#out').attr('src', e.target.result);
                sendImg(e.target.result);
                picAndColor["red"] = e.target.result;
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imgInp").change(function(){
        readURL(this);
        //picAndColor["red"] = this.files[0];
        //alert(this.files[0]);
        //alert(picAndColor.red);
        if (homepage===true) {
            goToPicPage(picAndColor);
        }

    });

    function sendImg(pic) {

        $.get("https://reqres.in/api/users", function(data, status){
            console.log("Inside callback");
            //alert("Data: " + data + "\nStatus: " + status);
        });

        console.log("Before ajax");

        $.ajax({
            url: "10.230.212.179:5000/climb/api2/"
        }).then(function(data) {
            console.log("hello!!!");
            console.log(data);
        });

        console.log("Sending img");
        console.log(pic);
        /*
        formdata = new FormData();
        if (formdata) {
            console.log("Sending img 2");
            formdata.append("image", pic);
            jQuery.ajax({
                url: "10.230.212.179:5000/climb/api2/",
                type: "POST",
                data: formdata,
                processData: false,
                contentType: false,
                success:function(data){
                    console.log("Received reply")
                    console.log(data);
                    //Assuming i receive an array of .jpg images here

                }
            });
        }
        */
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

    function goToPicPage(picAndColor) {
        $("#startPic").hide();
        $("#page2").show();
        createColorSelectors(picAndColor)
    }

    function createColorSelectors(object) {

        i = 0;
        for (var property in object) {
            if (object.hasOwnProperty(property)) {
                //alert(property+object[property]);
                var markup = "<div class=\"btn btn-squared-default btn-danger\" id='${index}'>${color}</div>"
                $.template("buttonTemplate",markup);

                $.tmpl("buttonTemplate",{
                    color: property,
                    index: i
                }).appendTo("#colorButtons");

                /*
                $("#colorButtons").append( "buttonTemplate" , {
                    color: property,
                    index: i
                });
                */
            }
            i++;
        }
        /*
        for (i = 0; i < picStruct.pics.length(); i++) {
            var t = $.template('<div id="${index}">${color}</div>');

            $("#colorButtons").append( t , {
                color: picStruct.colors[i],
                index: i
            });
        }
        */

    }


    //input.files[0]
});



