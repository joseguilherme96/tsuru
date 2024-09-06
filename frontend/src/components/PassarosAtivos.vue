<style>
.alert-dismissible {
    z-index: 500;
    position: fixed;
    top: 400px;
    /* Distância do topo da janela */
    right: 20px;
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 100px;
}

.scrollable-list {
    max-height: 300px;
    /* Ajuste para a altura máxima desejada */
    overflow-y: auto;
}
</style>
<template>
    <div class="col-12 col-md-6 col-lg-4 alert-dismissible scrollable-list border ">
        <div class="row cor-texto ">
            <div class="col-12 col-lg-12 text-center ">
                <h5> Passáros ativos</h5>
            </div>
        </div>
        <div class="row">
            <div class="col-3  col-lg-3 cor-texto text-center">
                Status
            </div>
            <div class="col-2  col-lg-3 cor-texto  text-center">
                Nº
            </div>
            <div class="col-4  col-lg-5 cor-texto  text-center">
                Voando em
            </div>
            <div class="col-3  col-lg-1 cor-texto  text-center">
                Visualize
            </div>
        </div>
        <!-- Adicione a classe `scrollable-list` aqui -->
        <div class="row" v-for="passaro in passarosAtivos">
            <div class="col-3  col-lg-3 cor-texto text-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="green" class="bi bi-circle-fill"
                    viewBox="0 0 16 16">
                    <circle cx="8" cy="8" r="8" />
                </svg>
            </div>
            <div class="col-2  col-lg-3 cor-texto">
                {{ passaro.numero_passaro }}
            </div>
            <div class="col-4  col-lg-5 cor-texto">
                {{ passaro.localizacao }}
            </div>
            <div class="col-3  col-lg-1 cor-texto text-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye"
                    viewBox="0 0 16 16">
                    <path
                        d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8M1.173 8a13 13 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5s3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5s-3.879-1.168-5.168-2.457A13 13 0 0 1 1.172 8z" />
                    <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5M4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0" />
                </svg>
            </div>
        </div>
    </div>



</template>
<script setup>

import io from 'socket.io-client'
import { watch, ref } from 'vue';

const props = defineProps({

    codPassaro: {

        type: String

    }

});

const codPassaro = ref(null);
const sid = ref();
const latitude = ref()
const longitude = ref()
const localizacao = ref()

const passarosAtivos = ref([]);

const socket = io('http://127.0.0.1:5000');

socket.on('connect', function (e) {
});

//Retorna a sid do passaro conectado e salva na variavel
socket.on('sid', (data) => {

    sid.value = data.sid;

})

socket.on('response event connect', (e) => {

    passarosAtivos.value = e

})

socket.on('response event disconnected', (e) => {

    passarosAtivos.value = e;

})

watch(

    () => props.codPassaro,
    (newVal) => {


        if (newVal !== "" && codPassaro.value == null) {

            codPassaro.value = newVal;

            //Atribui o numero do passaro para a sid
            passarosAtivos.value.forEach((linha, index) => {

                if (linha.sid == sid.value) {
                    passarosAtivos.value[index].numero_passaro = codPassaro.value;

                    //Pegando a localização do usuário
                    navigator.geolocation.getCurrentPosition(function (position) {
                        latitude.value = position.coords.latitude;
                        longitude.value = position.coords.longitude;

                        //Consultando api para verificar Estado
                        fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude.value}&lon=${longitude.value}`)
                            .then((response) => {

                                return response.json();

                            })
                            .then((data) => {

                                localizacao.value = data.address.town;
                                //Envia informação do numero do passaro para o web socket
                                socket.emit("adiciona_informacoes_para_passaro_conectado", JSON.stringify({ sid: sid.value, numero_passaro: codPassaro.value, localizacao: localizacao.value }));

                            })
                    });



                }

            });

        }

    }

)


</script>
