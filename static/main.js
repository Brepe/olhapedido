function calculateQTc(caixa) {
    // div_subprod = $('.div-subprod');
    // $(div_subprod).innerHTML = '';
    dou = document.getElementsByClassName("div-subprod")[0];
    dou.innerHTML = '';
    var server_data = [
        { "caixa": caixa }
    ]; 
    $.ajax({
        type: "POST",
        url: "/select_product",
        data: JSON.stringify(server_data),
        contentType: "application/json",
        dataType: 'json',
        success: function (subprod) {
            result = ''
            subprod.forEach((s, i) => {
                console.log('%d: %s', i, s['lista'], s['itens'][0]['image']);
                result += '<li class="list-group-item"> \
                <div class="d-flex align-items-center"> \
                  <img src="/static/images/'+s["itens"][0]["image"]+'" alt="Image" name="'+ s["lista"] +'" class="img-thumbnail" style="width: 50px; height: 50px; margin-right: 10px;"> \
                  <div> \
                    <select name="select-subprod-'+ i +'" class="form-select mt-2" aria-label="Default select example"> \
                    <option value="title" disabled selected>'+ s["lista"] +'</option>';

                s["itens"].forEach((item, j) => {
                    result += '<option value="'+item["image"]+'">'+item["nome"]+'</option>';

                });

                result += '</select> \
                                </div> \
                                    </div> \
                                        </li>';
            });
            dou.innerHTML = result;
        }
    });
}

$('.form-select').change(function () {
    var id = $(this).find(':selected')[0].img;
    var img = $(this).parent().parent().find('img');
    $(img).attr('src','static/images/'+id);
    // $.ajax({
    //     type: 'POST',
    //     url: '../include/country.php',
    //     data: {
    //         'id': id
    //     },
    //     success: function (data) {
    //         // the next thing you want to do 
    //         var $city = $('#city');
    //         $city.empty();
    //         for (var i = 0; i < data.length; i++) {
    //             $city.append('<option id=' + data[i].sysid + ' value=' + data[i].name + '>' + data[i].name + '</option>');
    //         }
    //     }
    // });
});