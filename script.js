const contents = [
    "O racismo é...",
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


