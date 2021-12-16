function handleFiles() {
//    var files = event.target.files;
    files = $('#upload-file')[0]
    $("#src").attr("src", URL.createObjectURL(files[0]));
    document.getElementById("audio").load();
    }
//
////document.getElementById("upload").addEventListener("change", handleFiles, false);
//window.onload=function(){
//    var elId = document.getElementById('upload');
//    if(elId){
//      elId.addEventListener('change', handleFiles, false);
//}
//}

$(function() {
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
//        handleFiles()
//        document.getElementById("upload-file")[0].addEventListener("change", handleFiles, false);
//        $("#src").attr("src", URL.createObjectURL(form_data[0]));
//        document.getElementById("audio").load();
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
                op = JSON.parse(data)
                console.log(data)
                alert(op["output"])
            },
        });
    });
});


$(function() {
    $('#start-processing-btn').click(function() {
//        handleFiles()
//        document.getElementById("upload-file")[0].addEventListener("change", handleFiles, false);
//        $("#src").attr("src", URL.createObjectURL(form_data[0]));
//        document.getElementById("audio").load();
        $.ajax({
            type: 'POST',
            url: '/startprocessing',
            data: "",
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
                console.log(data)
            },
        });
    });
});
