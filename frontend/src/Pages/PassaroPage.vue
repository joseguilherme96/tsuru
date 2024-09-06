<template>

    <div class="row justify-content-center m-3 d-flex vh-100 vw-100">

        <div class="d-flex justify-content-center align-items-center" v-show="!codPassaro">
            <div class="text-center cor-texto">
                <Apresentacao v-show="!codPassaro"></Apresentacao>
                <Pesquisa @codigoPassaro="setCodigoPassaro"></Pesquisa>
            </div>
        </div>


        <div class="col-12 col-lg-8" v-show="codPassaro">
            <Passaro :cor="corPassaro" ></Passaro>
        </div>
        <div class="col-12 col-lg-4 p-2" v-show="codPassaro">
            <div class="col-11  border mt-5">
                <InfomacaoPassaro :codPassaro="codPassaro" @alteraCorPassaro="alteraCorPassaro"></InfomacaoPassaro>
                <ButtonAlteraCorPassaro @alteraCorPassaro="alteraCorPassaro" :cor="corPassaro"></ButtonAlteraCorPassaro>
            </div>

        </div>

        <PassarosAtivos v-show="codPassaro" :codPassaro="codPassaro"></PassarosAtivos>

        <div class=" col-12 col-lg-12" v-show="codPassaro">
            <Creditos></Creditos>

        </div>
    </div>

</template>

<script setup>

import Pesquisa from '@/components/Pesquisa.vue';
import InfomacaoPassaro from '@/components/InfomacaoPassaro.vue';
import Creditos from '@/components/Creditos.vue';
import Passaro from '@/components/Passaro.vue';
import { ref } from 'vue';
import ButtonAlteraCorPassaro from '@/components/ButtonAlteraCorPassaro.vue';
import PassarosAtivos from '@/components/PassarosAtivos.vue';
import Apresentacao from '@/components/Apresentacao.vue';

const corPassaro = ref(0x9995C9);
const codPassaro = ref(null);

const alteraCorPassaro = (value) => {

    corPassaro.value = value;

}

const setCodigoPassaro = (value) => {

    codPassaro.value = value;

}


</script>
