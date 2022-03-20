<template>
  <div id="app">
      <router-link to="/"></router-link>
    <router-view/>
  </div>
</template>
<style>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css");
@import url("https://use.fontawesome.com/releases/v5.7.2/css/all.css");
@import url("../src/assets/css/style.css");
@import url("../src/assets/css/components.css");
    .my-custom-scrollbar {
    position: relative;
    height: 350px;
    overflow: auto;
    }
    .table-wrapper-scroll-y {
    display: block;
    }
    .table.b-table>thead>tr>th {
      background-color: #dee2e6;
      position: sticky;
      position: -webkit-sticky;
      top: 0;
      z-index: 2;
    } 
</style>