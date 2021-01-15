<template>
  <div
    class="page"
    :style="{
      backgroundImage: 'url(\'' + require('@/assets/bg-2.png') + '\')',
    }"
  >
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-10">
          <div class="card mb-3 py-5 px-4">
            <div class="row g-0 justify-content-center">
              <div class="col-lg-8">
                <div class="card-body d-flex flex-column">
                  <h1 class="card-title text-uppercase text-center">
                    Compra {{ product.name }}
                  </h1>

                  <div
                    class="d-flex justify-content-between align-items-center"
                  >
                    <span class="text-red-dark">Total producto:</span>
                    <span class="text-red-dark price"
                      >${{ formatPrice(product.price + product.tax) }}</span
                    >
                  </div>
                  <div class="divider"></div>
                  <div class="d-flex justify-content-between">
                    <span class="text-red-dark">Detalles de la compra:</span>
                    <div class="d-flex flex-column align-items-end">
                      <span class="text-red-dark price"
                        >${{ formatPrice(product.price) }}</span
                      >
                      <span class="text-red-dark"
                        >+${{ formatPrice(product.tax) }}</span
                      >
                      <span
                        class="text-red-dark discount"
                        v-if="product.discount_rate !== 0"
                        >-{{ product.discount_rate*100 }}% de descuento</span
                      >
                    </div>
                  </div>
                  <div class="divider"></div>
                  <div class="d-flex justify-content-between align-items-center mb-5">
                    <span class="text-red-dark">Total de la compra:</span>
                    <span class="text-red-dark price">${{ formatPrice(product.total) }}</span>
                  </div>

                  <div class="">
                    <FormulateForm name="checkout" v-model="order" @submit="handleSubmit">
                      <div class="row">
                        <div class="col-md-6">
                          <FormulateInput
                            name="first_name"
                            label="Nombre"
                            validation="required|alpha:default|min:3"
                          />
                        </div>
                        <div class="col-md-6">
                          <FormulateInput
                            name="last_name"
                            label="Apellido"
                            validation="required|alpha:default|min:3"
                          />
                        </div>
                      </div>
                      <FormulateInput
                        name="email"
                        label="E-mail"
                        validation="required|email"
                      />
                      <FormulateInput
                        name="card_number"
                        label="Tarjeta"
                        validation="required|number|max:2147483646"
                      />
                      <div>
                        <FormulateInput
                          type="submit"
                          label="Finalizar compra"
                          :input-class="(context, classes) => ['btn', 'btn-primary']"
                        />
                      </div>
                    </FormulateForm>
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
  name: "Checkout",
  data() {
    return {
      order: {
        first_name: null,
        last_name: null,
        email: null,
        card_number: null,
      },
    };
  },
  computed: {
    product() {
      // We will see what `params` is shortly
      console.log(this.$store.state.count);
      return this.$store.state.product;
    },
  },
  methods: {
    setData(product) {
      this.product = product;
    },
    handleSubmit(data) {
      data["product"] = this.product;

      console.log(data);
      axios
        .post("http://localhost:8000/orders/", { ...data })
        .then((response) => {
          console.log(response.data);
          alert('Compra realizada satisfactoriamente');
          this.$formulate.reset('checkout')
      });
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