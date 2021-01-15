<template>
  <div
  class="page"
    :style="{
      backgroundImage: 'url(\'' + require('@/assets/bg-1.png') + '\')',
    }"
  >
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-10">
          <div class="card mb-3 py-5 px-4">
            <div class="row g-0">
              <div class="col-lg-5">
                <img :src="getImage()" class="img-fluid" alt="..." />
              </div>
              <div class="col-lg-7">
                <div class="card-body d-flex flex-column py-lg-0 px-lg-5">
                  <h1 class="card-title">{{ product.name }}</h1>
                  <h3>${{ formatPrice(product.price) }}</h3>
                  <span class="tax mb-2"
                    >${{ formatPrice(product.tax) }} imp.</span
                  >
                  <span class="discount mb-5" v-if="product.discount_rate !== 0"
                    >-{{ product.discount_rate * 100 }}%</span
                  >
                  <p class="text-red">Descripción</p>
                  <div class="divider"></div>
                  <p class="card-text mb-4">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Duis convallis est placerat efficitur auctor. Integer
                    fermentum sem in quam rutrum, eu pretium purus pellentesque.
                    Duis nec pretium ligula, eu faucibus felis. Aliquam
                    ultricies sapien magna, sit amet aliquet tellus mollis et.
                  </p>
                  <div>
                    <button class="btn btn-primary btn-lg" v-on:click="goToCheckout">
                      Comprar
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
      product: {},
    };
  },
  beforeRouteEnter(to, from, next) {
    axios.get("http://localhost:8000/orders/product/").then((response) => {
      next((vm) => vm.setData(response.data));
    });
  },
  methods: {
    setData(product) {
      this.product = product;
    },
    getImage() {
      return this.product.image;
    },
    goToCheckout() {
      this.$store.commit("setProduct", this.product);
      this.$router.push("/checkout");
    },
    formatPrice(value) {
      let val = (value / 1).toFixed(2).replace(".", ",");
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    },
  },
};
</script>

<style>
</style>