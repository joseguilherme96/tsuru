<template>
    <div class="col-12 col-lg-12 d-flex">
        <input type="text" class="form-control  border" placeholder="Digite o código do seu pássaro"
            v-model="codigoPassaro" @change="setCodigoPassaro">
        <button class="btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#655f48" class="bi bi-search"
                viewBox="0 0 16 16">
                <path
                    d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0">
                </path>
            </svg>
        </button>
    </div>
</template>
<script setup>

import { ref } from 'vue'

const codigoPassaro = ref(null);
const emit = defineEmits(['codigoPassaro']);
const setCodigoPassaro = () => {

    emit('codigoPassaro', codigoPassaro.value)

}

</script>