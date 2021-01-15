import Vue from 'vue'
import App from './App.vue'
import router from './router'

import VueFormulate from '@braid/vue-formulate'
import Vuex from 'vuex'


import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.use(VueFormulate, {
    classes: {
        input: ['form-control', 'mb-3'],
        errors: ['p-0', 'm-0'],
        error: ['alert', 'alert-danger', 'text-sm'],
    }
})

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        product: {}
    },
    mutations: {
        setProduct(state, data) {
            state.product = data
        }
    }
})

Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')