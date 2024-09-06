<script setup>

defineProps({
    cor: {
        type: Number,
    },
});


</script>

<template>

    <div id="passaro">

    </div>
</template>
<style>
:root {

    --bg-color: #655f4815;
    --text-color: white;
    --text-align: center
}

body {
    margin: 0;
}

.cor-texto {

    color: #655f48;
}

.cor-borda {

    border: #655f48 solid 3px !important;
}
</style>

<script>

import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { ref, watch } from 'vue';

export default {



    data() {

        const fov = ref(50);
        const camera = ref(null);
        const childAltera = ref(null)

        const corLAterada = this.cor;

        const verificaAjuste = () => {

            if (window.innerWidth < 500) {

                this.fov = 75;

            } else if (window.innerWidth < 400) {


                this.fov = 100;
            } else if (window.innerWidth < 300) {


                this.fov = 150;
            } else {

                this.fov = 50;
            }

            // Atualiza o FOV da câmera
            this.camera.fov = this.fov;
            this.camera.updateProjectionMatrix();

        }


        return {
            fov,
            verificaAjuste
        }


    },
    watch: {
        
        'cor'(newCor) {
            this.childAltera.material.color.set(newCor);
        }
    },


    mounted() {

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(this.fov, window.innerWidth / window.innerHeight, 0.1, 2000);
        this.camera = camera;
        const renderer = new THREE.WebGLRenderer();

        this.verificaAjuste();

        window.addEventListener('resize', this.verificaAjuste, false)


        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0xffffff); // Cor de fundo branca

        let div_passaro = document.getElementById('passaro');
        div_passaro.appendChild(renderer.domElement);


        // Configura o OrbitControls
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true; // Animação suave
        controls.dampingFactor = 0.25; // Fator de amortecimento
        controls.enableZoom = true; // Permite zoom

        // Carrega o modelo GLB
        const loader = new GLTFLoader();

        loader.load('/models/tsuru_-_origami.glb', (gltf) => {
            scene.add(gltf.scene);
            gltf.scene.scale.set(200, 200, 200); // Ajuste o tamanho conforme necessário
            gltf.scene.position.set(0, 0, 0); // Ajuste a posição conforme necessário

            // Modifica a cor de todos os materiais no modelo
            gltf.scene.traverse((child) => {
                if (child.isMesh) {
                    this.childAltera = child;
                    child.material.color.set(this.cor); // Altere a cor aqui
                }
            });
        });

        // Adiciona luzes
        const ambientLight = new THREE.AmbientLight(0xffffff); // Luz ambiente
        scene.add(ambientLight);

        const directionalLight = new THREE.DirectionalLight(0xffffff, 1); // Luz direcional
        directionalLight.position.set(1, 1, 1).normalize();
        scene.add(directionalLight);

        // Configura a posição da câmera
        camera.position.set(0, 0, 50);

        function animate() {
            requestAnimationFrame(animate);
            controls.update(); // Atualiza os controles do mouse
            renderer.render(scene, camera);
        }
        animate();


    }


}


</script>