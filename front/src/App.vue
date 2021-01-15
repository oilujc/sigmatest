<template>
  <div id="app">
      <router-view />

  <div class="container pb-4">
    <div class="row justify-content-center">
      <div class="col-lg-2">
      <img src="@/assets/logo.png" width="150px" height="100px" alt="">
      </div>
    </div>
  </div>
  </div>
</template>

<style>
#app {
  font-family: "Poppins", sans-serif;
  margin: 0;
  background-color: #fdf1e2;
}

.page {
  padding-top: 10rem;
  background-color: #fdf1e2;
  background-position: top; /* Center the image */
  background-repeat: no-repeat; /* Do not repeat the image */
  background-size: 100% 60vh;
}

#app .page .container {
  min-height: 100vh;
}

ul {
  padding: 0;
}

ul li {
  list-style: none;
}

.card {
  border: none !important;
  box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.3);
}

.card .card-body h1 {
  margin-bottom: 1rem;
  color: #63484e;
  font-size: 2rem;
  font-weight: 600;
}

.card .card-body h3, .card .card-body span.price {
  color: #63484e;
  font-size: 1.5rem;
  font-weight: 400;
}

.card .card-body p {
  margin: 0;
}

.card .card-body span.tax {
  color: #bbb8b8;
  font-size: .9rem;
}

.card .card-body span.discount {
  color: #7d5050;
  font-size: 1rem;
  font-weight: 600;
}

.card .card-body div.divider {
  margin-top: .3rem;
  margin-bottom: .8rem;
  border: 0;
  border-top: 2px solid #7d5050;
}
.card .card-body p.text-red {
  color: #7d5050;
  font-size: .9rem;
  font-weight: 500;
}
.card .card-body .text-red-dark, form label {
  color: #5f4043;
  font-size: .9rem;
  font-weight: 500;
}

.card .card-body p.card-text {
  color: #af9993;
  font-size: .9rem;
  font-weight: 500;
}

.card .card-body button.btn-primary {
  background-color: #7d5050;
  border: none;
}

form .form-control {
  border-color: #7d5050;
}


</style>
