<template>
    <label class="px-2">
        <strong class="cor-texto">Altere a cor do seu pássaro:</strong>
    </label>
    <input type="color" :value="corPassaro" @change="alteraCorTema">
</template>

<script setup>
import { ref, watch } from 'vue';

//Define props codCor
const props = defineProps({
    cor: {
        type: Number,
    },
});

// Define os eventos que o componente pode emitir
const emit = defineEmits(['alteraCorPassaro']);

const corPassaro = ref(null);

// Função para converter hex para decimal
function hexToDecimal(hex) {
    return parseInt(hex.replace('#', ''), 16);
}

function decimalToHex(decimal) {
    let hex = decimal.toString(16); // Converte o decimal em hexadecimal
    return "#" + hex.padStart(6, '0'); // Adiciona o '#' e preenche com zeros à esquerda se necessário
}

// Função para lidar com a mudança de cores
function alteraCorTema(event = "", decimal = "") {

    let colorHex = "";
    let colorDecimal = "";

    if (event != "") {
        colorHex = event.target.value;
        colorDecimal = hexToDecimal(colorHex);
        emit('alteraCorPassaro', colorDecimal);
    } else if (decimal != "") {

        colorHex = decimalToHex(decimal)
        colorDecimal = decimal;
    }


    // Altera as cores da página baseado na cor selecionada do pássaro
    document.querySelector('svg').setAttribute('fill', colorHex);
    document.querySelectorAll('.cor-texto').forEach((dado) => {

        if (colorHex == "#ffffff") {

            dado.style.color = "#000000";

            return;

        }
        dado.style.color = colorHex;
    });

    corPassaro.value = colorHex;

}

watch(

    () => props.cor,
    (newVal) => {

        alteraCorTema("", newVal)

    }
)

</script>
