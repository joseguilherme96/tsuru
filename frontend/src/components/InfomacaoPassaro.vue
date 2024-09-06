<template>
    <p class="px-2 mt-2" v-show="exibirMensagem">{{ mensagem }}</p>
    <p class="px-2" v-show="dados.diaNascimentoPassaro"><strong class="cor-texto">Dia de Nascimento : </strong> Dia
        {{
            dados.diaNascimentoPassaro }}</p>
    <p class="px-2" v-show="dados.idadePassaro"> <strong class="cor-texto">Idade :</strong> {{ dados.idadePassaro }}
        Dias</p>
    <p class="px-2" v-show="dados.tamanho"><strong class="cor-texto">Tamanho :</strong> {{ dados.tamanho }}</p>
    <p class="px-2" v-show="dados.codigoPassaro"><strong class="cor-texto">Código :</strong> {{ dados.codigoPassaro
        }}
    </p>
    <p class="px-2" v-show="dados.numeroCorPassaro"><strong class="cor-texto">Cor :</strong>
        {{ dados.cor
        }}
    </p>
    <p class="px-2" v-show="dados.localizacao"><strong class="cor-texto">Localização:</strong> {{ dados.localizacao
        }}
    </p>
    <p class="px-2" v-show="dados.feito_por"><strong class="cor-texto">Feito por :</strong> {{ dados.feito_por }}
    </p>
    <p class="px-2" v-show="dados.entregue_por"><strong class="cor-texto">Entregue por :</strong> {{
        dados.entregue_por
        }} </p>
    <p class="px-2" v-show="dados.dono"><strong class="cor-texto">Dono :</strong> {{ dados.dono }} </p>

</template>
<script setup>

import { watch, ref } from 'vue';

const props = defineProps({

    codPassaro: {

        type: String
    }

});

const emit = defineEmits(['alteraCorPassaro']);

const mensagem = ref('');
const exibirMensagem = ref(false);
const dados = ref({ diaNascimentoPassaro: null })
const cores = ref([
    { hexadecimal: 16777215, nome: 'Branco' },
    { hexadecimal: 0x00000, nome: 'Preto' },
    { hexadecimal: 0x9B96CE, nome: 'Cool gray' },
    { hexadecimal: 0xB9B5D9, nome: 'Periwinkle' },
    { hexadecimal: 0x2C6BA8, nome: 'Green Blue' },
    { hexadecimal: 0x06B5EA, nome: 'Process Cyan' },
    { hexadecimal: 0xACE2F8, nome: 'Non Photo Blue' },
    { hexadecimal: 0x069F67, nome: 'Shamrock green' },
    { hexadecimal: 0xC3D2AB, nome: 'Tea green' },
    { hexadecimal: 0xB9D354, nome: 'Yellow Green' },
    { hexadecimal: 0xDCECA4, nome: 'Mindaro' },
    { hexadecimal: 0xFAD848, nome: 'Mustard' },
    { hexadecimal: 0xF7F050, nome: 'Icterine' },
    { hexadecimal: 0xEB9C41, nome: 'Butterscotch' },
    { hexadecimal: 0xC57858, nome: 'Brown sugar' },
    { hexadecimal: 0xFDE1B7, nome: 'Navajo white' },
    { hexadecimal: 0xFBC48B, nome: 'Peach' },
    { hexadecimal: 0xFB689E, nome: 'Clyclamen' },
    { hexadecimal: 0xFACCE0, nome: 'Fairy Tale' },
    { hexadecimal: 0xFEEBF1, nome: 'Lavender blush' },
    { hexadecimal: 0xFB0204, nome: 'Off red' }
])

//Baseado no código do passaro
const calculaIdadePassaro = () => {

    const dataAtual = ref(new Date());
    const nascimentoDoPassaro = ref(new Date(2024, 7, dados.value.diaNascimentoPassaro));
    const umDiaEmMilissegundos = 24 * 60 * 60 * 1000;

    return Math.floor((dataAtual.value.getTime() - nascimentoDoPassaro.value.getTime()) / umDiaEmMilissegundos);

}

//Função watch observa o recebimento de um numero de um passaro

// O código de um passaro pode ser formado por até 4 ou 5 conjuto de algarismo

//Passaros com 4 conjuntos de algarimos
/* 

    # Exemplo 1 - Passaro com o numero 111*

    Se separarmos este conjunto temos :

    1 - O numero do dia que o passaro foi feito
    1 - A meta da quantidade de passaros a fazer no dia
    1 - A posição do passaro feito no dia
    * -  Caso o codigo tem um *, foi um passaro feito a mais do que a meta estabelecida, ou seja se torna um passaro especial

*/

//Passaros com 5 conjuntos de algarimos
/* 

    # Exemplo 2 - Passaro com o numero 36115*

    Se separarmos este conjunto temos :

    36 - Representa o numero do dia que o passaro foi feito
    1 - A meta da quantidade de passaros a fazer no dia
    1 - A posição do passaro feito no dia
    5  - O numero da cor do passaro(Temos numeros de cores de 1 a 21 conforme variavel cores)
    * -  Caso o codigo tem um *, foi um passaro feito a mais do que a meta estabelecida, ou seja se torna um passaro especial

*/

watch(
    () => props.codPassaro,
    (newVal) => {

        exibirMensagem.value = false;

        const codigo = ref();

        //Caso o código contenha * elimina-os
        //Separa o código em numeros menores para extrair informações, pois cada conjunto tem um signicado
        codigo.value = newVal.split('*')[0].split('');

        //Verifica se todos os codigos são numeros
        let filtro = codigo.value.filter((numero) => isNaN(parseInt(numero)))

        if (filtro.length > 0) {

            mensagem.value = "Código inválido !";
            dados.value = {}
            exibirMensagem.value = true;

            return;

        }

        
        //Os códigos possuem significados, começo de verificação no tamanho do codigo do passsaro e
        // realizando extração de partes do código na busca de informações
        if (codigo.value.length == 3) {

            dados.value.diaNascimentoPassaro = codigo.value[0]; //Extraindo parte do codigo
            dados.value.metaDoDiaQtdPassarosParaFazer = codigo.value[1];//Extraindo parte do codigo
            dados.value.numeroDoPassaroNoDia = codigo.value[2]; //Extraindo parte do codigo
            dados.value.codigoPassaro = newVal;
            dados.value.idadePassaro = calculaIdadePassaro();
            dados.value.especial = false;
            dados.value.cor = ""
            dados.value.numeroCorPassaro =""

        } else if (codigo.value.length == 4) {

            dados.value.diaNascimentoPassaro = codigo.value[0] + codigo.value[1]; //Extraindo parte do codigo
            dados.value.metaDoDiaQtdPassarosParaFazer = codigo.value[2]; //Extraindo parte do codigo
            dados.value.numeroDoPassaroNoDia = codigo.value[3]; //Extraindo parte do codigo
            dados.value.codigoPassaro = newVal;
            dados.value.cor =""
            dados.value.numeroCorPassaro=""
            dados.value.idadePassaro = calculaIdadePassaro();
            dados.value.especial = false;

        } else if (codigo.value.length == 5) {

            dados.value.numeroCorPassaro  = codigo.value[4];
            if (dados.value.numeroCorPassaro > 21) {

                mensagem.value = "Código com código de cor inválida !";
                dados.value = {}
                exibirMensagem.value = true;

                return
            }

            dados.value.diaNascimentoPassaro = codigo.value[0] + codigo.value[1]; //Extraindo parte do codigo
            dados.value.metaDoDiaQtdPassarosParaFazer = codigo.value[2];//Extraindo parte do codigo
            dados.value.numeroDoPassaroNoDia = codigo.value[3];//Extraindo parte do codigo
            dados.value.cor = cores.value[dados.value.numeroCorPassaro].nome;
            dados.value.codigoPassaro = newVal;
            dados.value.idadePassaro = calculaIdadePassaro();
            dados.value.especial = false;

            emit('alteraCorPassaro', cores.value[dados.value.numeroCorPassaro - 1].hexadecimal);

        } else if (codigo.value.length == 6) {

            dados.value.numeroCorPassaro = parseInt(codigo.value[4] +""+ codigo.value[5]); //Extraindo parte do codigo

            if (dados.value.numeroCorPassaro > 21) {

                mensagem.value = "Código com código de cor inválida !";
                dados.value = {}
                exibirMensagem.value = true;

                return
            }

            dados.value.diaNascimentoPassaro = codigo.value[0] + codigo.value[1];//Extraindo parte do codigo
            dados.value.metaDoDiaQtdPassarosParaFazer = codigo.value[2]; //Extraindo parte do codigo
            dados.value.numeroDoPassaroNoDia = codigo.value[3]; //Extraindo parte do codigo
            dados.value.cor = cores.value[ dados.value.numeroCorPassaro - 1].nome;
            dados.value.codigoPassaro = newVal;
            dados.value.idadePassaro = calculaIdadePassaro();
            dados.value.especial = false;

            
            emit('alteraCorPassaro', cores.value[dados.value.numeroCorPassaro - 1].hexadecimal);

        } else {

            mensagem.value = "Não foram encontrado informações do seu passaro !";
            dados.value = {}
            exibirMensagem.value = true;

        }
    }
)


</script>