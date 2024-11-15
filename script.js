// alteração: função para mostrar o conteúdo dinâmico
function showContent(index) {
    const contentDiv = document.getElementById("content");
    contentDiv.innerHTML = `<p>${contents[index]}</p>`;
    
// alteração: reaplica o ScrollReveal após a atualização do conteúdo
    ScrollReveal().reveal('.content', { delay: 100, reset: true });
};

// alteração: função para executar o ScrollReveal após o carregamento completo da página
window.onload = function() {
    ScrollReveal().reveal('.hero', { delay: 100 });
    ScrollReveal().reveal('.sobre', { delay: 200 });
    ScrollReveal().reveal('.noticias', { delay: 300 });
    ScrollReveal().reveal('.card-cartilha', { delay: 400 });
    ScrollReveal().reveal('.content', { delay: 100, reset: true });
};


$(document).ready(function(){
    $('.news-carousel').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1050,
        centerMode: true,
        variableWidth: true,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            }
        ]
    });


    $('.carousel .carousel-inner').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        centerMode: true,
        variableWidth: true,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            }
            
        ]
    });
});