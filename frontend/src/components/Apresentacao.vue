<template>

    <h1>{{ exibindoMensagem }}</h1>

</template>
<script setup>

import {ref} from 'vue';

const fraseChamativa = "Bem vindo ao mundo dos passaros !".split(" ");
const exibindoMensagem = ref('');

// Função para exibir a frase lentamente
const exibirFraseLentamente = () => {
    let delay = 0; // Tempo inicial de atraso

    fraseChamativa.forEach((palavra) => {
        palavra.split("").forEach((letra, index) => {
            setTimeout(() => {
                exibindoMensagem.value += letra;
            }, delay + index * 300); // Ajuste o intervalo entre letras conforme necessário
        });

        delay += palavra.length * 300; // Adiciona o tempo de atraso entre palavras
        setTimeout(() => {
            exibindoMensagem.value += " ";
        }, delay); // Adiciona um espaço entre palavras
    });
};

// Chama a função para iniciar a exibição da frase
exibirFraseLentamente();

</script>