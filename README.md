# Trabalho Computação Gráfica

Projeto desenvolvido para disciplina SSC0250 - Computação Gráfica.

### Alunos:
*  **Fábio Verardino de Oliveira** - 12674547
*  **Rafael Sartori Vantin** - 12543353

## Introdução

O projeto consiste em um cenário 3D [x] que pode ser navegado pela câmera, com o uso das WASD 
para movimentação e do mouse para rotacionar a câmera. Além disso o usuário pode pressionar
a tecla 'P' a qualquer momento para alternar entre o modo de visão com textura e o modo de
visão com wireframe (malha de polígonos).

O cenário é composto por:
* **Um terreno com textura de grama**, que contém:
  * **Uma casa de madeira**, com telhado triangular e chaminé;
  * **Um gato laranja**, animado com translação e rotacão oscilantes;
  * **O espaço interno da casa**, que contém:
    * **Uma caixa de madeira**;
    * **Um abacaxi**, sobre a caixa de madeira;
    * **Uma caveira flutuante pequena**, animada de forma que sempre olhe em direção à câmera;
* **Um terreno com textura de areia**, que contém:
  * **Uma torre de vigia de madeira**;
  * **Uma caveira flutuante grande**, animada com rotação e escala oscilante;

## Requisitos
1. [x] O cenário deve conter um ambiente interno e externo.
    * Casa de madeira
2. [x] O ambiente interno pode ser obtido por meio de uma habitação, como casa, prédio, cabana, entre outros.
3. [x] Adicione pelo menos três modelos dentro da habitação (ambiente interno). Por exemplo, se o ambiente interno for uma casa, então a casa pode conter móveis como sofá e televisão. Também pode conter moradores, como humanos e animaisde estimação.
    * Caixa de madeira, abacaxi, caveira flutuante pequena
4. [x] O terreno/chão da habitação deve ter alguma textura diferente do ambiente externo.
    * Chão de madeira, dentro da casa
5. [x] O terreno/chão do ambiente externo deve ter no mínimo duas texturas diferentes. Por exemplo, uma parte do terreno pode ser grama e outra parte asfalto/pedra.
    * Terrenos de grama e areia
6. [x] O ambiente externo deve ter no mínimo três modelos, como árvores, carros, pessoas, animais, entre outros.
    * Torre de vigia de madeira, gato laranja, caveira flutuante grande, casa de madeira
7. [x] Escolha pelo menos 1 modelo para aplicar transformações geométricas de rotação, escala e translação, conforme eventos do teclado.
    * Caveira flutuante grande, caveira flutuante pequena, gato laranja
8. [x] O seu cenário deve ter um céu para o ambiente externo, com sua respectiva textura. Dica: pesquisar SkyBox.
9. [x] O seu programa deve restringir a exploração do cenário dentro dos limites da “borda” do céu e terreno. Não é necessário restringir o acesso aos modelos, ou seja, a câmera pode passar livremente “por dentro” dos modelos (com exceção do céu e terreno).
10. [x] O seu programa deve permitir ativar o modo de visualização de malha poligonal a qualquer momento, pressionando a tecla P. Ao pressionar novamente a tecla P, voltar ao modo textura.
