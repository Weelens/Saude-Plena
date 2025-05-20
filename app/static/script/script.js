// testando js
//variaveis
var texto_alerta = document.querySelector("#alerta_txt");
var texto_ex = document.querySelector("#dicas_ex");
var texto_ali = document.querySelector("#dicas_al");

//alterando

texto_alerta.textContent = "Antes de iniciar qualquer plano de exercícios físicos ou mudanças na alimentação, é fundamental consultar um profissional da saúde, como um educador físico ou nutricionista. Cada pessoa tem necessidades únicas, e a orientação especializada garante segurança e melhores resultados.";


texto_ex.textContent = "Se você quer começar a se movimentar, melhorar sua saúde ou dar um passo a mais nos seus treinos, este guia é para você. Com orientações acessíveis e práticas, ele traz exercícios que podem ser feitos em casa ou na academia, com dicas para quem está começando ou quer evoluir com consciência e segurança. Baixe e comece hoje mesmo a cuidar do seu corpo!";


texto_ali.textContent= "Comer bem não precisa ser complicado. Este material reúne orientações simples e eficazes sobre alimentação equilibrada, incluindo sugestões de alimentos, horários e combinações inteligentes para o dia a dia. Ideal para quem quer mais energia, saúde e qualidade de vida. Baixe o conteúdo e descubra como melhorar sua alimentação de forma prática!";
console.log(texto_alerta,texto_ex,texto_ali);

let meses = [' Janeiro ' ,
    ' Fevereiro ' ,
    ' Março ' ,
    ' Abril ' ,
    ' Maio ' ,
    ' Junho ' ,
    ' Julho ' ,
    ' Agosto ' ,
    ' Setembro ' ,
    ' Outubro ' ,
    ' Novembro ' ,
    ' Dezembro ']
let data = new Date();
let diaNumero = data.getDay();
let dia = data.getDate();
let mes = meses[data.getMonth()]
let ano = data.getFullYear()

let ativo = document.querySelector(".calen_semana li:nth-child("+diaNumero+")")
ativo.classList.add('atual')
let h1 = document.createElement('h1')
h1.innerHTML= dia;
ativo.appendChild(h1);

let h5 = document.createElement('h5')
h5.innerHTML= mes;
ativo.appendChild(h5);

let h3 = document.createElement('h3')
h3.innerHTML= ano;
ativo.appendChild(h3);