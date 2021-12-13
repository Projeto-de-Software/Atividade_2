$(document).ready(()=> {
    $(".deletar").click(function () {
        let url = $(this).attr("url");
        console.log(url);
        document.getElementById("confirmaDeletar").href = url;
        $("#modalDeletarItem").modal("show");
    });

    let url = window.location.href
    if (url.toString().indexOf('armazem') > -1){
        $(".all-nav-item").removeClass("active");
        $('.armazem').addClass("active");
    }
    else if (url.toString().indexOf('caixa') > -1){
        $(".all-nav-item").removeClass("active");
        $('.caixa').addClass("active");
    }
    else if (url.toString().indexOf('palet') > -1){
        $(".all-nav-item").removeClass("active");
        $('.palet').addClass("active");
    }
    else if (url.toString().indexOf('produto') > -1){
        $(".all-nav-item").removeClass("active");
        $('.produto').addClass("active");
    }
    else if (url.toString().indexOf('setor') > -1) {
        $(".all-nav-item").removeClass("active");
        $('.setor').addClass("active");
    } else if (url.toString().indexOf('regra') > -1){
        $(".all-nav-item").removeClass("active");
        $('.regra').addClass("active");
    }
});
