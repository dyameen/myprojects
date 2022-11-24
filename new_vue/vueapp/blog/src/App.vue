<template>
  <div>
  <MyHome data="Yameen is here." msg="Learning Vue.js"/>
    <br><br><hr>
  <EmpList/>
  </div>
</template>

<script>
import MyHome from './components/Home.vue'
import EmpList from './components/EmployeeList.vue'

export default {
  name: 'App',
  components: {
    //HelloWorld,
    MyHome,
    EmpList,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
