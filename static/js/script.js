const contents = [
    "De maneira simplificada, o racismo ocorre quando as pessoas são tratadas de maneiras diferentes (seja para receber benefícios ou negação de seus direitos, por exemplo) por causa de seus traços fenotípicos (como a cor da pele, a textura do cabelo, o formato do nariz) ou por sua etnia (sua nacionalidade, afiliação tribal, religião, língua e as tradições de um determinado grupo). Isso pode acontecer de modo proposital ou não, mas acaba prejudicando alguns grupos, como por exemplo negros e indígenas, e beneficiando outros, como a população branca.",
    "O racismo se manifesta...",
    "quem sofre racismo no Brasil...",
    "Como identificar no ambiente escolar...",
    "O que fazer em um caso de racismo..."
];

function showContent(index) {
    const contentDiv = document.getElementById("content");
    contentDiv.innerHTML = `<p>${contents[index]}</p>`;
}

ScrollReveal().reveal('.hero', { delay: 100 });
ScrollReveal().reveal('.card-cartilha', { delay: 300 });
ScrollReveal().reveal('.testimonials', { delay: 500 });
ScrollReveal().reveal('.about', { delay: 700 });
ScrollReveal().reveal('.card', { interval: 50 });

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